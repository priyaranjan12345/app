from fastapi import FastAPI
from blog.routers import userRouter, blogRouter, authRouter, profile
from blog import models
from blog import database
import uvicorn

app = FastAPI()

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


