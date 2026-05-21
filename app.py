from flask import Flask
import redis
import os
import socket

app = Flask(__name__)

redis_host = os.getenv("REDIS_HOST")
redis_port = os.getenv("REDIS_PORT")

r = redis.Redis(host=redis_host, port=redis_port)

hostname = socket.gethostname()

@app.route('/')
def home():
    r.incr('counter')
    count = r.get('counter').decode('utf-8')
    return f"Container: {hostname} | Visits: {count}"

app.run(host='0.0.0.0', port=5000)
