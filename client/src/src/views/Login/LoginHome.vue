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
      <h1 class="title">RinRinRun</h1>
      <div class="subtitle">壮大な総情の大地を走ろう！</div>
    </header>
    <nav>
      <a class="button" @click="googleLogin">
        <font-awesome-icon :icon="['fab', 'google']"></font-awesome-icon>
        Googleアカウントで続ける
      </a>
      <router-link class="button is-reverse" to="/mail-login">メールアドレスでログイン</router-link>
      <router-link class="button is-reverse" to="/mail-register">メールアドレスで登録</router-link>
    </nav>
  </div>
</template>

<style lang="scss">
@import "@/assets/scss/base/_variables.scss";
@import "@/assets/scss/modules/_button.scss";

.login_home {
  display: flex;
  flex-direction: column;
  overflow-y: hidden;
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
    margin-bottom: 3rem;
  }
  .button+.button {
      margin-top: 1rem;
  }
}


</style>

<script>
import firebase from 'firebase/app'
import router from '@/router'

export default {
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
