<template>
  <div class="home">
    <statusBar center="ゴール" right-link="/home"></statusBar>
    <main>
      <div class="running_goal section">
        <div class="running_goal_section">
          <strong class="running_goal_ome">おめでとうございます！</strong>
          <p class="running_goal_message">
            お疲れさまでした。<br/>
            今回の結果は次の通りです。
          </p>
        </div>
        <section class="running_goal_section">
          <h2 class="running_goal_title">ランク</h2>
          <p class="running_goal_text">{{page_info.rank}}</p>
        </section>
        <section class="running_goal_section">
          <h2 class="running_goal_title">走ったコース</h2>
          <dispMap :courseID="this.$store.state.runningCourseData.id" :routes="[this.$store.state.myGPSLocations]" className="running_goal_map"/>
          <!-- <div class="running_goal_map">
          </div> -->
        </section>
        <section class="running_goal_section">
          <h2 class="running_goal_title">距離</h2>
          <p class="running_goal_text">{{page_info.distance}}<span class="running_goal_unit">m</span></p>
        </section>
        <section class="running_goal_section">
          <h2 class="running_goal_title">時間</h2>
          <p class="running_goal_text">{{msToTime(page_info.time)}}</p>
        </section>
        <section class="running_goal_section">
          <h2 class="running_goal_title">消費カロリー(体重65kgで計算)</h2>
          <p class="running_goal_text">{{page_info.calorie.toFixed(3)}} kcal</p>
        </section>
      </div>
    </main>
  </div>
</template>

<style lang="scss">
@import "@/assets/scss/base/_variables.scss";
@import "@/assets/scss/modules/_home.scss";

.running_goal {
  background: $white;
  height: 100%;
  overflow-y: scroll;
  padding-top: 0;
  padding-bottom: 0;
  line-height: 1.7;
  color: $black;
}

.running_goal_section {
  margin: 1.5rem 0;
}

.running_goal_ome {
  font-size: 1.75rem;
  color: $black;
}

.running_goal_message {
  margin-top: 1rem;
  font-size: 1.25rem;
}

.running_goal_title {
  font-size: 1.5rem;
  font-weight: $weight-bold;
}

.running_goal_text {
  font-size: 2.5rem;
  color: $orange;
}

.running_goal_unit {
  font-size: 1.5rem;
  margin-left: .25rem;
}

.running_goal_map {
  border: 1px solid $black;
  border-radius: 2%;
  margin-top: .75rem;

  &::before {
    content: '';
    display: block;
    padding-top: 72.5%;
  }
}
</style>

<script>
import statusBar from '@/components/StatusBar.vue'
import dispMap from '@/components/DispMap.vue'

export default {
  components: {
    statusBar,
    dispMap
  },
  data() {
    return {
      page_info: {
        distance: this.$calDistance(this.$store.state.myGPSLocations),
        time: this.$store.state.myLandmarkVisits[this.$store.state.myLandmarkVisits.length - 1].time,
        calorie: calCalorie(this.$store.state.myLandmarkVisits[this.$store.state.myLandmarkVisits.length - 1].time / 1000 / 3600), // この辺直した方がいい
        rank: ''
      }
    }
  },
  methods: {
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
    sendResult(){
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

      const distance = this.$calDistance(this.$store.state.myGPSLocations)
      let postJson = {
        "properties":{
          "time_list": time_list,
          "total_distance": distance,
          "total_time": this.$store.state.myLandmarkVisits[this.$store.state.myLandmarkVisits.length - 1].time,
          "course_id": this.$store.state.runningCourseData.id
        },
        "landmark_visits": this.$store.state.myLandmarkVisits, 
        "geo_json":geoJson
      }
      console.log(postJson)
      this.$postApi('/session/workout/', postJson)
    },
    setRank(){
      this.$getApi(`/session/workout/course/${this.$store.state.runningCourseData.id}/`, {}, (res)=>{
        let rankTmp = 1
        for(const userData of res.data.results){
          if(userData.total_time < this.$store.state.myLandmarkVisits[this.$store.state.myLandmarkVisits.length - 1].time){
            rankTmp++
          } 
        }
        if(res.data.results.length < 1){
          this.page_info.rank = `${rankTmp}位`
        }else{
          this.page_info.rank = `${rankTmp} / ${res.data.results.length + 1}位`
        }
      })
    }
  },
  created(){
    this.setRank()
    this.sendResult()
    this.$store.commit('setIsRuning', false)
  },
}

// 消費カロリー(kcal) ＝ メッツ * 体重kg * 運動時間 * 1.05
// 体重はわからないので65で計算
// timeは h
function calCalorie(time){
  const mets = 9
  return mets * 65 * time * 1.05
}
</script>
