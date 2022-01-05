import flask
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import json

dataset = pd.read_csv(r"C:\Users\cg170794\Documents\ESILV\Python 4 Projet\OnlineNewsPopularity.csv")
def weekdays(x):
    if x[" weekday_is_monday"] == 1:
        return 1
    elif x[" weekday_is_tuesday"] == 1:
        return 2
    elif x[" weekday_is_wednesday"] == 1:
        return 3
    elif x[" weekday_is_thursday"] == 1:
        return 4
    elif x[" weekday_is_friday"] == 1:
        return 5
    elif x[" weekday_is_saturday"] == 1:
        return 6
    elif x[" weekday_is_sunday"] == 1:
        return 7
    else:
        return 0

def ArticleType(x):
    if x[" data_channel_is_lifestyle"] == 1:
        return 1
    elif x[" data_channel_is_entertainment"] == 1:
        return 2
    elif x[" data_channel_is_bus"] == 1:
        return 3
    elif x[" data_channel_is_socmed"] == 1:
        return 4
    elif x[" data_channel_is_world"] == 1:
        return 5
    elif x[" data_channel_is_tech"] == 1:
        return 6
    else:
        return 0

dataset["Weekday"] = dataset.apply(weekdays,axis=1)
dataset["Article Type"] = dataset.apply(ArticleType,axis=1)
dataset[' shares']=np.where(dataset[' shares']>= 1400,1,0)

dataset.drop(columns=['url',' timedelta', ' data_channel_is_lifestyle',' data_channel_is_entertainment',' data_channel_is_bus',' data_channel_is_socmed',' data_channel_is_tech',' data_channel_is_world',' weekday_is_monday',' weekday_is_tuesday',' weekday_is_wednesday',' weekday_is_thursday',' weekday_is_friday',' weekday_is_saturday',' weekday_is_sunday'], axis=1,inplace=True)

model = RandomForestClassifier(n_estimators=166,max_depth=37,n_jobs=-1)
model.fit(dataset.drop(" shares",axis=1),dataset[" shares"])

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "Python For Data Analysis - Popularity of an Article"



@app.route('/Api', methods=['GET','POST'])
def Prediciton():
    request = flask.request.args
    article = np.random.rand(1,47)
    article[0,46] = request["Weekday"]
    article[0,45] = request["Category"]
    article[0,1] = request["NoWords"]
    awnser = model.predict(article)
    if awnser == 0:
        stringaswnser = "Not Popular" 
    else:
        stringaswnser = "Popular" 
    return {"article": json.dumps(article.tolist()), "Prediction": stringaswnser, "request" : request}
app.run()