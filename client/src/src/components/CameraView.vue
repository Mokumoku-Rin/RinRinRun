<template>
  <section id="camera-view">
    <div id="overlay-wrapper">
      <video
        ref="video"
        id="src-video"
        :width="width"
        :height="height"
        playsinline
      ></video>

      <canvas ref="overlay" id="overlay-canvas" :width="width" :height="height"></canvas>
    </div>
    <button @click=takePhoto>写真をとる！</button>
    <canvas ref="takedPhotoCanvas" id="taked-ptoto-canvas" :width="width" :height="height"></canvas>
  </section>
</template>

<script>
export default {
  props:{
    landmarkImgUrl: {
      type: String,
      required: true
    },
    width: {
      type: Number,
      default: 400
    },
    height: {
      type: Number,
      default: 400
    }
  },
  data() {
    return {
      video: {},
      takedPhotoCanvas: {}
    };
  },
  mounted: async function() {
    // setup img canvas
    const overLayContext = this.$refs.overlay.getContext('2d')
    const overLayImage = new Image()
    overLayImage.src = this.landmarkImgUrl
    overLayImage.width = this.width
    overLayImage.height = this.height

    overLayImage.addEventListener('load', function() {
        overLayContext.drawImage(overLayImage, 0, 0, this.width, this.height)
    }, false)


    // setup video
    this.video = this.$refs.video;
    const userAgent = navigator.userAgent.toLowerCase();
    const stream = await getVideoStream(userAgent);
    this.video.srcObject = stream;
    this.video.play();
  },
  methods: {
    takePhoto(){
      this.takedPhotoCanvas = this.$refs.takedPhotoCanvas
      const canvasContext = this.takedPhotoCanvas.getContext('2d')
      canvasContext.drawImage(this.video, 0, 0)
      const imgData = this.takedPhotoCanvas.toDataURL('image/png')
      console.log(imgData);
      console.log('take photo')

      // TODO: コースのidとランドマークのidをちゃんとしたものにする
      const postData = {
        landmark_id: 1,
        course_id: 1,
        img: imgData.replace(/^.*,/, '') // data:image/png;base64, がサーバー側で不要なため消す
      }
      this.$postApi('/session/landmark/visit/', postData)

    },
    imgCaertification(responce){
      // TODO 認証結果を利用したその後の処理
      console.log(responce)
    }
  }
};


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
  pointer-events: none;
  opacity:0.3;
}

#overlay-wrapper{
  position: relative;
}

#taked-ptoto-canvas{
  display: none;
}
</style>
