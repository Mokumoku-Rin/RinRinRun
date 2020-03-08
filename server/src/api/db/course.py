import pymysql.cursors
from middlewares.database import get_db

def get_course_list_by_popular(limit: int):
  conn = get_db()
  with conn.cursor() as cursor:
    sql = "SELECT id, name, description FROM courses" + _build_order_by("played_count", limit)
    cursor.execute(sql)
    result = cursor.fetchall()
  return result

def get_course_list_by_latest(limit: int):
  conn = get_db()
  with conn.cursor() as cursor:
    sql = "SELECT id, name, description FROM courses" + _build_order_by("created_at", limit)
    cursor.execute(sql)
    result = cursor.fetchall()
  return result

def get_course_by_id(course_id: int):
  conn = get_db()
  with conn.cursor() as cursor:
    sql = "SELECT id, name, description, mean_distance, mean_time FROM courses WHERE id = %s"
    cursor.execute(sql, (course_id,))
    result = cursor.fetchone()
  return result


def _build_order_by(order: str, limit: int):
  return " ORDER BY %s limit %s" % (order, limit)
