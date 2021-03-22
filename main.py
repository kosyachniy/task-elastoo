from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title="Task for Elastoo")


class TaskInput(BaseModel):
	num: int
	timeout: float

class TaskOutput(BaseModel):
	position: int


@app.post(
	"/tasks",
	response_description="Task added to the queue",
	response_model=TaskOutput,
)
async def add(task: TaskInput):
	return {"position": 1}