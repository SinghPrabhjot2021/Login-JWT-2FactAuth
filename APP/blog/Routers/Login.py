from fastapi import APIRouter,Depends,HTTPException,status
from blog import DB_model
from fastapi.security import OAuth2PasswordRequestForm
from blog.Database import get_db
from sqlalchemy.orm import Session
from datetime import timedelta
from blog.Hashing import Hash
from .JWTtoken import create_access_token,ACCESS_TOKEN_EXPIRE_MINUTES
import pyotp

Router=APIRouter(
    tags=['Authentication']
)


#@Router.post('/Login')
def Login(request:OAuth2PasswordRequestForm=Depends() ,DB:Session=Depends(get_db),):
    User= DB.query(DB_model.User).filter(DB_model.User.email==request.username).first()
    
    if not User:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= f"Invalid Username")
    if not Hash.Verify(User.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= f"Invalid Password")
    totp = pyotp.TOTP(User.SecretKey)
    if not totp.verify(request.password[-6:]):
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= f"Invalid OTP")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": User.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}