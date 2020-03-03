import uvicorn
from fastapi import FastAPI
from routers import login, index, test

app = FastAPI()

app.include_router(index.router)
app.include_router(login.router)

# for testing
app.include_router(test.router, prefix="/test")

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8081)