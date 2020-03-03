import uvicorn
from fastapi import FastAPI
from routers import login, index

app = FastAPI()

app.include_router(index.router)
app.include_router(login.router)

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8081)