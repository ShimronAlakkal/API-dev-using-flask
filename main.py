from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def index():
    return {'message':"you're at ques notes"}