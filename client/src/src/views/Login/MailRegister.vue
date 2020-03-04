<template>
  <div>
    <h1>this is mail register page</h1>
    <h2>Sign up</h2>
    <input type="text" placeholder="Username" v-model="username"><br>
    <input type="password" placeholder="Password" v-model="password"><br>
    <button @click="signUp">Register</button><br>
    <p>Do you have an account? 
      <router-link to="/login-home">sign in now!!</router-link>
    </p>
  </div>
</template>

<script>
import firebase from 'firebase'
import router from '@/router'

export default {
  data () {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    signUp: function () {
      firebase.auth().createUserWithEmailAndPassword(this.username, this.password)
        .then(user => {
          alert('Create account: ', user.email)
          router.push('/')
        })
        .catch(error => {
          alert(error.message)
        })
    }
  }
}
</script>
