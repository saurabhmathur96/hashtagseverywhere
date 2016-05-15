import os, twitter
from collections import Counter

COUNT=os.getenv('TWEET_COUNT', 128)

class Twitter(object):
    twitterapi = None
    
    @staticmethod   
    def perform_oauth():
        OAUTH_TOKEN = os.environ.get('T_OAUTH_TOKEN') 
        OAUTH_TOKEN_SECRET = os.environ.get('T_OAUTH_TOKEN_SECRET')
        CONSUMER_KEY = os.environ.get('T_CONSUMER_KEY')
        CONSUMER_KEY_SECRET = os.environ.get('T_CONSUMER_KEY_SECRET')
        auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_KEY_SECRET)
        return auth
    
    @staticmethod
    def get_api():
        if Twitter.twitterapi is None:
            Twitter.twitterapi = twitter.Twitter(auth=Twitter.perform_oauth())
        return Twitter.twitterapi

def search(topic):
    twitterapi = Twitter.get_api()
    statuses = twitterapi.search.tweets(q=topic, count=COUNT)['statuses']
    allhashtags = (tag['text'] for status in statuses for tag in status['entities']['hashtags'])
    counts = [{'hashtag': tag, 'frequency': count} for tag, count in Counter(allhashtags).items()]
    print counts
    return counts

