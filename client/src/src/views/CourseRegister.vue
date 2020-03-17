<template>
<div class="home">
  <div id="root">
    <div v-for="landmark of landmarks"  v-bind:key="landmark.id">
      <input type="checkbox" @change="changeCheck(landmark.id)">
      <span style="font-size: 1.5em;">{{ landmark.name }}</span><br>
      <p>{{ landmark.description }}</p>
      <img :src="landmark.img_url" :alt="landmark.name" style="height: 200px;">
      <hr>
    </div>
    <hr>
    <p>登録情報</p>
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
    <button @click="postToServer">サーバに投稿</button>
  </div>
</div>
</template>

<script>
import firebase from 'firebase/app'

export default {
  data() {
    return {
      landmarks: null,
      checkedLandmark: [],
      courseTitle: "",
      courseDesc: ""
    }
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

#root{
  overflow: auto; 
  height: 100%;
}

#course-desc-text-area{
  width: 90vw;
  height: 150px;
}

#course-title-input{
  width: 90vw;
}
</style>