
import os

import redis, rq

listen = ['default']



host = os.getenv('REDIS_HOST')
if host is None:
    redis_url = 'redis://localhost:6379'
    conn = redis.from_url(redis_url)
else :
    port = os.getenv('REDIS_PORT')
    password = os.getenv('REDIS_PASSWORD')
    conn = redis.Redis(host=host,port=port,password=password)

def main():
    with rq.Connection(conn):
        worker = rq.Worker([rq.Queue(each) for each in listen])
        worker.work()
    