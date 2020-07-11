import json

filename = input("filename: ")

with open(filename, "r") as j:
    geojson = json.load(j)

    coords = geojson["coordinates"]
    rev_coords = []

    for coord in coords:
        rev_coords.append([coord[1], coord[0]])
    
    rev_geojson = {
        "type": "LineString",
        "coordinates": rev_coords
    }

    new_filename = filename + ".rev.geojson"

    with open(new_filename, "w") as nj:
        json.dump(rev_geojson, nj, indent=4)