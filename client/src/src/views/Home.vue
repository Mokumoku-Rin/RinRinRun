<template>
  <div class="home with-navibar">
    <statusBar center="今日の記録" :avatar="account.avatar" :rightFunc="confirmLogout"></statusBar>
    <main>
      <article class="today__no_data section" v-if="isEmpty(today_data)">
        <h2 class="title">記録がありません</h2>
        <router-link to="/search-course">
          <p class="message has-text-red">
            今からランニングを開始する
            <font-awesome-icon icon="chevron-right"></font-awesome-icon>
          </p>
        </router-link>
        <img src="@/assets/img/jogging.svg" alt="ジョギング">
      </article>

      <div class="today__has_data" v-else>
        <header class="today_top section">
          <section class="today_distance">
            <h2 class="today_data_title">距離</h2>
            <p class="today_data_text">{{today_data.distance}}<span class="today_data_unit">m</span></p>
          </section>
        </header>
        <div class="today_main section">
          <div class="today_informations">
            <section class="today_time">
              <h2 class="today_data_title">時間</h2>
              <p class="today_data_text">{{msToTime(today_data.time)}}</p>
            </section>
            <section class="today_calorie">
              <h2 class="today_data_title">消費カロリー</h2>
              <p class="today_data_text">{{today_data.calorie}}<span class="today_data_unit">kcal</span></p>
            </section>
          </div>
          <section class="today_course">
            <h2 class="today_data_title">走ったコース</h2>
            <!-- TODO スタイル修正 -->
            <dispMap :routes="routes" ref="map" className="today_map"/>
            <!-- <div class="today_map">地図</div> -->
          </section>
        </div>
      </div>
    </main>
    <naviBar active="Today"></naviBar>
  </div>
</template>

<style lang="scss">
@import "@/assets/scss/base/_variables.scss";
@import "@/assets/scss/modules/_home.scss";

.today__no_data {
  display: flex;
  height: 100%;
  flex-direction: column;
  justify-content: center;
  background: $white;

  .title, .message {
    margin-bottom: 1rem;
  }
  .title {
    color: $black;
  }
  .message {
    background: transparent;
  }
  img {
    width: 80%;
    margin: 0 auto;
  }
}

.has-text-red {
  color: $red;
}

.has-text-orange {
  color: $orange;
}

.today__has_data {
  display: flex;
  flex-direction: column;
  height: 100%;
  line-height: 1.4;

  .section {
    padding-top: 1rem;
    padding-bottom: 1rem;
  }
}

.today_top {
  color: $white;
  flex-grow: 0;
  .today_data_text {
    color: $white;
  }
}

.today_main {
  background: $white;
  flex-grow: 1;
  display: flex;
  flex-direction: column;
}

.today_informations {
  flex-grow: 0;
  display:flex;
}

.today_calorie {
  margin-left: .5rem;
}

.today_course {
  margin-top: 1rem;
  flex-grow: 1;
  padding-bottom: 2rem;
}

.today_data_title {
  font-size: 1.25rem;
  font-weight: $weight-bold;
}

.today_data_text {
  font-size: 2rem;
  color: $orange;
}

.today_data_unit {
  font-size: 1.25rem;
  margin-left: .25rem;
}

.today_map {
  margin-top: .5rem;
  border: 1px solid $black;
  border-radius: 2%;
  height: calc(100% - 3.5rem);
}
</style>

<script>
import firebase from 'firebase/app'
import router from '../router'

import statusBar from '@/components/StatusBar.vue'
import naviBar from '@/components/NaviBar.vue'
import dispMap from '@/components/DispMap.vue'

import testAvatarImage from '@/assets/img/user-circle.svg'

export default {
  data() {
    return {
      account: {
        avatar: testAvatarImage
      },
      today_data: {
        // distance: 0,
        // time: 0,  // ミリ秒
        // calorie: 0,
        // course: {}
      },
      routes: null,
    }
  },
  created() {
    // アバターを取得するコード（書き換え予定）
    var user = firebase.auth().currentUser
    this.account.avatar = user.photoURL

    this.$getApi('/session/workout/', {date: getNowYMD()}, (res)=>{
      if(res.data.datas.length > 0){
        let totalDistance = 0
        let totalTime = 0
        let tempRoutes = []
        for(const data of res.data.datas){
          totalDistance += data.total_distance
          totalTime += data.total_time
          tempRoutes.push(data.geo_json.coordinates)
        }
        this.$set(this.today_data, 'distance', totalDistance)
        this.$set(this.today_data, 'time', totalTime)
        this.$set(this.today_data, 'calorie', calCalorie(totalTime / 1000 / 3600).toFixed(3))
        this.routes = tempRoutes
      }
    })
  },
  components: {
    statusBar,
    naviBar,
    dispMap
  },
  methods: {
    confirmLogout() {
      console.log('読み込まれた')
      if(window.confirm("ログアウトしますか？")) {
        firebase.auth().signOut().then(function() {
          router.push('/login-home')
        }).catch(error => {
          console.log(error.message)
          router.push('/login-home')
        })
      }
    },
    isEmpty(obj) {
      // console.log(obj)
      // console.log(Object.keys(obj).length === 0)
      // console.log(obj.constructor === Object)
      return Object.keys(obj).length === 0 && obj.constructor === Object
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
    }
  }
}


function getNowYMD(){
  var dt = new Date();
  var y = dt.getFullYear();
  var m = ("00" + (dt.getMonth()+1)).slice(-2);
  var d = ("00" + dt.getDate()).slice(-2);
  var result = y + "-" + m + "-" + d;
  return result;
}

// 消費カロリー(kcal) ＝ メッツ * 体重kg * 運動時間 * 1.05
// 体重はわからないので65で計算
// timeは h
function calCalorie(time){
  const mets = 9
  return mets * 65 * time * 1.05
}
</script>
