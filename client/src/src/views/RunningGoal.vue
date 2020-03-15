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
          <h2 class="running_goal_title">走ったコース</h2>
          <div class="running_goal_map">
          </div>
        </section>
        <section class="running_goal_section">
          <h2 class="running_goal_title">距離</h2>
          <p class="running_goal_text">{{page_info.distance}}<span class="running_goal_unit">km</span></p>
        </section>
        <section class="running_goal_section">
          <h2 class="running_goal_title">時間</h2>
          <p class="running_goal_text">{{msToTime(page_info.time)}}</p>
        </section>
        <section class="running_goal_section">
          <h2 class="running_goal_title">消費カロリー</h2>
          <p class="running_goal_text">{{page_info.calorie}}</p>
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

export default {
  components: {
    statusBar
  },
  data() {
    return {
      page_info: {
        distance: 0,
        time: 0,
        calorie: 0
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
    }
  }
}
</script>
