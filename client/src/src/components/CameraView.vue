<template>
  <section id="camera-view">
    <div id="overlay-wrapper">
      <video
        ref="video"
        id="src-video"
        playsinline
      ></video>

      <canvas ref="overlay" id="overlay-canvas" height="1024" width="1024"></canvas>
    </div>
    <!-- <button @click=takePhoto>写真をとる！</button> -->
    <canvas ref="takedPhotoCanvas" id="taked-ptoto-canvas"></canvas>
  </section>
</template>

<script>
import router from '@/router'
import Compressor from "compressorjs"

export default {
  props:{
    landmarkID: {
      type: Number,
      required: true
    },
    courseID: {
      type: Number,
      required: true
    },
    searchType: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      video: {},
      takedPhotoCanvas: {},
      videoStream: null,
    };
  },
  mounted: async function() {
    const overLayContext = this.$refs.overlay.getContext('2d')
    const overLayImage = new Image()

    // findがうまく動作しないため
    
    for(const landmark of this.$store.state.runnigCourseData.landmarks){
      if(parseInt(landmark.id)  == this.landmarkID){
        overLayImage.src = landmark.img_url
        overLayContext.drawImage(overLayImage,0, 0, 512, 512)
        break
      }
    }

    // setup video
    this.video = this.$refs.video;
    const userAgent = navigator.userAgent.toLowerCase();
    this.videoStream = await getVideoStream(userAgent);
    this.video.srcObject = this.videoStream;
    this.video.play();
  },
  methods: {
    takePhoto(){
      this.takedPhotoCanvas = this.$refs.takedPhotoCanvas
      const canvasContext = this.takedPhotoCanvas.getContext('2d')
      canvasContext.drawImage(this.video, 0, 0, 512, 512)
      const imgData = this.takedPhotoCanvas.toDataURL('image/jpeg', 0.65)
      console.log('take photo')

      const postData = {
        landmark_id: this.landmarkID,
        course_id: this.courseID,
        img: imgData.replace(/^.*,/, '') // data:image/png;base64, がサーバー側で不要なため消す
      }
      this.$postApi('/session/landmark/visit/', postData, this.imgCaertification)

    },
    imgCaertification(responce){
      // ここに実装書くの良くないので時間あれば直す
      if(responce.data.result === 'OK'){
        if(this.$store.state.isRunning === false){
          this.$store.commit('clearMyLandmarkVisits')
          this.$store.commit('resetMyRunStartTime')
        }
        const tempDate = new Date()
        const elapsedTime = tempDate.getTime() - this.$store.state.myRunStartTime
        this.$store.commit('addMyRunCheckedLandmarkID', this.landmarkID)
        this.$store.commit('addMyLandmarkVisits', {id:this.landmarkID, time:elapsedTime})

        // before destoryが呼ばれないときがあるみたいなので一応
        this.videoStream.getTracks().forEach(track => track.stop())
        if(this.$store.state.myLandmarkVisits.length === this.$store.state.runnigCourseData.landmarks.length){
          //ゴールノーページへ
          router.push('/running-goal')
        }else{
          router.push({ path: '/running-info', query: { search_type: this.searchType, course_id: this.courseID } })
        }
      }
      console.log(responce.data.result)
    }
  },
  beforeDestroy: function () {
    this.videoStream.getTracks().forEach(track => track.stop())
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
        aspectRatio: {exact: 1}
      }
    };
  } else {
    medias = {
      audio: false,
      video: {
        aspectRatio: {exact: 1}
      }
    };
  }

  const videoStream = await navigator.mediaDevices.getUserMedia(medias);

  return videoStream;
}
</script>

<style scoped>
#overlay-canvas{
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
  pointer-events: none;
  opacity: 0.4;
  z-index: 1;
}

#overlay-wrapper{
  position: relative;
  height: 100%;
  width: 100%
}

#taked-ptoto-canvas{
  display: none;
}
</style>
