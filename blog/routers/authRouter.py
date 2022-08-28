from fastapi import APIRouter, Depends, HTTPException, status
from blog.database import get_db
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from blog import models, schemas, JWTtoken
from blog.hashing import Hash

approute = APIRouter(tags=['Authentication'])

@approute.post('/loginJWT')
def login(request:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials")
    
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect password")

    access_token = JWTtoken.create_access_token(data={"sub": user.email, "userId": user.id})
    return {"access_token": access_token, "token_type": "bearer"}


@approute.post('/loginSimple', status_code = status.HTTP_200_OK)
def simplelogin(request:schemas.Login, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
        
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials")
        
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect password")
            
    return user;