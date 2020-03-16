import firebase_admin
from firebase_admin import App

firebase_app: App

def get_app():
  global firebase_app
  return firebase_app

def setup():
  BUCKET_NAME = "rinrinrun-ad626.appspot.com"
  global firebase_app
  firebase_app = firebase_admin.initialize_app(options={
    "storageBucket": BUCKET_NAME
  })