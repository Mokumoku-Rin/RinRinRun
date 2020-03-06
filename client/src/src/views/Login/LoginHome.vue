<template>
  <div class="container">
    <div class="row">
      <div class="col-md-12">
        <h2>ログイン画面</h2>
        <div class="mt-2"><button block variant="primary" @click="googleLogin">Google ログイン</button></div>
      </div>
      <router-link to="/mail-login">メールアドレスでログイン</router-link><br>
      <router-link to="/mail-register">メールアドレスで登録</router-link>
      <CameraView></CameraView>
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
import axios from 'axios'
import router from '@/router'
import CameraView from "@/components/CameraView"

export default {
  components: {
    CameraView,
  },
  methods: {
    googleLogin() {
      const provider = new firebase.auth.GoogleAuthProvider()

      firebase.auth().signInWithPopup(provider).then(() => {
        firebase.auth().currentUser.getIdToken(/* forceRefresh */ true).then(function(idToken) {
          firebase.auth().currentUser.providerData.forEach(function (profile) {
            sendLoginRequest(idToken, profile.displayName, profile.photoURL)
          })
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

function sendLoginRequest(token, userName, photoURL) {
  const API_URL = 'http://localhost:8081'
  const ENDPOINT = "/login"
  axios.post(API_URL + ENDPOINT, {
    token: token,
    img_url: photoURL,
    name: userName
  }).then(response => {
    if (response.status !== 200) {
      throw Error("Login failed by reason:" + response.data)
    }
  }).catch(e => {
    throw Error(e.message)
  })
}
</script>
