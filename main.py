import time
import threading
import queue
import typing

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title="Elastoo task")
queue_in = queue.Queue()
queue_out = queue.Queue()


class TaskInput(BaseModel):
	num: int
	timeout: float

class TaskOutput(BaseModel):
	position: int

class ResultOutput(BaseModel):
	result: list[int]

class ExampleItem(typing.TypedDict):
	id: int
	time: float
	num: int
	timeout: float

class QueueOutput(BaseModel):
	result: list[dict] = [ExampleItem(
		id=1, time=1616450789.260913, num=5, timeout=0.5,
	)]


def worker():
	while True:
		if not queue_in.qsize():
			continue

		item = queue_in.queue[0]
		print('Working on {} (ID {})'.format(item['num'], item['id']))
		time.sleep(item['timeout'])
		print('Finished {} (ID {})'.format(item['num'], item['id']))

		queue_out.put(item['num'])
		queue_in.get()
		queue_in.task_done()

threading.Thread(target=worker, daemon=True).start()


@app.post(
	"/tasks",
	response_description="Task added to the queue",
	response_model=TaskOutput,
)
async def add(task: TaskInput):
	history_position = queue_out.qsize()
	position = queue_in.qsize()+1

	item = {
		'id': history_position+position,
		'time': time.time(),
		'num': task.num,
		'timeout': task.timeout,
	}

	queue_in.put(item)

	return {"position": position}

@app.get(
	"/results",
	response_description="Results",
	response_model=ResultOutput,
)
async def result():
	return {"result": queue_out.queue}

@app.get(
	"/tasks",
	response_description="Current task queue",
	response_model=QueueOutput,
)
async def get():
	return {"result": queue_in.queue}