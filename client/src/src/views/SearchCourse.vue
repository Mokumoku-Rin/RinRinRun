<template>
  <div class="home">
    <statusBar leftLink="home" center="コースの検索"></statusBar>
    <main>
      <div class="search_course section">
        <router-link class="search_course_card card" :to="{ path: '/choice-course', params: { type: 'popular' } }" >
          <div class="card-content">
            <h2 class="search_course_card_title">人気のコース</h2>
            <p class="serach_course_card_description">人気のコースから選択</p>
            <img class="search_course_card_img" src="@/assets/img/office-best-achiever.svg" alt="office best achiever">
          </div>
        </router-link>
        <router-link class="search_course_card card" :to="{ path: '/choice-course', params: { type: 'latest' } }" >
          <div class="card-content">
            <h2 class="search_course_card_title">最新のコース</h2>
            <p class="serach_course_card_description">最新のコースから選択</p>
            <img class="search_course_card_img" src="@/assets/img/idea.svg" alt="office best achiever">
          </div>
        </router-link>
      </div>
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

.search_course {
  display: flex;
  background: $white;
  flex-direction: column;
  justify-content: center;
  height: 100%;

  &.section {
    padding-top: 0;
    padding-bottom: 0;
  }
}

.search_course_card {
  display: block;
  border: 1px solid $glay;
  border-radius: 2%;

  &+.search_course_card {
    margin-top: 2.5vh;
  }
}

.card-content {
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  line-height: 1.75;
}

.search_course_card_title {
  font-size: 1.5rem;
  color: $red;
  font-weight: $weight-bold;
}

.search_course_card_discription {
  font-size: 1rem;
}

.search_course_card_img {
  width: 50%;
  margin: 0.5rem auto 0 auto;
  max-height: 20vh;
}
</style>

<script>
import statusBar from '@/components/StatusBar.vue'

export default {
  components: {
    statusBar
  }
}
</script>
