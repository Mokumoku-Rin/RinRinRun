from enum import Enum, auto
from middlewares.database import get_db


def build_update_sql(obj: dict, table: TABLE, wheres: str):
  sets = []
  for c, v in obj.items():
    if v == None:
      continue
    sets.append(" ".join([c, "=", v, ","]))
  sets[-1].replace(",", "")

  sql = "".join(["UPDATE", table.value, "SET"] + sets) + wheres

  
def exec(sql: str):
  conn = get_db()
  with conn.cursor() as c:
    c.execute(sql)


class TABLE(Enum):
  USERS = "users"
  WORKOUTS = "workout_history"
  LANDMARKS = "landmarks"
  LAND_VISITS = "landmark_visits"
