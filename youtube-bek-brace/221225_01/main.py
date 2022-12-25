# https://www.youtube.com/watch?v=eedaafutru4&ab_channel=BekBrace
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def example():
    return {"message":"Hello World, from FastAPI"}

@app.get("/greetings")
def greetings():
    return {"message":"Hello World, from greetings endpoint"}

if __name__ == "__main__":
    uvicorn.run("main:app")