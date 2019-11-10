import tweepy
import os
from name_generator import generate_tweet
import random 

DEBUG = os.environ["DEBUG"].lower() == "true"
print(f"DEBUG={DEBUG}")
tweet = generate_tweet()
print(tweet)
if not DEBUG:
    CONSUMER_API = os.environ["CONSUMER_API_KEY"]
    CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]
    ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
    ACCESS_SECRET = os.environ["ACCESS_SECRET"]
    auth = tweepy.OAuthHandler(CONSUMER_API, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    api.update_status(f"{tweet}")
