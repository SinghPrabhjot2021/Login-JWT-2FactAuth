from fastapi import APIRouter
from typing import List
from blog import Schemas,OAuth2
from blog.Database import engine ,SessionLocal ,get_db
from fastapi import Depends, HTTPException,status,Response
from sqlalchemy.orm import Session
from blog.repository import BlogFunctions

Router=APIRouter(

    prefix="/Blog",
    tags=['Blogs']
)


#to fetch  data from database
@Router.get('/',response_model=List[Schemas.ShowPydantic])
def ALL(DB:Session=Depends(get_db),Current_User:Schemas.User= Depends(OAuth2.get_current_user)):
   return BlogFunctions.get_all(DB)

# function to create and add data to database---------------
@Router.post('/')
def Create(request: Schemas.Pydantic,DB:Session=Depends(get_db),Current_User:Schemas.User= Depends(OAuth2.get_current_user)):
   return BlogFunctions.Create(request,DB)

#Function to delete record from database
@Router.delete('/{id}')
def Delete(id,DB:Session=Depends(get_db),Current_User:Schemas.User= Depends(OAuth2.get_current_user)):
    return BlogFunctions.Delete(id,DB)

#Function to Update the record in database
@Router.put('/{id}')
def Update(id,request:Schemas.Pydantic,DB:Session=Depends(get_db),Current_User:Schemas.User= Depends(OAuth2.get_current_user)):
    return BlogFunctions.Update(id,DB,request)


#Function to fetch record of particular ID from the database
@Router.get('/{id}',status_code=status.HTTP_302_FOUND,response_model=Schemas.ShowPydantic)
def Getid(id,response:Response,DB:Session=Depends(get_db),Current_User:Schemas.User= Depends(OAuth2.get_current_user)):
    return BlogFunctions.Get_ID(id,DB)
