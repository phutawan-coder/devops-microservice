import redis
import json
import os
import time

redis_host = os.getenv("REDIS_HOST", "redis")
r = redis.Redis(host=redis_host,port=6379)

print("Worker started...")

while True:
    task = r.brpop("task_queue", timeout=5)
    if task:
        data = json.loads(task[1])
        print(f"Processing task: {data}")
        time.sleep(3)
        print("task completed")
