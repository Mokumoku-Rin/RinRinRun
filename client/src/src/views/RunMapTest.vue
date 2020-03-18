<template>
  <div>
    test
    <rin-rin-map :courseID="1" :myLocation="myLocation" :elapsedTime="mapElapsedTime"/>
    <button @click="startRunning">計測スタート</button>
    <button @click="stopRunning">計測ストップ</button>
    <button @click="clearHistory">クリア</button>
    <button @click="showGPSHistory">GPS計測結果</button>
    <button @click="sendGPSHistory">計測結果を送信</button>
  </div>
</template>

<script>
import rinRinMap from '@/components/RinRinMap.vue'

const SOJO_GPS_POSITION = [34.878031, 135.575573]

// TODO サーバーから取得する
const dummyGhostData = [
  {
    name: 'hogehoge',
    img_url: 'example.com',
    time_list: [0, 5500, 10010, 16000],
    pos_list: [[34.878834, 135.575930], [34.878623, 135.575838], [34.878515, 135.575773], [34.878468, 135.575622]],
    total_distance: 123,
    score: 123, //なくてもいいかも
    landmark_visits:[
      {
        id: 1,
        time: 7000
      },
      {
        id: 2,
        time: 17000
      },
    ]
  },
  {
    name: 'piyopiyo',
    img_url: 'example.com',
    time_list: [0, 5500, 10010, 16000],
    pos_list: [[34.878822, 135.575930], [34.878517, 135.575880], [34.878446, 135.576017], [34.878245, 135.575942]],
    total_distance: 123,
    score: 123, //なくてもいいかも
    landmark_visits:[
      {
        id: 1,
        time: 7000
      },
      {
        id: 2,
        time: 17000
      },
    ]
  }
]

export default {
  components: {
    rinRinMap
  },
  data() {
    return {
      gpsTimerObj: null,
      mapTimerOnj: null, 
      isIntervalSet: false,
      myLocation: SOJO_GPS_POSITION,
      ghostData: dummyGhostData,
      mapElapsedTime: 0, 
    }
  },
  methods: {
    startRunning(){
      this.clearHistory()
      if(this.isIntervalSet === false){
        this.gpsIntervalFunc() 
        this.gpsTimerObj = setInterval(this.gpsIntervalFunc, 5000) //5000 is ms
        this.mapTimerOnj = setInterval(this.mapIntervalFunc, 500) //500 is ms

        this.isIntervalSet = true
        this.$store.commit('resetMyRunStartTime')
      }
    },
    stopRunning(){
      clearInterval(this.gpsTimerObj)
      clearInterval(this.mapTimerOnj)
    },
    clearHistory(){
      this.$store.commit('clearMyGPSLocation')
      this.$store.commit('clearMyRunTimeList')
    },
    showGPSHistory(){
      console.log(this.$store.state.myGPSLocations)
    },
    successGetGPS(position){
      const nowGPS = [position.coords.latitude, position.coords.longitude]
      this.$store.commit('addMyGPSLocation', nowGPS)
      // this.myLocation = nowGPS
      // TODO 上に書き換える
      this.myLocation = SOJO_GPS_POSITION

      this.$store.commit('setMyRunNowDistance', this.$calDistance(this.$store.state.myGPSLocations))

      this.$store.commit('addMyRunTimeList', this.getElapssedTime())
      console.log('success')
    },
    gpsIntervalFunc(){
      console.log('get location')
      navigator.geolocation.getCurrentPosition(this.successGetGPS, (error)=>{console.log('gps error',error.code)})
    },
    mapIntervalFunc(){
      this.mapElapsedTime = this.getElapssedTime()
    },
    getElapssedTime(){
      const tempDate = new Date()
      return tempDate.getTime() - this.$store.state.myRunStartTime
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
      const distance = this.$calDistance(this.$store.state.myGPSLocations)
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
  destroyed: function () {
    this.stopRunning()
  }
}


</script>

<style>

</style>