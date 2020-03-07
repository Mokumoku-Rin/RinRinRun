<template>
  <div class="login_mail">
    <statusBar left-link="login-home"></statusBar>
    <main class="section">
      <h1 class="title">メールアドレスでログイン</h1>
      <p class="error" v-show="showError" dismissible variant="danger">{{ errorMessage }}</p>
      <div class="control has-icons-left">
        <input class="input is-medium" v-model="email" type="email" placeholder="メールアドレス" />
        <span class="icon is-left is-medium">
          <font-awesome-icon icon="envelope"></font-awesome-icon>
        </span>
      </div>
      <div class="control has-icons-left">
        <input class="input is-medium" v-model="password" type="password" placeholder="パスワード" /><br>
        <span class="icon is-left is-medium">
          <font-awesome-icon icon="key"></font-awesome-icon>
        </span>
      </div>
      <a class="button" @click="emailLogin">ログイン</a>
      <router-link class="forget" to="/forget-password">パスワードを忘れましたか？</router-link>
    </main>
  </div>
</template>

<style lang="scss">
@import "@/assets/scss/base/_variables.scss";
@import "@/assets/scss/modules/_button.scss";

.login_mail {
  overflow-y: hidden;
  height: 100vh;
  width: 100%;
  justify-content: space-around;
  color: $white;

  .navbar {
    background: transparent;
    padding: .75rem 1.5rem;
    font-size: 1.75rem;
    a {
      color: $white;
    }
  }

  .section {
    padding-top: 1rem;
  }

  .title {
    color: $white;
    font-size: 1.5rem;
    text-align: center;
  }

  .control {
    margin-top: 1rem;
  }

  .button {
    margin-top: 1.5rem;
  }

  .error {
    text-align: center;
    color: $red;
    font-size: 1.2rem;
    margin: 1rem 0;
  }

  .forget {
    display: block;
    margin-top: 1rem;
    color: $white;
    text-align: center;
    font-weight: $weight-bold;
  }
}
</style>

<script>
import firebase from 'firebase/app'
import router from '@/router'

import statusBar from '@/components/StatusBar.vue'

export default {
  components: {
    statusBar
  },
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
        this.errorMessage = "認証できませんでした。"
        this.showError = true
      })
    },
    backHome() {
      router.push('login-home')
    }
  }
}
</script>
