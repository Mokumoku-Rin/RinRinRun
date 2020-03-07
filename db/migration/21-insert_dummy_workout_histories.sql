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

SET @time_list = '5000,10000,15000,20000,25000,30000,35000,40000,45000,50000,55000,60000';

INSERT INTO `workout_histories` (`user_id`, `course_id`, `total_time`, `total_distance`, `time_list`, `geo_linestring`) VALUES ('1', '1', '710000', '5485',@time_list, ST_GeomFromGeoJSON(@geojson));

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

INSERT INTO `workout_histories` (`user_id`, `course_id`, `total_time`, `total_distance`, `time_list`, `geo_linestring`) VALUES ('2', '1', '730000', '2547',@time_list,ST_GeomFromGeoJSON(@geojson));

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

INSERT INTO `workout_histories` (`user_id`, `course_id`, `total_time`, `total_distance`, `time_list`,  `geo_linestring`) VALUES ('3', '2', '620000', '6643',@time_list, ST_GeomFromGeoJSON(@geojson));

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

INSERT INTO `workout_histories` (`user_id`, `course_id`, `total_time`, `total_distance`, `time_list`, `geo_linestring`) VALUES ('4', '2', '66000', '6464',@time_list, ST_GeomFromGeoJSON(@geojson));