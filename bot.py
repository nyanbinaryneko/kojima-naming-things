import tweepy
import os
from name_generator import generate_name
import random 

DEBUG = os.environ["DEBUG"].lower() == "true"
name = generate_name() 
print(f"kojima name: {name}")
print(f"DEBUG={DEBUG}")
sentences = [f"Thinking my next game will have {name} as the main character.", 
    f"hmmm, is {name} a good name? I'm thinking it fits the character and my vision", 
    f"Ah, yes, {name}. They will be played by Norman Reedus.",
    f"{name} will be an otter furry played by Conan O'brien."]
sentence = random.choice(sentences)
print(sentence)
if not DEBUG:
    CONSUMER_API = os.environ["CONSUMER_API_KEY"]
    CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]
    ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
    ACCESS_SECRET = os.environ["ACCESS_SECRET"]
    auth = tweepy.OAuthHandler(CONSUMER_API, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    api.update_status(f"{sentence}")
