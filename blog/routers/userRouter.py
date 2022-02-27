from fastapi import APIRouter, Depends, HTTPException, status, Response
from blog.database import get_db
from sqlalchemy.orm import Session
from typing import List
from blog import schemas
from blog.repository import userRepository

approute = APIRouter(
    prefix='/user',
    tags=['User']
)

@approute.post("/create", status_code = status.HTTP_201_CREATED)
def createUser(user: schemas.User, db: Session = Depends(get_db)):
   
    return userRepository.create(user, db)

@approute.get("/all", status_code = status.HTTP_200_OK, response_model= List[schemas.ShowUser])
def getAllUser(db: Session = Depends(get_db)):
    
    return userRepository.all(db)

@approute.get("/showUserWithBlogs/{id}", status_code= status.HTTP_200_OK, response_model= schemas.ShowUserWithBlogs)
def showUserBlogs(id:int, db: Session = Depends(get_db)):
       
    return userRepository.showUserBlogs(id, db)

