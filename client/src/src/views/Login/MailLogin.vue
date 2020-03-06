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
        firebase.auth().currentUser.getIdToken(/* forceRefresh */ true).then(function(idToken) {
          sendLoginRequest(idToken)
        })
        router.push('/')
      }).catch(error => {
        console.log(error)
        this.errorMessage = error.message
        this.showError = true
      })
    }
  }
}

function sendLoginRequest(token) {
  const API_URL = 'http://localhost:8081'
  const ENDPOINT = "/login"

  axios.post(API_URL + ENDPOINT, {
    token: token,
    img_url: "",
    name: ""
  }).then(response => {
    if (response.status !== 200) {
      throw Error("Login failed by reason:" + response.data)
    }
  }).catch(e => {
    throw Error(e.message)
  })
}
</script>
