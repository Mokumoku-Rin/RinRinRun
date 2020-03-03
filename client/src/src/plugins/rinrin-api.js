import axios from 'axios'
import firebase from 'firebase/app'

function sendToApi(path,json_input, token) {
  const headers = {
    'X-token': token
  }
  axios.post('http://localhost:8081/'+path , json_input,  {
    headers: headers
  }).then(response => {
    console.log(response)
  }).catch(error => {
    console.log(error)
  })
}

const RinRinApi = {
install (Vue) {
    Vue.prototype.$sendApi = (path, json_input, get_token=true, token=null) => {
      if (get_token) {
        firebase.auth().currentUser.getIdToken(/* forceRefresh */ true).then(function(idToken) {
          sendToApi(path, json_input, idToken)
        }).catch(function(error) {
          console.log('---rinrin-api-plugin-firebase-error-----')
          console.log(error)
          console.log('----------------------------------------')
        })
      }else{
        sendToApi(path, json_input, token)
      }
    }
  }
}
  
export default RinRinApi