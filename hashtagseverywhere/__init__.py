import flask
from rq import Queue
from rq.job import Job
from worker import conn
from lib import *

app = flask.Flask(__name__)
q = Queue(connection = conn)

import hashtagseverywhere.routes