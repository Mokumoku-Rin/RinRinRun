SET @json = '{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {
        "name": "B",
        "imageUrl": "https://www.hoge.com/img.png",
        "description": "たのしい"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          135.57448625564575,
          34.877226506346105
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "name": "A",
        "imageUrl": "https://www.hoge.com/img.png",
        "description": "すごい"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          135.57664275169373,
          34.87784262403066
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "name": "B",
        "imageUrl": "https://www.hoge.com/img.png",
        "description": "うつくしい"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          135.5750012397766,
          34.87820349081563
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "name": "L",
        "imageUrl": "https://www.hoge.com/img.png",
        "description": "かなしい"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          135.57620286941525,
          34.875334116012404
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "name": "N",
        "imageUrl": "https://www.hoge.com/img.png",
        "description": "つらい"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          135.57844519615173,
          34.87509646391483
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "name": "C",
        "imageUrl": "https://www.hoge.com/img.png",
        "description": "おはよう"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          135.57846665382385,
          34.873661734806596
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "name": "P",
        "imageUrl": "https://www.hoge.com/img.png",
        "description": "こんばんわ"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          135.57785511016846,
          34.878009855176764
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "name": "GG",
        "imageUrl": "https://www.hoge.com/img.png",
        "description": "さよなら"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          135.57576298713684,
          34.876601582262936
        ]
      }
    }
  ]
}';

INSERT INTO `cources` (`name`, `landmark_geojson`) VALUES ('sample cource1',@json);