from urllib import response
import tweepy

from twitter_keys import ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, twitter_secrets as ts
from days_calculator import calculator

# Assigns the keys from another file. 
BEARER = ts.BEARER_TOKEN
CONSUMER_KEY = ts.CONSUMER_KEY
CONSUMER_SECRET = ts.CONSUMER_SECRET
ACCESS_KEY = ts.ACCESS_KEY
ACCESS_SECRET = ts.ACCESS_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

client = tweepy.Client(bearer_token=BEARER, consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, access_token=ACCESS_KEY, access_token_secret=ACCESS_SECRET)

days_until = calculator()
day_text = "Quedan %s días para el concierto de #BadBunny en Orlando, FL. Te amo BIBR <3" %str(days_until)
client.create_tweet(text=day_text)

