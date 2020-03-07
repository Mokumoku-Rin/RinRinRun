<template>
  <div>
    adfasf
    <camera-view :landmark-img-url="landmarkImgUrl"/>
    <canvas ref="canvas" id="canvas" width="400" height="600" disabled></canvas>

  </div>
</template>

<script>
import CameraView from '@/components/CameraView.vue'

export default {
  components:{
    CameraView
  },
  data() {
    return {
      landmarkImgUrl: 'https://livedoor.blogimg.jp/boomsports/imgs/4/8/488abd7a.jpg'
    }
  },
  mounted: function(){
    this.canvas = this.$refs.canvas

  }
}
</script>

<style>

</style>