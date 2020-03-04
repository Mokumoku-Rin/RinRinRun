<template>
  <div>
    this is mail login page<br>
    <input v-model="email" type="text" placeholder="メールアドレス" /> <br>
    <input v-model="password" type="text" placeholder="パスワード" /><br>
    <button block variant="primary" @click="emailLogin">ログイン</button><br>
    <span v-show="showError" dismissible variant="danger">{{ errorMessage }}</span><br>
    <router-link to="/forget-password">パスワードを忘れましたか？</router-link>
  </div>
</template>

<script>
import firebase from 'firebase/app'
import router from '@/router'

export default {
  data() {
    return {
      email: '',
      password: '',
      errorMessage: '',
      showError: false
    }
  },  
  methods: {
    emailLogin() {
      firebase.auth().signInWithEmailAndPassword(this.email, this.password).then(result => {
        console.log(result)
        router.push('/')
      }).catch(error => {
        console.log(error)
        this.errorMessage = error.message
        this.showError = true
      })
    }
  }
}
</script>
