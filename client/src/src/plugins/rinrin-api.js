import axios from 'axios'
import firebase from 'firebase/app'

function postToApi(path,jsonInput, token) {
  const headers = {
    headers: {
      'X-Token': token
    }
  }
  axios.post('http://localhost:8081'+path , jsonInput, headers)
  // .then(response => {
  //   console.log(response)
  // })
  .catch(error => {
    console.log('---rinrin-api-plugin-$postApi--postToApi-error-----')
    console.log(error)
    console.log('--------------------------------------------------')
  })
}

function getToApi(path,jsonInput, token) {
  const headers = {
    headers: {
      'X-Token': token
    }
  }
  const sendHeaderBody = Object.assign(headers, jsonInput);
  axios.get('http://localhost:8081'+path , sendHeaderBody)
  // .then(response => {
  //   console.log(response)
  // })
  .catch(error => {
    console.log('---rinrin-api-plugin-$getApi--getToApi-error-----')
    console.log(error)
    console.log('-------------------------------------------------')
  })
}

const RinRinApi = {
install (Vue) {
    Vue.prototype.$postApi = (path, jsonInput, getToken=true, token=null) => {
      if (getToken) {
        firebase.auth().currentUser.getIdToken(/* forceRefresh */ true).then(function(idToken) {
          postToApi(path, jsonInput, idToken)
        }).catch(function(error) {
          console.log('---rinrin-api-plugin-$postApi--firebase-error-----')
          console.log(error)
          console.log('--------------------------------------------------')
        })
      }else{
        postToApi(path, jsonInput, token)
      }
    }

    Vue.prototype.$getApi = (path, jsonInput, getToken=true, token=null) => {
      if (getToken) {
        firebase.auth().currentUser.getIdToken(/* forceRefresh */ true).then(function(idToken) {
          getToApi(path, jsonInput, idToken)
        }).catch(function(error) {
          console.log('---rinrin-api-plugin-$getApi--firebase-error-----')
          console.log(error)
          console.log('-------------------------------------------------')
        })
      }else{
        getToApi(path, jsonInput, token)
      }
    }
  }
}
  
export default RinRinApi