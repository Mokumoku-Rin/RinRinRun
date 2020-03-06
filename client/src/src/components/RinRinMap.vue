<template>
  <div>
    <div id='map'></div>
    this is map
    <button @click="startGetGPS">計測スタート</button>
    <button @click="stopGetGPS">計測ストップ</button>
    <button @click="clearGPSHistory">クリア</button>
    <button @click="showGPSHistory">GPS計測結果</button>
    <button @click="sendGPSHistory">計測結果を送信</button>
    <br>
    <button @click="test">test func</button>

  </div>
</template>

<script>
import L from 'leaflet'

// デフォルトマーカーアイコン設定
delete L.Icon.Default.prototype._getIconUrl;
L.Icon.Default.mergeOptions({
    iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
    iconUrl: require('leaflet/dist/images/marker-icon.png'),
    shadowUrl: require('leaflet/dist/images/marker-shadow.png')
});

const SOJO_GPS_POSITION = [34.878031, 135.575573]

function calDistance(positionList){
  let distance = 0.0

  if(positionList.length < 2)return 0

  for(let i=1; i<positionList.length; i++){
    // 緯度経度をラジアンに変換
    const radLatitudeA = deg2rad(positionList[i-1][0])
    const radLongitudeA = deg2rad(positionList[i-1][1])
    const radLatitudeB = deg2rad(positionList[i][0])
    const radLongitudeB = deg2rad(positionList[i][1])

    const radLatDiff = radLatitudeA - radLatitudeB
    const radLonDiff = radLongitudeA - radLongitudeB

    const radLatAve = (radLatitudeA + radLatitudeB) / 2.0;

    const a = 6378137.0 // 赤道半径
    const e2 = 0.00669438002301188 // 第一離心率^2
    const a1e2 = 6335439.32708317 // 赤道上の子午線曲率半径

    let sinLat = Math.sin(radLatAve)

    sinLat = Math.sin(radLatAve)
    let W2 = 1.0 - e2 * (sinLat*sinLat)
    let M = a1e2 / (Math.sqrt(W2)*W2); // 子午線曲率半径M
    let N = a / Math.sqrt(W2); // 卯酉線曲率半径

    let t1 = M * radLatDiff
    let t2 = N * Math.cos(radLatAve) * radLonDiff
    let dist = Math.sqrt((t1*t1) + (t2*t2))

    distance += dist
  }
  return distance
}

function deg2rad(deg){
  return deg * ( Math.PI / 180 )
}

export default {
  data() {
    return {
      gpsTimerObj: null,
      isGpsIntervalSet: false,
      map: null,
      startDate: new Date(),
      startTime: 0
    }
  },
  methods:{
    startGetGPS(){
      if(this.isGpsIntervalSet === false){
        this.gpsIntervalFunc() 
        this.gpsTimerObj = setInterval(this.gpsIntervalFunc, 5000) //5000 is ms
        this.isGpsIntervalSet = true
        const tempDate = new Date()
        this.startTime = tempDate.getTime()
      }
    },
    successGetGPS(position){
      const nowGPS = [position.coords.latitude, position.coords.longitude]
      this.$store.commit('addMyGPSLocation', nowGPS)
      this.map.setView(nowGPS)

      const tempDate = new Date()
      this.$store.commit('addMyRunTimeList', tempDate.getTime() - this.startTime)

      console.log('success')
    },
    gpsIntervalFunc(){
      console.log('get location')
      navigator.geolocation.getCurrentPosition(this.successGetGPS, (error)=>{console.log('gps error',error.code)})
    },
    stopGetGPS(){
      clearInterval(this.gpsTimerObj)
    },
    clearGPSHistory(){
      this.$store.commit('clearMyGPSLocation')
    },
    showGPSHistory(){
      console.log(this.$store.state.myGPSLocations)
    },
    sendGPSHistory(){
      let coordinates = '['
      for(let i=0; i<this.$store.state.myGPSLocations.length; i++){
        if (i !== 0){
          coordinates += ',['+this.$store.state.myGPSLocations[i][0] + ',' + this.$store.state.myGPSLocations[i][1] + ']'
        }else{
          coordinates += '['+this.$store.state.myGPSLocations[i][0] + ',' + this.$store.state.myGPSLocations[i][1] + ']'
        }
      }
      coordinates += ']' 

      let geoJson = '{"type": "LineString","crs": { "type": "name"},'
      geoJson += '"coordinates":' + coordinates + '}'

      // TODO landmark_visitsの処理を追加する
      // ランドマークを回ったタイミングを出すには、それぞれのtimeが必要になる
      const distance = calDistance(this.$store.state.myGPSLocations)
      let postJson = {
        "properties":{
          "time_list": this.$store.state.myRunTimeList,
          "total_distance": distance,
          "total_time": this.$store.state.myRunTimeList[this.$store.state.myRunTimeList.length - 1]
        },
        "landmark_visits": [
          {
            "id": 1,
            "time": 10000
          },
          {
            "id": 2,
            "time": 20000
          }
        ],
        "geo_json":geoJson
      }
      console.log(postJson)
      this.$postApi('/session/workout', postJson)
    },
    test(){
      console.log(calDistance([[36.10377477777778, 140.08785502777778], [35.65502847222223, 139.74475044444443]]))
    }
  },
  mounted: function () {
    const mapDefaultZoomLevel = 17
    //MAP読み込み
    this.map = L.map('map').setView(SOJO_GPS_POSITION, mapDefaultZoomLevel);
    //map boxを現在使用しているが、より良いものがあったら変える
    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
      attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
      maxZoom: 20,
      id: 'mapbox/streets-v10', //v11もあるがv10の方が詳細な地図が出るためv10を使う
      tileSize: 512,
      zoomOffset: -1,
      accessToken: process.env.VUE_APP_MAP_BOX_API_KYE
     }).addTo(this.map);
  },
  destroyed: function () {
    this.stopGetGPS()
  }
}
</script>

<style scoped>
  #map {
    z-index: 0;
    height: 100%;
    min-height: 200px;
  }
</style>