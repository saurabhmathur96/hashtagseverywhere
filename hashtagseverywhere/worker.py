
import os

import redis, rq

listen = ['default']



host = os.genenv('REDIS_HOST')
if host is None:
    redis_url = 'redis://localhost:6379'
    conn = redis.from_url(redis_url)
else :
    port = os.genenv('REDIS_PORT')
    password = os.genenv('REDIS_PASSWORD')
    conn = redis.Redis(host=host,port=port,password=password)

def main():
    with rq.Connection(conn):
        worker = rq.Worker([rq.Queue(each) for each in listen])
        worker.work()
    