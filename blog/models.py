from multiprocessing.reduction import duplicate
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from blog.database import base

class Blog(base):
    __tablename__ = 'Blogs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('Users.id'))
    
    bloger = relationship('User', back_populates='blogs')
    
    
class User(base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String)
    
    blogs = relationship('Blog', back_populates='bloger')
