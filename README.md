# OnlineNewsPopularity
Final Project for a Data Analysis in Python course

The Flask API works by asking for the Weekday in between 0 and 7, the category of the article between 0 and 6 and finally the number of words. All the other variables are filled randomly to avoid having to send 47 variables.
You can simply GET or POST to the api to get a response using Weekday Category and NoWords and the parameter names.

**for example**:
http://127.0.0.1:5000/Api?Weekday=3&Category=2&NoWords=1000

**for the weekdays**:
- Monday: 1
- Tuesday: 2
- Wednesday: 3
- Thursday: 4
- Friday: 5
- Saturday: 6
- Sunday: 7
- other: 0

**for the categories**:
- Lifestyle: 1
- Entertainment: 2
- Business: 3
- Social Media: 4
- World: 5
- Tech: 6
- Other: 0
