<template>
  <div class="home">
    <statusBar left-link="/search-course" :center="page_info.title"></statusBar>
    <main>
      <ul class="search_course_list">
        <li class="search_course_item" v-for="data in course_data" :key="data.id" v-show="!page_info.loading">
          <router-link class="search_course_link" :to="{ path: '/course-info', query: { search_type: page_info.search_type, course_id: data.id } }">
            <div class="search_course_content">
              <h2 class="search_course_name">{{data.name}}</h2>
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
@import "@/assets/scss/modules/_home.scss";

.search_course_list {
  height: 100%;
  background: $white;
  overflow-y: scroll;
  color: $black;

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

.search_course_name {
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
      page_info: {
        title: '',
        search_type: '',
        loading: true,
        course: 0
      },
      course_data: [
        {id: '0', name: 'タイトル1', description: 'hogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehoge'},
        {id: '1', name: 'タイトル1', description: 'hogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehoge'},
        {id: '2', name: 'タイトル1', description: 'hogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehoge'},
        {id: '3', name: 'タイトル1', description: 'hogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehoge'},
        {id: '4', name: 'タイトル1', description: 'hogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehoge'},
        {id: '5', name: 'タイトル1', description: 'hogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehoge'},
        {id: '6', name: 'タイトル1', description: 'hogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehoge'},
        {id: '7', name: 'タイトル1', description: 'hogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehoge'},
        {id: '8', name: 'タイトル1', description: 'hogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehoge'},
        {id: '9', name: 'タイトル1', description: 'hogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehoge'},
        {id: '10', name: 'タイトル1', description: 'hogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehoge'},
        {id: '11', name: 'タイトル1', description: 'hogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehoge'},
        {id: '12', name: 'タイトル1', description: 'hogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehoge'},
        {id: '13', name: 'タイトル1', description: 'hogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehoge'},
        {id: '14', name: 'タイトル1', description: 'hogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehoge'},
        {id: '15', name: 'タイトル1', description: 'hogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehoge'},
        {id: '16', name: 'タイトル1', description: 'hogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehoge'},
      ]
    }
  },
  mounted() {
    this.page_info.search_type = this.$route.query.search_type
    if(this.page_info.search_type=="popular") {
      this.page_info.title = "人気のコース"
      // 人気のコース情報を取得するコード
    } else if(this.page_info.search_type=="latest") {
      this.page_info.title = "最新のコース"
      // 最新のコース情報を取得するコード
    } else {
      this.page_info.title = "error: no queries"
    }

    this.$getApi('/session/course/', {sort_by: this.type, limit: 10}, (res)=>{
      if(res.data.courses.length > 0){
        this.course_data = res.data.courses
      }
      this.page_info.loading = false
    })
  },
  components: {
    statusBar
  }
}
</script>
