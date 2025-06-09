import time

import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        # Se non riesce a connettersi (es. Redis non è ancora pronto)
        # Riprova 5 volte e aspetta 0.5 secondi prima di riprovare ogni volta
        try:
            # incr('hits') → se la chiave non esiste, Redis la inizializza a 0 e poi la incrementa a 1
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)
    # return 'Hello from Docker! I have been seen {} times.\n'.format(count)