import os

from fastapi import FastAPI
from pymysql import Connection, cursors, err

db: Connection


def get_db():
    global db
    # reconnect when connection is closed
    db.ping(reconnect=True)
    return db


def setup(app: FastAPI):
    @app.on_event("startup")
    async def up_connection():
        global db
        cursor_type = cursors.DictCursor

        try:
            connection = Connection(
                host=os.environ['DB_HOST'],
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
        global db
        if db.open:
            db.close()

    return app


def execute_fetchone(sql, args=None):
    conn = get_db()
    with conn.cursor() as cursor:
        cursor.execute(sql, args)
        result = cursor.fetchone()
    return result


def execute_fetchall(sql, args=None):
    conn = get_db()
    with conn.cursor() as cursor:
        cursor.execute(sql, args)
        result = cursor.fetchall()
    return result


def execute_commit(sql, args):
    conn = get_db()
    with conn.cursor() as cursor:
        cursor.execute(sql, args)
    conn.commit()
