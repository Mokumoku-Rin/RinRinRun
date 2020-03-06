<template>
  <div class="login_mail">
    <nav class="navbar">
      <router-link to="login-home">
        <font-awesome-icon icon="chevron-left"></font-awesome-icon>
      </router-link>
    </nav>
    <main class="section">
      <h1 class="title">メールアドレスで登録</h1>
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
      <a class="button" @click="signUp">登録</a>
    </main>
  </div>
</template>

<script>
import firebase from 'firebase'
import router from '@/router'

export default {
  data () {
    return {
      email: '',
      password: '',
      errorMessage: '',
      showError: false
    }
  },
  methods: {
    signUp: function () {
      firebase.auth().createUserWithEmailAndPassword(this.email, this.password)
        .then(user => {
          alert('Create account: ', user.email)
          router.push('/')
        })
        .catch(error => {
          console.log(error)
          this.errorMessage = "登録できませんでした。"
          this.showError = true
        })
    }
  }
}
</script>
