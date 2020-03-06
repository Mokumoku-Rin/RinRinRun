<template>
  <div>
    <div id='map'></div>
    this is map
    <button @click="startGetGPS">計測スタート</button>
    <button @click="stopGetGPS">計測ストップ</button>
    <button @click="clearGPSHistory">クリア</button>
    <button @click="showGPSHistory">計測結果</button>
    <button @click="sendGPSHistory">計測結果を送信</button>

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

export default {
  data() {
    return {
      gpsTimerObj: null,
      isGpsIntervalSet: false,
      map: null,
    }
  },
  methods:{
    startGetGPS(){
      if(this.isGpsIntervalSet === false){
        this.gpsIntervalFunc() 
        this.gpsTimerObj = setInterval(this.gpsIntervalFunc, 5000) //5000 is ms
        this.isGpsIntervalSet = true
      }
    },
    successGetGPS(position){
      const nowGPS = [position.coords.latitude, position.coords.longitude]
      this.$store.commit('addMyGPSLocation', nowGPS)
      console.log('gps success')
      this.map.setView(nowGPS)
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

      let geoJson = ` { "type": "LineString",
                      "crs": { "type": "name"
                      },`;      
      geoJson += '"coordinates":' + coordinates + '}'

      console.log(geoJson)
      // TODO 送信処理 
      // TODO total timeとかを追加する
      // ランドマークを回ったタイミングを出すには、それぞれのtimeが必要になる
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