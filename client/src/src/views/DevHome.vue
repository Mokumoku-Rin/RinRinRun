<template>
  <div class="home">
    <span>ログイン成功</span>
    <br>
    <button @click="logout">ログアウト</button>
    <hr>
    <showAllRoute/>
    <hr>
    <apiTest/>
    <hr>
    <!-- <rinRinMap/> -->
    <!-- <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/> -->
  </div>
</template>

<script>
// // @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

// export default {
//   name: 'Home',
//   components: {
//     HelloWorld
//   }
// }
import firebase from 'firebase/app'
import router from '../router'

import apiTest from '@/components/devtools/ApiTest.vue'
import showAllRoute from '@/components/devtools/ShowAllRoute.vue'
// import rinRinMap from '@/components/RinRinMap.vue'

export default {
  components: {
    apiTest,
    showAllRoute,
    // rinRinMap
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
