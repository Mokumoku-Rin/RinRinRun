<template>
  <div class="home">
    <statusBar :center="page_info.title" :left-link="{path: '/course-info', query: {search_type: page_info.search_type, course_id: page_info.course_id } }"></statusBar>
    <main>
      <div class="take_picture">
        <div class="take_picture_img_wrapper">
          <img class="take_picture_img" :src="landmark_info.img_url" :alt="landmark_info.name">
        </div>
        <div class="take_picture_camera">
          <camera-view class="take_picture_camera_view" ref="camera" :landmark-img-url="landmark_info.img_url"/>
          <canvas class="take_picture_canvas" ref="canvas" id="canvas" disabled></canvas>
        </div>
      </div>
    </main>
    <cameraButton :func="takePhoto" :active="page_info.active_button"></cameraButton>
    <collation :active="page_info.active_collation"></collation>
  </div>
</template>

<style lang="scss">
@import "@/assets/scss/base/_variables.scss";
@import "@/assets/scss/modules/_home.scss";

.take_picture {
  position: relative;
  background: $white;
  width: 100%;
  height: calc(100% - 4.5rem);
  overflow-y: scroll;
}

.take_picture_img_wrapper {
  position: absolute;
  top: 2rem;
  left: 0.5rem;
  width: 40vw;
  overflow: hidden;
  border: 1px solid $black;
  border-radius: 5%;
  z-index: 2;
  &::before {
    content: "";
    display: block;
    padding-top: 100%;
  }
}

.take_picture_img {
  position: absolute;
  height: 100%;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 0;
}

.take_picture_camera {
  position: absolute;
  top: 10rem;
  left: 1rem;
  width: calc(100% - 2rem);
  border: 1px solid $black;
  border-radius: 2%;

  &::before {
    content: "";
    display: block;
    padding-top: 100%;
  }
}

.take_picture_camera_view {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.take_picture_canvas {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
</style>

<script>
import statusBar from '@/components/StatusBar.vue'
import cameraButton from '@/components/CameraButton.vue'
import collation from '@/components/Collation.vue'
import CameraView from '@/components/CameraView.vue'

export default {
  components:{
    statusBar,
    cameraButton,
    collation,
    CameraView
  },
  data() {
    return {
      canvas: null,
      page_info: {
        title: '',
        search_type: '',  // コースの検索手法の記録
        course_id: 0,  // コース番号の記録
        landmark_id: 0,  // 撮影する写真のid
        active_button: true,  // 撮影が開始できるか
        active_collation: false  // 照合中の画面を表示するか
      },
      landmark_info: {
        id: 0,
        name: 'ランドマークテスト1',
        position: [0, 0],
        img_url: 'https://livedoor.blogimg.jp/boomsports/imgs/4/8/488abd7a.jpg'
      }
    }
  },
  created() {
    this.landmark_info.id = this.$route.query.landmark_id
    // idから情報を取得するコード
    this.page_info.search_type = this.$route.query.search_type
    this.page_info.course_id = this.$route.query.course_id
    this.page_info.title = this.landmark_info.name + 'の撮影'
  },
  mounted: function(){
    this.canvas = this.$refs.canvas

  },
  methods: {
    takePhoto() {
      this.$refs.camera.takePhoto()
    }
  }
}
</script>
