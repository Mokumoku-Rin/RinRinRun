import db.workout
import json


def get_today_record(uid, date):
    today_workout_history = []
    for i in db.workout.get_today_record(uid, date):
        i['geo_json'] = json.loads(i.pop('ST_AsGeoJSON(geo_linestring)'))
        today_workout_history.append(i)
    return today_workout_history
