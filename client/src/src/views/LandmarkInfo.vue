<template>
  <div class="home">
    <statusBar :center="page_info.title" :left-link="{path: '/course-info', query: { search_type: page_info.search_type, course_id: this.page_info.course_id }}"></statusBar>
    <main>
      <article class="landmark_info section">
        <img class="landmark_info_img" :src="landmark_info.img_url" :alt="landmark_info.name">
        <h2 class="landmark_info_title">説明</h2>
        <p class="landmark_info_description">{{landmark_info.description}}</p>
      </article>
    </main>
  </div>
</template>

<style lang="scss">
@import "@/assets/scss/base/_variables.scss";
@import "@/assets/scss/modules/_home.scss";

.landmark_info {
  height: 100%;
  background: $white;
  overflow-y: scroll;
  line-height: 1.75;
  padding-top: 1.5rem;
  padding-bottom: 1.5rem;

  &::after {
    // リストが最後まで表示されない問題の回避
    content: '';
    display: block;
    height: 3.4rem;
  }
}

.landmark_info_img {
  border: 1px solid $black;
  border-radius: 2%;
}

.landmark_info_title {
  margin-top: .5rem;
  font-size: 1.75rem;
  font-weight: $weight-bold;
}
</style>

<script>
import statusBar from '@/components/StatusBar.vue'
import testImage from '@/assets/img/jogging.svg'

export default {
  data() {
    return {
      page_info: {
        title: '',
        search_type: '',  // コースの検索手法の記録
        course_id: 0,  // コース番号の記録
        landmark_id: 0,  // 表示している写真のランドマークid
      },
      landmark_info: {
        id: 0,
        name: 'ランドマークテスト1aaaaaq',
        pos: [0, 0],
        img_url: testImage,
        description: '説明説明説明説明説明説明説明説明説明説明説明説明説明説明説明説明説明説明説明説明説明説明説明説明説明説明説明説明説明説明説明説明説明説明説明説明説明説明説明説明説明説明説明説明説明説明説明説明説明説明'
      }
    }
  },
  components: {
    statusBar
  },
  created() {
    for(const landmark of this.$store.state.runningCourseData.landmarks){
      if(landmark.id === this.$route.query.landmark_id){
        this.landmark_info = landmark
        break
      }
    }
    // 画面描写に使う情報の取得
    this.page_info.title = this.landmark_info.name
    this.page_info.search_type = this.$route.query.search_type
    this.page_info.course_id = this.$route.query.course_id
    this.page_info.landmark_id = this.$route.query.landmark_id
  }
}
</script>
