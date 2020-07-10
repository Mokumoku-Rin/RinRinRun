import os
import uvicorn
from fastapi import FastAPI, Depends
from routers import login, session
from middlewares import cors, database, firebase
from depends.auth import FirebaseToken

app = FastAPI()

app = cors.setup(app)
app = database.setup(app)
firebase.setup()

app.include_router(
    login.router,
    prefix="/login",
)

app.include_router(
    session.router,
    prefix="/session",
    dependencies=[Depends(FirebaseToken, use_cache=False)]
)

if __name__ == "__main__":
    print("Firebase Admin:", firebase.get_app().name, "is running")
    server_host = os.environ["SERVER_HOST"]
    server_port = os.environ["SERVER_ROOT"]
    print("host:" + str(server_host))
    print("port:" + str(server_port))
    uvicorn.run(app, host=os.environ["SERVER_HOST"], port=os.environ["SERVER_PORT"])
