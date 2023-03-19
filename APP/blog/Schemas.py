from pydantic import BaseModel 
from typing import List,Union
class Pydantic(BaseModel):
    Title:str
    Body:str   
    class Config():
       orm_mode = True 

class User(BaseModel):
    name:str
    email:str
    password:str
    # SecretKey=Key
    class Config():
       orm_mode = True  

class ShowUser(BaseModel):
    name:str
    email:str
    class Config():
       orm_mode = True     
class ShowPydantic(BaseModel):
    Title:str
    Body:str
    Creator:ShowUser
    class Config():
       orm_mode = True 
class Login(BaseModel):
    username:str
    password:str 


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None