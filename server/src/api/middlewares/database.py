from fastapi import FastAPI
from pymysql import Connection, err, cursors
import os

db: Connection = None

def get_db():
  return db

def setup(app: FastAPI):
  @app.on_event("startup")
  async def up_connection():
    cursor_type = cursors.DictCursor

    try:
      connection = Connection(
        host='mokumoku-mariadb',
        user=os.environ['DB_USER'],
        passwd=os.environ['DB_PASSWORD'],
        db='mokumoku',
        charset='utf8mb4',
        cursorclass=cursor_type)
      db = connection

    except err.DatabaseError as e:
      raise err.DatabaseError("Database connection failed:", str(e))
      db.close()

  @app.on_event("shutdown")
  async def down_connection():
    if db.open:
      db.close()
  
  return app
    



