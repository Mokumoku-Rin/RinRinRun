<template>
  <div>
    -----------------------------------------------<br>
    <button @click="postTestButton">post test</button>
  </div>
</template>

<script>
import firebase from 'firebase/app'
import axios from 'axios'

export default {
  methods: {
    postTestButton(){ 
      firebase.auth().currentUser.getIdToken(/* forceRefresh */ true).then(function(idToken) {
        console.log(idToken)
        axios.post('http://localhost:8081/test/', {
          token: idToken,
          name: 'this is test'
        }).then(response => {
          console.log('送信したテキスト: ' + response.data.text);
        }).catch(error => {
          console.log(error);
        })
      }).catch(function(error) {
        // Handle error
        console.log(error)
      })
    }
  }
}
</script>
