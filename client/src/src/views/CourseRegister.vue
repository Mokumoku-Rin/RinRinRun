<template>
<div class="home">
  <statusBar center="コースの登録"></statusBar>
  <main class="main">
    <div v-for="landmark of landmarks"  v-bind:key="landmark.id">
      <label class="landmark_label">
        <input type="checkbox" @change="changeCheck(landmark.id)">
        {{ landmark.name }}
      </label>
      <!-- <span style="font-size: 1.5em;"></span><br> -->
      <p>{{ landmark.description }}</p>
      <img class="landmark_img" :src="landmark.img_url" :alt="landmark.name" style="height: 200px;">
      <hr>
    </div>
    <p>登録情報</p>
    <hr>
    <p>ランドマークID</p>
    <ul>
      <li v-for="item of checkedLandmark" v-bind:key="item">
        {{ item }}
      </li>
    </ul>
    <p>コース名</p>
    <input v-model="courseTitle" id="course-title-input"/>
    <p>コースの説明</p>
    <textarea v-model="courseDesc" id="course-desc-text-area"/>
    <hr>
    <div class="button_warapper">
      <button class="post_course" @click="postToServer">サーバに投稿</button>
    </div>
  </main>
</div>
</template>

<script>
import firebase from 'firebase/app'
import statusBar from '@/components/StatusBar.vue'

export default {
  data() {
    return {
      landmarks: null,
      checkedLandmark: [],
      courseTitle: "",
      courseDesc: ""
    }
  },
  components: {
    statusBar
  },
  created(){
    this.$getApi('/session/landmark/', {}, (res)=>{
      const editedCourseData = res.data
      const storageRef = firebase.storage().ref()
      const this_ref = this
      let urlCallbackCount = 0

      for(let index = 0; index < editedCourseData.landmarks.length; index++){
        storageRef.child(editedCourseData.landmarks[index].img_path).getDownloadURL().then(function(url) {
          urlCallbackCount++
          editedCourseData.landmarks[index].img_url = url
          if(urlCallbackCount === editedCourseData.landmarks.length){
            this_ref.landmarks = editedCourseData.landmarks
          }
        }).catch(function(error) {
          urlCallbackCount++
          console.log(error)
        })
      }
    })
  },
  methods:{
    changeCheck(id){
      const index = this.checkedLandmark.indexOf(id)
      if(index === -1){
        this.checkedLandmark.push(id)
      }else{
        this.checkedLandmark.splice(index, 1)
      }
      console.log(this.checkedLandmark)
    },
    postToServer(){
      if(this.checkedLandmark.length < 1){
        alert('ランドマークにチェックをつけてください')
        return
      }
      const postData = {
        name: this.courseTitle,
        description: this.courseDesc,
        landmarks: this.checkedLandmark
      }
      console.log(postData)
      this.$postApi('/session/course/', postData, (res)=>{
        if(res.data.result==='OK'){
          alert('登録完了')
        }else{
          alert('登録エラー')
        }
      })
    }
  }
}
</script>

<style lang="scss">
@import "@/assets/scss/modules/_home.scss";
@import "@/assets/scss/base/_variables.scss";

.main {
  background: $white;
  overflow-y: scroll;
}

.button_warapper {
  text-align: center;
}

.landmark_label {
  font-size: 1.5em;
}

.post_course {
  background-color: rgb(65, 195, 255);
  text-align: center;
  border: 1px solid;
  border-radius: 2%;
  border-color: #D62828;
  color: white;
  font-weight: 700;
  font-size: 1.25rem;
  padding: .75rem 0;
  width: 80%;
  margin-bottom: 1rem;
}

.landmark_img {
  margin-left: 5%;
}

#course-desc-text-area{
  width: 90vw;
  height: 150px;
}

#course-title-input{
  width: 90vw;
}
</style>