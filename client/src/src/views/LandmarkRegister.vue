<template>
<div class="home">
  <statusBar center="ランドマークの登録"></statusBar>
  <main class="main">
    <video ref="video" id="src-video" playsinline />
    <div class="button_warapper">
      <button class="take_photo" @click="takePhoto">写真を撮る</button>
    </div>
    <p>画像</p>
    <canvas ref="takedPhotoCanvas" id="taked-ptoto-canvas"></canvas>
    <p>座標</p>
    <p>{{ location }}</p>
    <p>ランドマーク名</p>
    <input v-model="landmarkTitle" id="landmark-title-input"/>
    <p>ランドマークの説明</p>
    <textarea v-model="landmarkDesc" id="landmark-desc-text-area"/>
    <hr>
    <div class="button_warapper">
      <button class="post_photo" @click="postToServer">サーバに投稿</button>
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
      video: {},
      takedPhotoCanvas: {},
      videoStream: null,
      landmarkTitle:'',
      landmarkDesc: '',
      gpsTimerObj: null,
      location: 'not set'
    }
  },
  components: {
    statusBar
  },
  methods: {
    takePhoto(){
      this.takedPhotoCanvas = this.$refs.takedPhotoCanvas
      const canvasContext = this.takedPhotoCanvas.getContext('2d')
      this.takedPhotoCanvas.width = 512
      this.takedPhotoCanvas.height = 512

      canvasContext.drawImage(this.video, 0,0)
    },
    postToServer(){
      if(!this.takedPhotoCanvas){
        alert('画像がありません')
        return
      }

      const fileName = generateUuid()
      const childName = fileName + '.jpg'

      const this_ref = this // コールバックの中でthisがvueインスタンスを指さなくなるため

      this.takedPhotoCanvas.toBlob(function(blob){
        const storageRef = firebase.storage().ref()
        storageRef.child(childName).put(blob).then( () => {
          const postData = {
            name: this_ref.landmarkTitle,
            description: this_ref.landmarkDesc,
            img_path: fileName + '.jpg',
            pos: this_ref.location[0] + ',' + this_ref.location[1]
          }
          console.log(postData)
          this_ref.$postApi('/session/landmark/', postData, (res)=>{
            if(res.data.result==='OK'){
              alert('登録完了')
            }else{
              alert('登録エラー')
            }
          })
        }).catch(error => {
          console.log(error)
        })
      }, "image/jpeg", 0.90) // jpeg 90% quarity
    },
    gpsIntervalFunc(){
      navigator.geolocation.getCurrentPosition(this.successGetGPS, (error)=>{console.log('gps error',error.code)})
    },
    successGetGPS(position){
      this.location = [position.coords.latitude, position.coords.longitude]
      console.log('success')
    },
  },
  mounted: async function() {
    this.gpsIntervalFunc()
    this.gpsTimerObj = setInterval(this.gpsIntervalFunc, 5000)

    this.video = this.$refs.video;
    const userAgent = navigator.userAgent.toLowerCase();
    this.videoStream = await getVideoStream(userAgent);
    this.video.srcObject = this.videoStream;
    this.video.play();
  },
  beforeDestroy: function () {
    this.videoStream.getTracks().forEach(track => track.stop())
    clearInterval(this.gpsTimerObj)
  }
}

async function getVideoStream(userAgent) {
  const ua = userAgent.toLowerCase();
  let medias = {};

  // For iPhone support
  if (ua.includes("iphone")) {
    medias = {
      audio: false,
      video: {
        facingMode: {
          exact: "environment"
        },
        aspectRatio: {exact: 1},
        width: 512
      }
    };
  } else {
    medias = {
      audio: false,
      video: {
        aspectRatio: {exact: 1},
        width: 512
      }
    };
  }

  const videoStream = await navigator.mediaDevices.getUserMedia(medias);

  return videoStream;
}

function generateUuid() {  
  // https://github.com/GoogleChrome/chrome-platform-analytics/blob/master/src/internal/identifier.js  
  // const FORMAT: string = "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx";  
  let chars = "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".split("");  
  for (let i = 0, len = chars.length; i < len; i++) {  
    switch (chars[i]) {  
      case "x":  
        chars[i] = Math.floor(Math.random() * 16).toString(16);  
        break;  
      case "y":  
        chars[i] = (Math.floor(Math.random() * 4) + 8).toString(16);  
        break;  
    }  
  }  
  return chars.join("");  
} 
</script>

<style lang="scss">
@import "@/assets/scss/base/_variables.scss";
@import "@/assets/scss/modules/_home.scss";

.main {
  background: $white;
  overflow-y: scroll;
}

.button_warapper {
  text-align: center;
}

.take_photo {
  background-color: #D62828;
  text-align: center;
  border: 1px solid;
  border-radius: 2%;
  border-color: #D62828;
  color: white;
  font-weight: 700;
  font-size: 1.25rem;
  padding: .75rem 0;
  width: 80%;
}

.post_photo {
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

#taked-ptoto-canvas{
  height: 512px;
  width: 512px;
  border: 1px solid black;
}

#landmark-desc-text-area{
  width: 90vw;
  height: 150px;
}

#landmark-title-input{
  width: 90vw;
}
</style>