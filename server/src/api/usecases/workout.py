from db.workout import insert_workout_history


def add_workout_history(uid, cource_id, geometry_track, time):
    insert_workout_history(uid, cource_id, geometry_track, time)
