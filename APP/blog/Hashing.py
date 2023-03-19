from passlib.context import CryptContext

PWD_CRYPT=CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def Crypt(password:str):
        return PWD_CRYPT.hash(password)
    def Verify(hashed_password,plain_password):
        return PWD_CRYPT.verify(plain_password[:-6],hashed_password)