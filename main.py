from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from blog.routers import userRouter, blogRouter, authRouter, profile
from blog import models
from blog import database
import uvicorn

app = FastAPI()

origins = [
    "https://app-demo-banty.herokuapp.com",
    "http://app-demo-banty.herokuapp.com",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def homeView():
    return 'This is initial page'

models.base.metadata.create_all(database.engine)

app.include_router(profile.approute)
app.include_router(authRouter.approute)
app.include_router(blogRouter.approute)
app.include_router(userRouter.approute) #prefix="/user", tags=["User"] we can add this here also


# if __name__ == "__main__":
#     uvicorn.run(app, host="localhost", port=8000)


