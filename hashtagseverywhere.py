from flask import Flask, render_template, redirect, request, make_response
from collections import Counter
import json
from functools import wraps, update_wrapper
from datetime import datetime
from TweetUtils import get_tweets, format_tweets, lexical_diversity_percent, average_words, \
                        get_hashtags, get_words, get_tweet_texts

COUNT = 200

app = Flask(__name__)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

@app.route('/')
def hello_world():
  return render_template('index.html')

@app.route('/htags', methods = ['POST'])
def htags():
  topic = request.form['topic']
  print ('Topic: {}'.format(topic))
  tweets = get_tweets(q=topic, count=COUNT)
  hashtags = get_hashtags(tweets) 
  tweet_texts = get_tweet_texts(tweets) 
  print (hashtags)
  c = Counter(hashtags).most_common(20)
  print (dict(c))
  d = [{"Hashtag": key, "Frequency":value} for key, value in dict(c).iteritems()]
  print json.dumps(d)
  
  with open('static/data.json', 'w') as outfile:
    json.dump(d, outfile)
  
  words = get_words(tweet_texts)
  diversity = lexical_diversity_percent(words)
  avg_words = average_words(tweet_texts)
  print ('lexical diversity: {}%'.format(diversity))
  print ('Average length: {} words'.format(avg_words))
  
  
  #return redirect('/') 
  return render_template('htags.html', d=d, diversity=diversity, avg_words=avg_words)

if __name__ == '__main__':
  app.run(debug=True)
