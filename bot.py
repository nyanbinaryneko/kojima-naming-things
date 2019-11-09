import tweepy
import os
from name_generator import generate_name

DEBUG = os.environ["DEBUG"].lower() == "true"
name = generate_name() 
print(f"kojima name: {name}")
print(f"DEBUG={DEBUG}")
if not DEBUG:
    CONSUMER_API = os.environ["CONSUMER_API_KEY"]
    CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]
    ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
    ACCESS_SECRET = os.environ["ACCESS_SECRET"]
    auth = tweepy.OAuthHandler(CONSUMER_API, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    print(f'bot - new kojima name: {name.lower()}')
    api.update_status(f"Thinking my next game will have {name} as the main character.")
