<template>
  <!-- <div class="container">
    <div class="row">
      <div class="col-md-12">
        <h2>ログイン画面</h2>
        <div class="mt-2"><button block variant="primary" @click="googleLogin">Google ログイン</button></div>
      </div>
      <router-link to="/mail-login">メールアドレスでログイン</router-link><br>
      <router-link to="/mail-register">メールアドレスで登録</router-link>
      <CameraView></CameraView>
    </div>
  </div> -->
  <div class="section login_home">
    <header>
      <h1 class="title">
        <img src="@/assets/img/logo.svg" alt="かけだせSOJOの森">
      </h1>
      <div class="subtitle">Update Orienteering!</div>
    </header>
    <nav>
      <Button :func="googleLogin" :icon="['fab', 'google']" label="Googleアカウントで続ける"></Button>
    </nav>
  </div>
</template>

<style lang="scss">
@import "@/assets/scss/base/_variables.scss";

.login_home {
  position: absolute;
  margin: auto;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;

  display: flex;
  flex-direction: column;
  overflow: hidden;
  height: 100vh;
  width: 100%;
  justify-content: space-around;
  color: $white;
  background-color: rgba(0, 0, 0, 0);

  header, nav {
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
  }
  .title, .subtitle {
    color: $white;
    text-align: center;
  }
  .title {
    margin-bottom: 1.25rem;
  }
  .subtitle {
    font-size: 1.5rem;
  }
  .button_wrapper+.button_wrapper {
      margin-top: 1rem;
  }
  .button {
    font-size: 1rem;
  }
}
</style>

<script>
import firebase from 'firebase/app'
import router from '@/router'

import Button from '@/components/Button.vue'

export default {
  components: {
    Button
  },
  methods: {
    async googleLogin() {
      const provider = new firebase.auth.GoogleAuthProvider()

      try {
        const userCred = await firebase.auth().signInWithPopup(provider)

        this.$postApi('/login', {
          token: await userCred.user.getIdToken(true),
          img_url: userCred.user.photoURL,
          name: userCred.user.displayName
        })
        router.push('/')
      } catch (error) {
        console.log(error)
        alert(error)
      }
    }
  }
}
</script>
