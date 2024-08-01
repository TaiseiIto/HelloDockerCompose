import time
import redis # A database management system on memory.
from flask import Flask # A web application framework

app = Flask(__name__)
cache = redis.Redis(host = 'redis', port=6379) # Connect from the web container to the redis container in the port 6379.

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits') # https://redis.io/docs/latest/commands/incr/
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/') # Define a responce for a request to the root URL
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)

