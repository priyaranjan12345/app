from fastapi import APIRouter, Depends, status
from blog.database import get_db
from sqlalchemy.orm import Session
from typing import List
from blog import schemas
from blog.repository import userRepository
from blog import schemas, oAuth2

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

@approute.get("/currentUser", status_code= status.HTTP_200_OK)
def showUserBlogs(current_user: schemas.User = Depends(oAuth2.get_current_user)):
    
    return {'email': current_user.email}

@approute.delete("/currentUser/{id}", status_code= status.HTTP_204_NO_CONTENT)
def deleteUser(id: int, db: Session = Depends(get_db)):
    
    return userRepository.deleteUser(id, db)