import uvicorn
from fastapi import FastAPI
from routers import login, session
from middlewares import cors
from depends import auth
import firebase_admin

app = FastAPI()

app = cors.setup(app)


app.include_router(
  login.router,
  prefix="/login",
)

app.include_router(
  session.router,
  prefix="/session",
  dependencies=auth.verify_firebase_token
)

if __name__ == "__main__":
  default_app = firebase_admin.initialize_app()
  uvicorn.run(app, host="0.0.0.0", port=8081)