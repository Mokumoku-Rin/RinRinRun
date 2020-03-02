<template>
  <div class="container">
    <div class="row">
      <div class="col-md-12">
        <h2>ログイン画面</h2>
        <div class="mt-2"><input v-model="email" type="text" placeholder="メールアドレス" /></div>
        <div class="mt-2"><input v-model="password" type="text" placeholder="パスワード" /></div>
        <div class="mt-2"><button block variant="primary" @click="emailLogin">ログイン</button></div>
        <div class="mt-2"><button block variant="primary" @click="googleLogin">Google ログイン</button></div>
        <div class="mt-2"><span v-show="showError" dismissible variant="danger">{{ errorMessage }}</span></div>
      </div>
      <router-link to="/register">ユーザ登録</router-link>
    </div>
  </div>
</template>

<style>
.mt-2 {
  margin-top: 2px;
}
</style>

<script>
import firebase from 'firebase/app'
import router from '../router'

export default {
  name: 'login',
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
    },
    googleLogin() {
      const provider = new firebase.auth.GoogleAuthProvider()

      firebase.auth().signInWithPopup(provider).then(result => {
        console.log(result.user)
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
