SET @geojson = '
{
    "type": "LineString",
    "coordinates": [
        [1,2],
        [1,3],
        [1,4],
        [1,5],
        [1,6],
        [2,6],
        [3,6]
    ]
}';

INSERT INTO `workout_histories` (`user_id`, `cource_id`, `total_time`, `total_distance`, `geo_linestring`) VALUES ('1', '1', '560000', '5485', ST_GeomFromGeoJSON(@geojson));

SET @geojson = '
{
    "type": "LineString",
    "coordinates": [
        [2,2],
        [2,3],
        [2,4],
        [2,5],
        [4,6],
        [5,6],
        [1,6]
    ]
}';

INSERT INTO `workout_histories` (`user_id`, `cource_id`, `total_time`, `total_distance`, `geo_linestring`) VALUES ('2', '1', '520000', '2547', ST_GeomFromGeoJSON(@geojson));

SET @geojson = '
{
    "type": "LineString",
    "coordinates": [
        [1,4],
        [2,3],
        [1,5],
        [0,5],
        [1,2],
        [1,6],
        [3,3]
    ]
}';

INSERT INTO `workout_histories` (`user_id`, `cource_id`, `total_time`, `total_distance`, `geo_linestring`) VALUES ('3', '2', '430000', '6643', ST_GeomFromGeoJSON(@geojson));

SET @geojson = '
{
    "type": "LineString",
    "coordinates": [
        [1,0],
        [1,3],
        [1,4],
        [7,5],
        [1,3],
        [8,6],
        [3,1]
    ]
}';

INSERT INTO `workout_histories` (`user_id`, `cource_id`, `total_time`, `total_distance`, `geo_linestring`) VALUES ('4', '2', '980000', '6464', ST_GeomFromGeoJSON(@geojson));