import time
import threading
import queue

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title="Task for Elastoo")
queue_in = queue.Queue()
queue_out = queue.Queue()


class TaskInput(BaseModel):
	num: int
	timeout: float

class TaskOutput(BaseModel):
	position: int

class ResultOutput(BaseModel):
	result: list[int]


def worker():
	while True:
		if not queue_in.qsize():
			continue

		item = queue_in.queue[0]
		print(f'Working on {item.num}')
		time.sleep(item.timeout)
		print(f'Finished {item.num}')

		queue_out.put(item.num)
		queue_in.get()
		queue_in.task_done()

threading.Thread(target=worker, daemon=True).start()


@app.post(
	"/tasks",
	response_description="Task added to the queue",
	response_model=TaskOutput,
)
async def add(task: TaskInput):
	queue_in.put(task)
	return {"position": queue_in.qsize()}

@app.get(
	"/results",
	response_description="Results",
	response_model=ResultOutput,
)
async def result():
	return {"result": queue_out.queue}