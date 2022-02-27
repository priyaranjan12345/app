from fastapi import status, APIRouter, UploadFile, File, Form, Depends, HTTPException
from typing import List
import shutil

approute = APIRouter(tags=["Profile"])

@approute.post('/profile', status_code=status.HTTP_201_CREATED,)
async def uploadProfileData(file: UploadFile = File(...)):
    
    file_location = f"files/{file.filename}"
    with open(file_location, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    return {'status': status.HTTP_201_CREATED, 'message': 'Profile data uploaded successfully'}


@approute.post('/uploadMultipleFiles', status_code=status.HTTP_201_CREATED,)
async def uploadFiles(files: List[UploadFile] = File(...)):
    for file in files:
        file_location = f"files/{file.filename}"
        with open(file_location, 'wb') as buffer:
            shutil.copyfileobj(file.file, buffer)
        
    return {'status': status.HTTP_201_CREATED, 'message': 'Profile data uploaded successfully'}



# try:
    
# except JWTError: