import json

filename = input("filename: ")


with open(filename, "r") as j:
    geojson = json.load(j)
    coords = geojson["coordinates"]

    interval = 5000
    for i in range(len(coords)):
        t = i * interval
        print(t, end=",")
