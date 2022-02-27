from fastapi import status, APIRouter, UploadFile, File, Form, Depends, HTTPException
from fastapi.responses import FileResponse
from typing import List
import shutil, glob

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

@approute.get('/downloadFile')
def getAllFiles():
    return FileResponse(path='files/one.png', filename='one.png', media_type='application/octet-stream')

@approute.get('/allFineNames')
def allFilesName():
    txtfiles = []
    for file in glob.glob("files/*.*"):
        txtfiles.append(file)
    return {'files': txtfiles}

@approute.post('/userData')
def userData(name: str = Form(...), dob: str = Form(...),file: UploadFile = File(...)):
    return {'name': name, 'file': file.filename, 'dob': dob}



# try:
    
# except JWTError: