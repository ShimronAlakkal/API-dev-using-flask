import string
from telnetlib import STATUS
from pydantic import BaseModel
from typing import Optional
from fastapi import FastAPI, HTTPException, status
from .database import *

app = FastAPI()

class Notes(BaseModel):
    title : string
    description : string

@app.get("/")
def index():
    return {'message':"you're at ques notes"}

# get user profile 
@app.get("/users/{uid}",status_code = status.HTTP_200_OK)
async def get_user_profile(uid :int):
    
    if user_exists(uid) : 
        return {'User':{uid:'info goes here'}}
        # get the user details from db and retunr it
    else:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"A user with id = {uid} could not be found")

