import flask
from lib import tweet
from hashtagseverywhere import app, q
from rq.job import Job
from worker import conn


@app.route('/', methods=['get'])
def index():
    return flask.render_template('index.html')

@app.route('/api/v1/tweets', methods=['get'])
def request_tweets():
    topic = flask.request.args.get('topic')
    job = q.enqueue_call(
        func = tweet.search, args=(topic,), result_ttl=5000
    )
    
    return flask.jsonify(jobid=job.get_id())
    
@app.route('/api/v1/results/<job_key>', methods=['get'])
def get_results(job_key):

    job = Job.fetch(job_key, connection=conn)

    if job.is_finished:
        return flask.jsonify(result=job.result)
    else:
        return ('Nay!', 202)