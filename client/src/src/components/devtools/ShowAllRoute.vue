<template>
  <div>
    This is route test<br>
    <router-link to="/home">HOME</router-link><br>
    <router-link to="/search-course">コース検索</router-link><br>
    <router-link to="/choice-course">コース選択</router-link><br>
    <router-link to="/take-picture">写真をとるページ</router-link><br>
    <router-link to="/run-map-test">ゴースト表示テスト</router-link><br>
    <router-link to="/running-info?course_id=1">ランニング中のページ</router-link><br>
    <router-link to="/running-goal">ゴールしたときのページ</router-link><br>
    <hr>
    <router-link to="/dev/landmark-register">ランドマーク登録ページ</router-link><br>
    <router-link to="/dev/course-register">コース登録ページ</router-link>
  </div>
</template>

<script>
export default {

}
</script>

<style>

</style>
