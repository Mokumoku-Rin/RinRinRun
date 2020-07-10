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
              <p class="running_info_statistics_text">{{page_info.run_distance}}<span class="running_info_statistics_unit">m</span></p>
            </div>
            <div class="running_info_statistics">
              <h4 class="running_info_statistics_title">現在の順位</h4>
              <p class="running_info_statistics_text">{{page_info.ranking}}<span class="running_info_statistics_unit">位</span></p>
            </div>
          </div>
        </article>
        <section class="running_info_section">
          <h2 class="running_info_title">撮影場所とゴーストの情報</h2>
            <rin-rin-map :courseID="this.page_info.course_id" :myLocation="myLocation" :elapsedTime="mapElapsedTime" className="running_info_map" ref="map"/>
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
  color: $black;
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
  font-size: 1.4rem;
  color: $black;
  font-weight: $weight-bold;
}

.running_info_statistics_text {
  font-size: 3rem;
  color: $orange;
}

.running_info_time {
  font-size: 3.75rem;
}

.running_info_statistics_unit {
  font-size: 1.5rem;
  margin-left: .25rem;
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
    this.page_info.title = this.$store.state.runningCourseData.name
  },
  methods: {
    confirmExit() {
      if(window.confirm("ランニングを中止しますか？\n中止をすると計測されたデータは破棄されます。")) {
        this.$store.commit('setIsRuning', false)
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
      this.$store.commit('resetMyRunStartTime')
    },
    successGetGPS(position){
      const nowGPS = [position.coords.latitude, position.coords.longitude]
      this.$store.commit('addMyGPSLocation', nowGPS)
      this.myLocation = nowGPS

      this.$store.commit('setMyRunNowDistance', this.$calDistance(this.$store.state.myGPSLocations))

      this.$store.commit('addMyRunTimeList', this.getElapssedTime())

      const distMetre = this.$calDistance(this.$store.state.myGPSLocations)
      this.page_info.run_distance = Math.round(distMetre)
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
    stopWatchFunc(){
      this.page_info.run_time = this.getElapssedTime()
    },
    getElapssedTime(){
      const tempDate = new Date()
      return tempDate.getTime() - this.$store.state.myRunStartTime
    },
  },
  mounted(){
    this.startRunning()
  },
  beforeDestroy: function () {
    this.stopRunning()
  }
}

</script>
