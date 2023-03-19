from sqlalchemy.orm import Session
from blog import DB_model,Schemas
from fastapi import HTTPException,status

def get_all(DB:Session):
     fetch=DB.query(DB_model.Blog).all() 
     return fetch 

def Create(request:Schemas.Pydantic,DB:Session):
    new_blog=DB_model.Blog(Title=request.Title,Body=request.Body,DB_ID=1)
    DB.add(new_blog)
    DB.commit()
    DB.refresh(new_blog)
    #response_blog=Schemas.ShowPydantic(Title=new_blog.Title,Body=new_blog.Body,)
    return new_blog
def Delete(id:int,DB:Session):
    Delete=DB.query(DB_model.Blog).filter(DB_model.Blog.UserID == id)
    if not Delete.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog {id} not found") 
    else:
        Delete.delete(synchronize_session=False)
        DB.commit()
        return f"Record with ID:{id} Deleted"
def Update(id:int,DB:Session,request:Schemas.Pydantic):
    update=DB.query(DB_model.Blog).filter(DB_model.Blog.UserID == id)
    if not update.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog {id} not found") 
    else: 
        update.update({'Title':request.Title,'Body':request.Body},synchronize_session=False)
        DB.commit()
        return f"Record with ID: {id} Updated"

def Get_ID(id:int,DB:Session):
    showID=DB.query(DB_model.Blog).filter(DB_model.Blog.UserID == id).first()
    if not showID:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= f"Blog ID:{id} is not Available")
    return showID    