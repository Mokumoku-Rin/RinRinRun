<template>
  <div>
    <div id='map'></div>
    this is map
  </div>
</template>

<script>
import L from 'leaflet'

import myRunnerPath from '@/assets/img/my_runner.svg'
import ghostPath from '@/assets/img/ghost.svg'
import pinPath from '@/assets/img/pin_offset.svg'

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
      type: Number,
      required: true
    },
    myLocation: {
      type: Array,
      required: true
    },
    ghostData: {
      type: Array,
      required: true
    },
    elapsedTime: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      gpsTimerObj: null,
      isGpsIntervalSet: false,
      map: null,
      existDrawed: [],
      landmarks: {}
    }
  },
  methods:{
    removeLayerDrawed(){
      for(const eLayer of this.existDrawed){
        this.map.removeLayer(eLayer)
      }
      this.existDrawed.length = 0
    },
    setMapLandmark(){
      for(const landmark of this.landmarks){
        // check ずみ
        if(this.$store.state.myRunCheckedLandmarkID.includes(landmark.id)) continue

        const tempPos = landmark.pos.split(',')
        const pinIcon = L.icon({ iconUrl: pinPath, iconSize: [38, 95]})
        this.existDrawed.push(L.marker(tempPos,{icon: pinIcon}).bindPopup('<b>'+landmark.name+'</b><br>'+landmark.description).addTo(this.map))
      }
    },
    reRender(){
      console.log('re render')
      this.removeLayerDrawed()
      this.setMapLandmark()

      this.existDrawed.push(L.marker(this.myLocation, {icon: L.icon({iconUrl: myRunnerPath, iconSize: [30, 30]})}).addTo(this.map))
      for(const ghost of this.ghostData){
        const dispRouteList = []
        let dispNowGPS = ghost.pos_list[0]

        // for of は遅いらしいので使用しない
        for(let index = 0; index < ghost.time_list.length; index++){
          if(ghost.time_list[index] < this.elapsedTime){
            dispRouteList.push(ghost.pos_list[index])
            dispNowGPS = ghost.pos_list[index]
          }
        }

        if(dispRouteList.length > 1){
            this.existDrawed.push( L.polyline(dispRouteList,{
              "color": "#FF0000",
              "weight": 5,
              "opacity": 0.6
            }).addTo(this.map) )
        }
        this.existDrawed.push(L.marker(dispNowGPS, {icon: L.icon({iconUrl: ghostPath, iconSize: [30, 30]})}).addTo(this.map))
      }

      this.map.setView(this.myLocation)
    }
  },
  mounted: function () {
    const mapDefaultZoomLevel = 18
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
     
    this.$getApi('/session/course/'+this.courseID+'/', {}, (response)=>{
      this.landmarks = response.data.landmarks
      this.setMapLandmark()
    })

  },
  watch: {
    myLocation: function(){
      this.reRender()
    },
    elapsedTime: function(){
      this.reRender()
    }
  }
}
</script>

<style scoped>
  #map {
    z-index: 0;
    height: 100%;
    min-height: 500px;
  }
</style>
