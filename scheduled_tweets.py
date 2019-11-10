import tweepy
import os
import random 

CONSUMER_API = os.environ["CONSUMER_API_KEY"]
CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]
ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
ACCESS_SECRET = os.environ["ACCESS_SECRET"]

auth = tweepy.OAuthHandler(CONSUMER_API, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

tweets = ["I'm a bad bot. Please alert my mxstress, @ComradeEevee when I do something like tweet something racist or sexist.", "any ideas on how i can be a better bot? want to see some automated Kojima shitposting? https://forms.gle/YyyJYHWZRJdmE9D88"]
for tweet in tweets:
    print(f"scheduled tweet: {tweet}")
    api.update_status(tweet)