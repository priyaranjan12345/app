from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from sqlalchemy.orm import Session
from blog import models, schemas
from blog.hashing import Hash

def create(user: schemas.User, db: Session):
    try:
        new_user = models.User(name=user.name, email=user.email, password= Hash.dcrypt(user.password))
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        
        return new_user
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_NOT_FOUND, detail=f"email id already exist")

def all(db: Session):
    allusers = db.query(models.User).all()
    
    return allusers;

def showUserBlogs(id:int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with {id} not found")
    
    return user

def deleteUser(id:int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with {id} not found")
    
    try:
        db.delete(user) 
        db.commit()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"user not deleted")
    return Response(status_code=status.HTTP_204_NO_CONTENT)