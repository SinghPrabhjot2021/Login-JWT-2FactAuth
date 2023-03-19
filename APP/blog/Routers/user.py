from fastapi import APIRouter
from blog import Schemas,OAuth2
from blog.Database import get_db
from fastapi import Depends,status
from sqlalchemy.orm import Session
from blog.repository import UserFunctions

Router=APIRouter(
      
      prefix='/User',
      tags=['Users']
)


# Function to create user DB and store uer information

@Router.post('/SignUP',status_code=status.HTTP_201_CREATED,response_model=Schemas.ShowUser)
def User(request: Schemas.User,DB:Session=Depends(get_db)):
       return UserFunctions.CreateUser(DB,request)
    

#Function to fetch user details with id
@Router.get('/{id}',status_code=status.HTTP_302_FOUND,response_model=Schemas.ShowUser)
def UserId(id,DB:Session=Depends(get_db)):
    return UserFunctions.Get_UserID(id,DB)
