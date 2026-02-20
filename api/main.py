from fastapi import FastAPI
import redis
import os
import json

app = FastAPI()

redis_host = os.getenv("REDIS_HOST","redis")
r = redis.Redis(host=redis_host, port=6379)

@app.get('/')
def index():
    return {"message": "API running"}

@app.get('/health')
def health():
    return {"status": "ok"}

@app.post('/task')
def task(data: dict):
    r.lpush("task_queue", json.dumps(data))
    return {"status": "task queue"}
