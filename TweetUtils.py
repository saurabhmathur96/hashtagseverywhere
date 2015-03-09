import twitter


def do_Oauth():
  with open('config') as f:
    OAUTH_TOKEN = f.readline().strip()
    OAUTH_TOKEN_SECRET = f.readline().strip()
    CONSUMER_KEY = f.readline().strip()
    CONSUMER_KEY_SECRET = f.readline().strip()
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                             CONSUMER_KEY, CONSUMER_KEY_SECRET)

  twitter_api = twitter.Twitter(auth=auth)
  return twitter_api

def get_tweets(q, count):
  ''' Use the twitter api get @count tweets on topic @q '''
  twitter_api = do_Oauth() 
  print twitter_api
  
  response = twitter_api.search.tweets(q=q, count=count)
  
  return response['statuses']
  

def format_tweets(tweets):  
  ''' return a list of tweets with each element of form {hashtag: count} '''
  print tweets


def lexical_diversity_percent(tokens):
  ''' calculate percent lexical diversity: a measure of uniqueness of words '''
  return 100.0*len(set(tokens))/len(tokens) 

def average_words(statuses):
  ''' return average number of words used'''
  total_words = sum([ len(s.split()) for s in statuses ]) 
  return 1.0*total_words/len(statuses)
  
def get_hashtags(tweets):
  ''' return a list of hashtags from tweets '''
  return [ hashtag['text'] 
             for tweet in tweets
                 for hashtag in tweet['entities']['hashtags'] ]
                 
def get_tweet_texts(tweets):
  ''' '''
  return [ tweet['text'] 
                 for tweet in tweets ]
                
def get_words(tweet_texts):
  ''' '''
  return [ w 
          for t in tweet_texts 
              for w in t.split() ]
