from blog import DB_model,Schemas
from blog.Hashing import Hash
from fastapi import status,HTTPException
from blog.Database import engine ,SessionLocal ,get_db
from sqlalchemy.orm import Session
from blog.TwoFactorAuth import Key
def CreateUser(DB:Session,request:Schemas.User):
    
    new_User=DB_model.User(name=request.name,email=request.email,password=Hash.Crypt(request.password),SecretKey=Key)
    DB.add(new_User)
    DB.commit()
    DB.refresh(new_User)
    return new_User
def Get_UserID(id:int,DB:Session,):
    showID=DB.query(DB_model.User).filter(DB_model.User.UserID == id).first()
    if not showID:
             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= f"User ID:{id} is not Available")
    return showID