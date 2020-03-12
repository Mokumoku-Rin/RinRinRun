<template>
  <div class="home">
    <statusBar backgroundColor="white" :center="page_info.title" :right-func="confirmExit"></statusBar>
    <main>
      <div class="running_info section">
        <article class="running_info_section">
          <h2 class="running_info_title">現在の状況</h2>
          <h3 class="running_info_statistics_title">経過時間</h3>
          <p class="running_info_statistics_text running_info_time">{{msToTime(page_info.run_time)}}</p>
          <div class="running_info_statistics_wrapper">
            <div class="running_info_statistics">
              <h4 class="running_info_statistics_title">走った距離</h4>
              <p class="running_info_statistics_text">{{page_info.run_distance}}<span class="running_info_statistics_unit">km</span></p>
            </div>
            <div class="running_info_statistics">
              <h4 class="running_info_statistics_title">現在の順位</h4>
              <p class="running_info_statistics_text">{{page_info.ranking}}<span class="running_info_statistics_unit">位</span></p>
            </div>
          </div>
        </article>
        <section class="running_info_section">
          <h2 class="running_info_title">撮影場所とゴーストの情報</h2>
          <div class="running_info_map">
            <rin-rin-map :courseID="this.page_info.course_id" :myLocation="myLocation" :elapsedTime="mapElapsedTime" style="height:500px;" className="" ref="map"/>
          </div>
        </section>
      </div>
    </main>
    <cameraButton :link="{path: '/take-picture', query: {
        search_type: page_info.search_type, course_id: page_info.course_id, landmark_id: page_info.landmark_id, cleared: page_info.cleared } }" :active="page_info.active_button"></cameraButton>
  </div>
</template>

<style lang="scss">
@import "@/assets/scss/base/_variables.scss";
@import "@/assets/scss/modules/_home.scss";

.running_info {
  background: $white;
  padding-top: 1rem;
  padding-bottom: 1rem;
  height: calc(100% - 5.5rem);
  overflow-y: scroll;
  line-height: 1.7;
}

.running_info_section {
  margin-bottom: 1rem;
}

.running_info_title {
  font-size: 1.5rem;
  color: $black;
  font-weight: $weight-bold;
  margin-bottom: 1rem;
}

.running_info_statistics_wrapper {
  display: flex;
  justify-content: space-between;
}

.running_info_statistics {
  width: 45%;
}

.running_info_statistics_title {
  font-size: 1.25rem;
  color: $black;
  font-weight: $weight-bold;
}

.running_info_statistics_text {
  font-size: 2.5rem;
  color: $orange;
}

.running_info_time {
  font-size: 3.5rem;
}

.running_info_statistics_unit {
  font-size: 1.5rem;
}

.running_info_map {
  position: relative;
  border: 1px solid $black;
  border-radius: 2%;

  &:before {
    display: block;
    content: '';
    padding-top: 75%;
  }
}

.running_info_map_inner {
  position: absolute;
  top: 0;
  left: 0;
}
</style>

<script>
import router from '../router'

import statusBar from '@/components/StatusBar.vue'
import cameraButton from '@/components/CameraButton.vue'

import rinRinMap from '@/components/RinRinMap.vue'

const SOJO_GPS_POSITION = [34.878031, 135.575573]

export default {
  components: {
    statusBar,
    cameraButton,
    rinRinMap
  },
  data() {
    return {
      page_info: {
        title: 'テストコース1',
        search_type: '',  // コースの検索手法の記録
        course_id: 0,  // コース番号の記録
        landmark_id: 0,  // 撮影する写真のid
        active_button: false,  // 撮影が開始できるか
        cleared: 1,
        run_time: 0,
        run_distance: 0,
        ranking: 1
      },
      gpsTimerObj: null,
      mapTimerOnj: null, 
      isIntervalSet: false,
      myLocation: SOJO_GPS_POSITION,
      mapElapsedTime: 0, 
      stopWatchTimer: null,
      nearestID: 1
    }
  },
  created() {
    this.page_info.search_type = this.$route.query.search_type
    this.page_info.course_id = parseInt(this.$route.query.course_id)
    this.page_info.title = this.$store.state.runnigCourseData.name
  },
  methods: {
    confirmExit() {
      if(window.confirm("ランニングを中止しますか？\n中止をすると計測されたデータは破棄されます。")) {
        router.push('/home')
      }
    },
    msToTime(s) {
      var padding = function(num) {
        return ("00"+num).slice(-2)
      }
      var ms = s % 1000
      s = (s - ms) / 1000
      var secs = s % 60
      s = (s - secs) / 60
      var mins = s % 60
      var hrs = (s - mins) / 60
      return padding(hrs) + ':' + padding(mins) + ':' + padding(secs)
    },
    startRunning(){
      if(this.$store.state.isRunning === false){
        this.clearHistory()
      }
      if(this.isIntervalSet === false){
        this.gpsIntervalFunc() 
        this.gpsTimerObj = setInterval(this.gpsIntervalFunc, 5000) //5000 is ms
        this.mapTimerOnj = setInterval(this.mapIntervalFunc, 500) //500 is ms
        this.stopWatchTimer = setInterval(this.stopWatchFunc, 200)

        this.isIntervalSet = true
      }
      
      if(this.$store.state.isRunning === false){
        this.$store.commit('setIsRuning', true)
      }
    },
    stopRunning(){
      clearInterval(this.gpsTimerObj)
      clearInterval(this.mapTimerOnj)
      clearInterval(this.stopWatchTimer)
    },
    clearHistory(){
      this.$store.commit('clearMyGPSLocation')
      this.$store.commit('clearMyRunTimeList')
    },
    successGetGPS(position){
      const nowGPS = [position.coords.latitude, position.coords.longitude]
      this.$store.commit('addMyGPSLocation', nowGPS)
      this.myLocation = nowGPS

      this.$store.commit('setMyRunNowDistance', calDistance(this.$store.state.myGPSLocations))

      this.$store.commit('addMyRunTimeList', this.getElapssedTime())

      this.page_info.run_distance = calDistance(this.$store.state.myGPSLocations) / 1000
      console.log('success')
    },
    gpsIntervalFunc(){
      console.log('get location')
      navigator.geolocation.getCurrentPosition(this.successGetGPS, (error)=>{console.log('gps error',error.code)})
    },
    mapIntervalFunc(){
      this.mapElapsedTime = this.getElapssedTime()
      if(this.$refs.map.nearestLandmark()){
        const idDistance = this.$refs.map.nearestLandmark()
        if(idDistance){
          // 何メートルまで近づいたらカメラを起動するか
          if(idDistance.distance < 1000000){
            this.page_info.landmark_id = idDistance.id
            this.page_info.active_button = true
          }
        }
      }
    },
    getElapssedTime(){
      const tempDate = new Date()
      return tempDate.getTime() - this.$store.state.myRunStartTime
    },
    stopWatchFunc(){
      this.page_info.run_time = this.getElapssedTime()
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

      let geoJson = '{"type": "LineString",'
      geoJson += '"coordinates":' + coordinates + '}'

      let time_list = ""
      for(let i=0; i<this.$store.state.myRunTimeList.length; i++){
        if (i === 0){
          time_list += this.$store.state.myRunTimeList[i]
        }else{
          time_list += ','+this.$store.state.myRunTimeList[i]
        }
      }

      // TODO landmark_visitsの処理を追加する
      // ランドマークを回ったタイミングを出すには、それぞれのtimeが必要になる
      const distance = calDistance(this.$store.state.myGPSLocations)
      let postJson = {
        "properties":{
          "time_list": time_list,
          "total_distance": distance,
          "total_time": this.getElapssedTime()
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
      this.$postApi('/session/workout/', postJson)
    }
  },
  mounted(){
    this.startRunning()
  },
  beforeDestroy: function () {
    this.stopRunning()
  }
}


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
</script>
