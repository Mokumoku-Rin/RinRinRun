<template>
  <div class="running">
  </div>
</template>

<style lang="scss">
@import "@/assets/scss/base/_variables.scss";


</style>

<script>
// import statusBar from '@/components/StatusBar.vue'

export default {
  data() {
    return {
      pageTitle: '',
      courseData: [
        {title: 'タイトル', param: ''}
      ]
    }
  },
  created() {
    // var type = this.$route.query.type
  },
  components: {
    // statusBar
  }
}
</script>
