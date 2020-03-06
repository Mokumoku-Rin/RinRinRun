<template>
  <section id="camera-view">
    <div>
      <video
        ref="video"
        id="video"
        width="400"
        height="600"
        playsinline
      ></video>
    </div>
    <canvas ref="canvas" id="canvas" width="400" height="600" disabled></canvas>
  </section>
</template>

<script>
export default {
  data() {
    return {
      video: {},
      canvas: {},
      interval: null
    };
  },
  mounted: async function() {
    // setup video
    this.video = this.$refs.video;
    const userAgent = navigator.userAgent.toLowerCase();
    const stream = await getVideoStream(userAgent);
    this.video.srcObject = stream;
    this.video.play();

    // setup capture interval
    const interval = 1000; //1000ms is 1sec
    this.interval = setInterval(() => {
      this.capture();
    }, interval);
  },
  destroyed: async function() {
    clearInterval(this.interval);
  },
  methods: {
    capture: function() {
      // this.captures.pop()
      this.canvas = this.$refs.canvas;
      const imgData = this.canvas.toDataURL("image/png");
      // TODO: 画像データから類似度を取る
      console.log(imgData);
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
        }
      }
    };
  } else {
    medias = {
      audio: false,
      video: true
    };
  }

  const videoStream = await navigator.mediaDevices.getUserMedia(medias);

  return videoStream;
}
</script>
