<template>
  <div class="home">
    <statusBar :leftLink='{path: "/choice-course", query: { search_type: this.page_info.search_type } }' :center="page_info.title"></statusBar>
    <main>
      <div class="course_info section">
        <article class="course_info_section">
          <h2 class="course_info_title">コース情報</h2>
          <p class="course_info_description">{{course_info.description}}</p>
          <div class="course_info_statistics_wrapper">
            <section class="course_info_statistics">
              <h3 class="course_info_statistics_title">最短活動距離</h3>
              <p class="course_info_statistics_text">{{course_info.shortest_distance}}<span class="course_info_statistics_unit">km</span></p>
            </section>
            <section class="course_info_statistics">
              <h3 class="course_info_statistics_title">平均活動距離</h3>
              <p class="course_info_statistics_text">{{course_info.mean_distance}}<span class="course_info_statistics_unit">km</span></p>
            </section>
            <section class="course_info_statistics">
              <h3 class="course_info_statistics_title">最速タイム</h3>
              <p class="course_info_statistics_text">{{msToTime(course_info.shortest_time)}}</p>
            </section>
            <section class="course_info_statistics">
              <h3 class="course_info_statistics_title">平均タイム</h3>
              <p class="course_info_statistics_text">{{msToTime(course_info.mean_time)}}</p>
            </section>
          </div>
        </article>
        <section class="course_info_section">
          <h2 class="course_info_title">撮影場所</h2>
          <p class="course_info_description">
            撮影スポット周辺に移動すると、スポットの撮影ができるようになります。
          </p>
          <dispMap :courseID="parseInt(course_info.id)" className="course_info_map" :showMyLocation="true" ref="map"/>
        </section>
        <section class="course_info_section">
          <h2 class="course_info_title">撮影する写真</h2>
          <div class="course_info_photos_wrapper">
            <div class="course_info_photo" v-for="landmark in course_info.landmarks" :key="landmark.id">
              <router-link :to="{path: '/landmark-info', query: {search_type: page_info.search_type, course_id: page_info.course_id , landmark_id: landmark.id} }">
                <img class="course_info_photo_img" :src="landmark.img_url" :alt="landmark.name">
                <div class="course_info_photo_label">
                  <span class="course_info_photo_name">{{landmark.name}}</span>
                  <font-awesome-icon class="course_info_photo_chevron" icon="chevron-right"></font-awesome-icon>
                </div>
              </router-link>
            </div>
          </div>
        </section>
      </div>
    </main>
    <cameraButton :link="{path: '/take-picture', query: {
        search_type: page_info.search_type, course_id: page_info.course_id, landmark_id: page_info.landmark_id } }" :active="page_info.active_button"></cameraButton>
  </div>
</template>

<style lang="scss">
@import "@/assets/scss/base/_variables.scss";
@import "@/assets/scss/modules/_home.scss";

.course_info {
  background: $white;
  color: $black;
  height: 100%;
  overflow-y: scroll;

  &.section {
    padding-top: 0;
    padding-bottom: 0;
  }
  &::after{
    // 情報が最後まで表示されない問題の回避
    content: '';
    display: block;
    height: 5.5rem;
  }
}

.course_info_section {
  margin: 1.5rem 0;
  line-height: 1.75;
}

.course_info_title {
  font-size: 1.5rem;
  font-weight: $weight-bold;
  margin-bottom: .75rem;
}

.course_info_description {
  margin: .75rem 0;
}

.course_info_statistics_wrapper {
  margin: .75rem 0 -.5rem 0;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.course_info_statistics {
  width: 47.5%;
  margin: .5rem 0;
  line-height: 1.5;
}

.course_info_statistics_title {
  font-size: 1.2rem;
  font-weight: $weight-bold;
}

.course_info_statistics_text {
  color: $orange;
  font-size: 1.75rem;
}

.course_info_statistics_unit {
  font-size: 1rem;
}

.course_info_map {
  margin: .5rem 0;
  border: 1px solid $black;
  border-radius: 2%;
  width: 100%;
  position: relative;

  &::before {
    content: '';
    display: block;
    padding-top: 75%;
  }
}

.course_info_photos_wrapper {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.course_info_photo {
  width: 47.5%;
  margin: .5rem 0;
}

.course_info_photo_img {
  border: 1px solid $black;
  border-radius: 2%;
}

.course_info_photo_label {
  display: flex;
  justify-content: center;
  align-items: center;
}

.course_info_photo_name {
  display: -webkit-box;
  overflow: hidden;
  text-overflow: ellipsis;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
  height: 1.5em;
  max-width: 80%;
}

.course_info_photo_chevron {
  color: $red;
  margin-left: .5rem;
}
</style>

<script>
import statusBar from '@/components/StatusBar.vue'
import cameraButton from '@/components/CameraButton.vue'
import dispMap from '@/components/DispMap.vue'
// import testImage from '@/assets/img/jogging.svg'
import firebase from 'firebase/app'

export default {
  data() {
    return {
      page_info: {
        title: '',
        search_type: '',  // コースの検索手法の記録
        course_id: 0,  // コース番号の記録
        landmark_id: 0,  // 撮影する写真のid
        active_button: false,  // 撮影が開始できるか
        check_nearest_landmark_timer: null,
      },
      course_info: {
        id: 0,
        name: 'テストコース',
        description: 'コース説明コース説明コース説明コース説明コース説明コース説明コース説明コース説明コース説明コース説明コース説明コース説明',
        mean_distance: 0,
        shortest_distance: 0,
        mean_time: 0,
        shortest_time: 0,
        landmarks: null
      }
    }
  },
  created() {
    this.course_info.id = this.$route.query.course_id
    // idから情報を取得するコード
    this.$getApi('/session/course/'+this.course_info.id+'/', {}, (res)=>{
      this.course_info.name = res.data.neme
      this.course_info.description = res.data.description
      this.course_info.mean_distance = res.data.mean_distance
      this.course_info.mean_time = res.data.mean_time
      this.course_info.shortest_time = res.data.shortest_time
      this.course_info.shortest_distance = res.data.shortest_distance

      const editedCourseData = res.data
      const storageRef = firebase.storage().ref()
      const this_ref = this
      let urlCallbackCount = 0
      for(let index = 0; index < editedCourseData.landmarks.length; index++){
        storageRef.child(editedCourseData.landmarks[index].img_path).getDownloadURL().then(function(url) {
          urlCallbackCount++
          editedCourseData.landmarks[index].img_url = url
          if(urlCallbackCount === editedCourseData.landmarks.length){
            this_ref.$store.commit('setRunnigCourseData', editedCourseData)
            this_ref.course_info.landmarks = editedCourseData.landmarks
            console.log(this_ref.$store.state.runnigCourseData)
          }
        }).catch(function(error) {
          console.log(error)
        })
      }
    })

    this.page_info.search_type = this.$route.query.search_type
    this.page_info.course_id = this.$route.query.course_id
    this.page_info.title = this.course_info.name
  },
  mounted() {
    this.check_nearest_landmark_timer = setInterval(this.checkNearestLandmark, 1000)
  },
  components: {
    statusBar,
    cameraButton,
    dispMap
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
    checkNearestLandmark(){
      if(this.$refs.map.nearestLandmark()){
        const idDistance = this.$refs.map.nearestLandmark()
        if(idDistance){
          // 何メートルまで近づいたらカメラを起動するか
          if(idDistance.distance < 1000000000){
            this.page_info.landmark_id = idDistance.id
            this.page_info.active_button = true
          }
          console.log(idDistance.distance)
        }
      }
    }
  },
  beforeDestroy: function () {
    clearInterval(this.check_nearest_landmark_timer)
  }
}
</script>
