from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from blog import models, schemas

def create(blog: schemas.Blog, db: Session):
    new_blog = models.Blog(title=blog.title, body=blog.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    
    return new_blog

def all(db: Session):
    blogs = db.query(models.Blog).all()
    
    return blogs

def get(id: int, db:Session):
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
    
    if blogs is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with {id} not found")
    
    return blogs

def getWithUser(id: int, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if blog is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with {id} not found")
    
    return blog

def update(id: int, newblog: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    
    if blog.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with {id} not found")
    
    blog.update(newblog.dict())
    db.commit()
    
    return {"detail": f"Blog {id} updated"}

def delete(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    
    if blog.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with {id} not found") 
    
    blog.delete(synchronize_session = False) 
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)