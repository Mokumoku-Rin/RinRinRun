<template>
  <div class="home">
    <statusBar left-link="/search-course" :center="pageTitle"></statusBar>
    <main>
      <ul class="search_course_list">
        <li class="search_course_item" v-for="data in courseData" :key="data.id">
          <router-link class="search_course_link" :to="{ path: '/running-info', query: { id: data.id } }">
            <div class="search_course_content">
              <h2 class="search_course_title">{{data.title}}</h2>
              <p class="search_course_description">{{data.description}}</p>
            </div>
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
  padding: 1.25rem 1.5rem;

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
  width: 100%;
}

.search_course_content {
  line-height: 1.5;
  flex-grow: 1;
  width: 80%;
}

.search_course_title {
  margin-bottom: .25rem;
  font-size: 1.5rem;
  font-weight: $weight-bold;
}

.search_course_description {
  height: 3em;
  overflow-wrap: break-word;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
}

.search_course_chevron {
  font-size: 1.25rem;
  flex-grow: 0;
  margin-left: .75rem;
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
        {id: '0', title: 'タイトル1', description: 'hogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehoge'}
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
