from typing import Optional
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from database import *

#this is some sort of video storing app api

app = FastAPI()

class VideoInfo(BaseModel):
    title: str
    likes: int
    comments: Optional[int] = "null"

# The home route 
@app.get("/")
def index():
    return {"message": "You're on Ques"}


# get all videos in app
@app.get("/videos",status_code = status.HTTP_200_OK)
async def get_all_videos():
    status, values = get_all()
    return {'data':values}


# create a new video that is not already in the db
@app.post('/videos',status_code = status.HTTP_201_CREATED)
async def create_video(vi: VideoInfo):
    status  = inster_to_table( vi.dict() )
    if status != 201:
        raise HTTPException(status_code = status.HTTP_208_ALREADY_REPORTED,detail = 'The given video already exist' )
    else:
        return {'status': 'Created new video successfully'}



# get video info of a certain video provided its id
@app.get('/videos/{vid}',status_code = status.HTTP_200_OK)
async def video_info_on_id(vid : int):
    values = get_one_specific_data(vid)
    if values != 404:
        return {'data': values}
    elif values == 404:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail = f"a video with id {vid} was not found")




# updating the details of an existing video
@app.put('/videos/{vid}',status_code = status.HTTP_202_ACCEPTED)
async def update_video_details(vid : int, updation_info : VideoInfo):
    if find_video_with_id(vid):
        record = updation_info.dict()
        state = await update_video_info(vid,record)
    else:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail = f'Could not find a video with id = {vid}')

    if state == 202:
        return {vid:record}




# deleting a video that exists 
@app.delete('/videos/{vid}',status_code = status.HTTP_204_NO_CONTENT)
async def delete_video(vid: int):
    if find_video_with_id(vid):
        await delete_video(vid)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Found no video with id = {vid}')