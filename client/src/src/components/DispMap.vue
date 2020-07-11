<template>
  <div style="height: 100%;">
    <div id='map' v-bind:class="className"></div>
    <div v-if="this.showMyLocation">
      <input type="radio" name="test1" id="総情" checked="checked"><label for="総情">総情</label>
      <input type="radio" name="test1" id="実際"><label for="実際">実際の位置</label>
    </div>
  </div>
</template>

<script>
import L from 'leaflet'
import pinPath from '@/assets/img/pin_offset.svg'
import myRunnerPath from '@/assets/img/my_runner.svg'

// デフォルトマーカーアイコン設定
delete L.Icon.Default.prototype._getIconUrl;
L.Icon.Default.mergeOptions({
    iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
    iconUrl: require('leaflet/dist/images/marker-icon.png'),
    shadowUrl: require('leaflet/dist/images/marker-shadow.png')
});

const SOJO_GPS_POSITION = [34.878031, 135.575573]

export default {
  props: {
    courseID: {
      type: Number
    },
    routes: {
      type: Array
    },
    className: {
      type: String,
      default: ""
    },
    showMyLocation: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      map: null,
      gpsTimerObj: null,
      existDrawedRunner: [],
      existDrawedPinRoute: [],
      location: null,
      landmarks: null
    }
  },
  mounted: function () {
    console.log('location pathname: ', location.pathname)
    const mapDefaultZoomLevel = 17
    //MAP読み込み
    this.map = L.map('map').setView(SOJO_GPS_POSITION, mapDefaultZoomLevel)
    //map boxを現在使用しているが、より良いものがあったら変える
    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
      attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
      maxZoom: 20,
      id: 'mapbox/streets-v10', //v11もあるがv10の方が詳細な地図が出るためv10を使う
      tileSize: 512,
      zoomOffset: -1,
      accessToken: process.env.VUE_APP_MAP_BOX_API_KEY
     }).addTo(this.map)

    if(this.showMyLocation){
      this.gpsIntervalFunc()
      this.gpsTimerObj = setInterval(this.gpsIntervalFunc, 5000) //5000 is ms
    }

    this.render()
  },
  methods: {
    gpsIntervalFunc(){
      navigator.geolocation.getCurrentPosition(this.successGetGPS, (error)=>{console.log('gps error',error.code)})
    },
    successGetGPS(position){
      for(const eLayer of this.existDrawedRunner){
        this.map.removeLayer(eLayer)
      }
      this.existDrawedRunner.length = 0
      if (document.getElementById("総情").checked){
        this.location = SOJO_GPS_POSITION
      }else{
        this.location = [position.coords.latitude, position.coords.longitude]
      }
      this.existDrawedRunner.push(L.marker(this.location, {icon: L.icon({iconUrl: myRunnerPath, iconSize: [30, 30]})}).addTo(this.map))

      this.map.setView(this.location)
      console.log('success')
    },
    nearestLandmark(){
      if(this.location){
        let nearestID = 0;
        let nearestDistance = 99999999999999
        for(const landmark of this.landmarks){
          const landmarkTempPos = landmark.pos.split(',')
          const distance = this.$calDistance([this.location, landmarkTempPos])
          if(distance < nearestDistance){
            nearestDistance = distance
            nearestID = landmark.id
          } 
        }

        return {id: nearestID, distance: nearestDistance}
      }
      return false
    },
    render(){
      for(const eLayer of this.existDrawedPinRoute){
        this.map.removeLayer(eLayer)
      }

      const pinIcon = L.icon({ iconUrl: pinPath, iconSize: [38, 95]})
      if(this.courseID){
        this.$getApi('/session/course/'+this.courseID+'/', {}, (response)=>{
          this.landmarks = response.data.landmarks
          for(const landmark of this.landmarks){
            const tempPos = landmark.pos.split(',')
            this.existDrawedPinRoute.push(L.marker(tempPos,{icon: pinIcon}).bindPopup('<b>'+landmark.name+'</b><br>'+landmark.description).addTo(this.map))
          }
        })
      }
      
      if(this.routes){
        for(const route of this.routes){
          this.existDrawedPinRoute.push(L.polyline(route,{
            "color": "#FF0000",
            "weight": 5,
            "opacity": 0.6
          }).addTo(this.map))
        }
      }
    }
  },
  beforeDestroy: function () {
    if(this.showMyLocation){
      clearInterval(this.gpsTimerObj)
    }
  },
  watch:{
    routes:function(){
      this.render()
    }
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
