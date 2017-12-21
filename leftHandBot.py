from credentials import *
import tweepy
from time import sleep
import pprint

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
leftHand = {"q","w","e","r","t","a","s","d","f","g","z","x","c","v","b"," ","1","2","3","4","5","!","@","#","$","%"}
for tweet in tweepy.Cursor(api.search,q='#Rockets').items():
    try:
        onlyLeft = True
        for letters in tweet.text:
            print(letters)
            if letters.lower() not in leftHand:
                print("not in set")
                onlyLeft = False
                break
        print(onlyLeft)
        if onlyLeft == True:
            tweet.retweet()
            print(tweet.user.screen_name + ' only used their left hand to type : ' + tweet.text)
        sleep(5)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break
