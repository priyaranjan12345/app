from pydantic import BaseModel
from typing import List, Optional, Union
from fastapi import Query


# blog 
# request json type
class Blog(BaseModel):
    title: str
    body: str
    
# response json type
class ShowBlogs(BaseModel): 
    title: str
    body: str
    
    class Config:
        orm_mode = True
        
"""
if we required all the field as our model use model_name instead BaseModel
e.g.- 
class ShowBlogs(Blog): 
   pass
    
    class Config:
        orm_mode = True
"""
        
# user       
# request json type
class User(BaseModel):
    name: str
    email: Union[str, None] = Query(default=None, regex="^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$")
    password: str
    
# response json type
class ShowUser(BaseModel):
    name: str
    email: str
    
    class Config:
        orm_mode = True
        
class ShowBlogWithUser(BaseModel):
    title: str
    body: str
    bloger: ShowUser
    
    class Config:
        orm_mode = True
        
class ShowUserWithBlogs(BaseModel):
    name: str
    email: str
    blogs: List[ShowBlogs] = []
    
    class Config:
        orm_mode = True
        
        
# login request json type
class Login(BaseModel):
    username: str
    password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    email: Optional[str] = None
    userId: Optional[int] = None