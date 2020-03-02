<template>
  <div class="home">
    <span>ログイン成功</span>
    <br>
    <button @click="logout">ログアウト</button>
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

export default {
  methods: {
    logout() {
      firebase.auth().signOut().then(function() {
        router.push('/login')
      }).catch(error => {
        console.log(error.message)
        router.push('/login')
      })
    }
  }
}
</script>
