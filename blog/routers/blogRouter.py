from fastapi import APIRouter, Depends, status, Response
from blog.database import get_db
from sqlalchemy.orm import Session
from blog.repository import blogRepository
from blog import schemas, oAuth2

approute = APIRouter(
    prefix = "/blog",
    tags = ["Blog"]
)

@approute.post("/", status_code = status.HTTP_201_CREATED, )
def createBlogs(blog: schemas.Blog, db: Session = Depends(get_db)):
    return blogRepository.create(blog, db)

@approute.get("/allBlogs")
def allBlogs(db: Session = Depends(get_db), current_user: schemas.User = Depends(oAuth2.get_current_user)):
    return blogRepository.all(db)

@approute.get("/{id}", status_code= status.HTTP_200_OK, response_model= schemas.ShowBlogs)
def getBlog(id:int, response: Response, db: Session = Depends(get_db)):
    
    return blogRepository.get(id, db)

@approute.get("/blogWithBloger/{id}", status_code= status.HTTP_200_OK, response_model= schemas.ShowBlogWithUser)
def blogWIthVloger(id: int, db: Session = Depends(get_db)):
    
    return blogRepository.getWithUser(id, db)

@approute.put("/updateBlogs/{id}", status_code= status.HTTP_202_ACCEPTED)
def updateBlog(id: int, newblog: schemas.Blog, db: Session = Depends(get_db)):
        
    return blogRepository.update(id, newblog, db)

@approute.delete("/delete/{id}" , status_code = status.HTTP_204_NO_CONTENT)
def deleteBlog(id: int, db: Session = Depends(get_db)):
        
    return blogRepository.delete(id, db)
