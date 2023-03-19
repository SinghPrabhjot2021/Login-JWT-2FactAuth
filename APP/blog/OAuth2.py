from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from blog.Routers import JWTtoken

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="Login")

def get_current_user(token: str = Depends(oauth2_scheme)):
   credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
   return JWTtoken.Verify_Token(token,credentials_exception)