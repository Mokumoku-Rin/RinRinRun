<template>
  <div class="home">
    <statusBar left-link="/search-course" :center="pageTitle"></statusBar>
    <main>
      <ul class="search_course_list">
        <li class="search_course_item" v-for="data in courseData" :key="data.id">
          <router-link class="search_course_link" :to="{ path: '/running-info', query: { id: data.id } }">
            <div>{{data.title}}</div>
            <font-awesome-icon class="search_course_chevron" icon="chevron-right"></font-awesome-icon>
          </router-link>
        </li>
      </ul>
    </main>
  </div>
</template>

<style lang="scss">
@import "@/assets/scss/base/_variables.scss";

.home {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100vh;
  overflow-y: hidden;

  main {
    flex-grow: 1;
    height: 100%;
  }
}

.search_course_list {
  height: 100%;
  background: $white;
  overflow-y: auto;
  &::after{
    // リストが最後まで表示されない問題の回避
    content: '';
    display: block;
    height: 3.4rem;
  }
}

.search_course_item {
  padding: 1rem 1.5rem;

  &+.search_course_item {
    border-top: 1px solid $black;
  }
  &:last-child {
    border-bottom: 1px solid $black;
  }
}

.search_course_link {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.search_course_chevron {
  height: 100%;
  color: $red;
}
</style>

<script>
import statusBar from '@/components/StatusBar.vue'

export default {
  data() {
    return {
      pageTitle: '',
      courseData: [
        // {id: '0', title: 'タイトル1'}
      ]
    }
  },
  created() {
    var type = this.$route.query.type
    if(type=="popular") {
      this.pageTitle = "人気のコース"
      // 人気のコース情報を取得するコード
    } else if(type=="latest") {
      this.pageTitle = "最新のコース"
      // 最新のコース情報を取得するコード
    } else {
      this.pageTitle = "error: no queries"
    }
  },
  components: {
    statusBar
  }
}
</script>
