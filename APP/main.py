import uvicorn
from blog import DB_model
from blog.Database import engine 
from fastapi import  FastAPI
from blog.Routers import Blog,user,Login
from blog import TwoFactorAuth

app=FastAPI(title='MyFirstApp')
DB_model.Base.metadata.create_all(engine)
app.include_router(user.Router)
app.include_router(Login.Login)
app.include_router(Blog.Router)





if __name__=='__main__':
    uvicorn.run(app)
    
    