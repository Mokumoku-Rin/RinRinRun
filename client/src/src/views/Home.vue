<template>
  <div class="">
    <span>ログイン成功</span>
    <br>
    <button @click="logout">ログアウト</button>
    <hr>
    <showAllRoute/>
    <hr>
    <apiTest/>
  </div>
</template>

<script>
import firebase from 'firebase/app'
import router from '../router'

import apiTest from '@/components/devtools/ApiTest.vue'
import showAllRoute from '@/components/devtools/ShowAllRoute.vue'

export default {
  components: {
    apiTest,
    showAllRoute
  },
  methods: {
    logout() {
      firebase.auth().signOut().then(function() {
        router.push('/login-home')
      }).catch(error => {
        console.log(error.message)
        router.push('/login-home')
      })
    }
  }
}
</script>
