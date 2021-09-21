from fastapi import FastAPI
from . import  models
from .database import engine
from  .routers import blog, user, authentication

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router,
                    tags=["User"],)
app.include_router(blog.router,
                   prefix="/blog",
                   tags=["Blog"],)
app.include_router(user.router,
                        prefix="/user",
                        tags=["user"],)
