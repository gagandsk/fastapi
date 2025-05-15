from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {"name": "Hello World from Python"}