from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


origins = [
  "http://localhost:8080",
  "https://localhost:8080",
  "https://develop.hiragi.guru:7370",
  "https://kakemori-vue.azurewebsites.net",
]

def setup(app: FastAPI):
  app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
  )

  return app
