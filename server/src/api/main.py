import uvicorn
from fastapi import FastAPI, Depends
from routers import login, session
from middlewares import cors, database
from depends import auth
import firebase_admin

app = FastAPI()

app = cors.setup(app)
app = database.setup(app)


app.include_router(
  login.router,
  prefix="/login",
)

app.include_router(
  session.router,
  prefix="/session",
  dependencies=[Depends(auth.verify_firebase_token, use_cache=False)]
)

if __name__ == "__main__":
  default_app = firebase_admin.initialize_app()
  uvicorn.run(app, host="0.0.0.0", port=8081)