import time
import threading
import queue

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title="Task for Elastoo")
q = queue.Queue()


class TaskInput(BaseModel):
	num: int
	timeout: float

class TaskOutput(BaseModel):
	position: int


def worker():
	while True:
		item = q.get()
		print(f'Working on {item.num}')
		time.sleep(item.timeout)
		print(f'Finished {item.num}')
		q.task_done()

threading.Thread(target=worker, daemon=True).start()


@app.post(
	"/tasks",
	response_description="Task added to the queue",
	response_model=TaskOutput,
)
async def add(task: TaskInput):
	position = q.qsize()
	q.put(task)
	return {"position": position}