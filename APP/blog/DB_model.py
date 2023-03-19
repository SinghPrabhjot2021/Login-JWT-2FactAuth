from blog.Database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
class Blog(Base):
    __tablename__="Blog"
    UserID=Column(Integer,primary_key=True,index=True)
    Title=Column(String)
    Body=Column(String)
    DB_ID=Column(Integer,ForeignKey('User.UserID'))
    Creator=relationship("User",back_populates="blogs")
class User(Base):
    __tablename__='User'
    UserID=Column(Integer,primary_key=True,index=True)
    name=Column(String)    
    email=Column(String) 
    password=Column(String)
    SecretKey=Column(String)
    blogs=relationship("Blog",back_populates="Creator") 
