import json

with open("31-workout_histories.sql", "r") as f:
    raw = f.read()

    splited = raw.split("'")

    i = 0
    jsons_raw = []
    jsons_raw.append(splited[1])
    jsons_raw.append(splited[15])
    jsons_raw.append(splited[29])

    jsons = []
    for jw in jsons_raw:
        jw = jw.rstrip("}")
        j = json.loads(jw)
        
        coord = j["coordinates"]
        new_coord = []
        for c in coord:
            new_coord.append([c[1], c[0]])
        jsons.append({
            "type": "LineString",
            "coordinates": new_coord
        })
    
    for j in jsons:
        print(json.dumps(j, indent=4))
