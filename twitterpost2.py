import tweepy
from key import *

auth = tweepy.OAuthHandler(ckey,csecret)
auth.set_access_token(akey,asecret)

api = tweepy.API(auth)

api.update_with_media('C:\Python27/bk.jpg','coming with image')