import axios from 'axios'
import firebase from 'firebase/app'

const API_ENDPOINT = process.env["API_ENDPOINT"]

function postApiErrorDefaultFunc(error){
  console.log('---rinrin-api-plugin-$postApi--postToApi-error-----')
  console.log(error)
  console.log('--------------------------------------------------')
}

function getApiErrorDefaultFunc(error){
  console.log('---rinrin-api-plugin-$getApi--getToApi-error-----')
  console.log(error)
  console.log('-------------------------------------------------')
}

function postToApi(path,jsonInput, token, successFunc, errorFunc) {
  const headers = {
    headers: {
      'X-Token': token
    }
  }
  axios.post(API_ENDPOINT+path , jsonInput, headers)
  .then(successFunc)
  .catch(errorFunc)
}

function getToApi(path,jsonInput, token, successFunc, errorFunc) {
  const headers = {
    headers: {
      'X-Token': 1
    }
  }
  const sendHeaderBody = Object.assign(headers, jsonInput);
  axios.get(API_ENDPOINT+path , sendHeaderBody)
  .then(successFunc)
  .catch(errorFunc)
}

const RinRinApi = {
install (Vue) {
    Vue.prototype.$postApi = (path, jsonInput, successFunc=()=>{}, errorFunc=postApiErrorDefaultFunc, getToken=true, token=null) => {
      if (getToken) {
        firebase.auth().currentUser.getIdToken(/* forceRefresh */ true).then(function(idToken) {
          postToApi(path, jsonInput, idToken, successFunc, errorFunc)
        }).catch(function(error) {
          console.log('---rinrin-api-plugin-$postApi--firebase-error-----')
          console.log(error)
          console.log('--------------------------------------------------')
        })
      }else{
        if (token === null) {
          throw new Error('getTokenをfalseにする場合はTokenを引数に与えてください')
        }
        postToApi(path, jsonInput, token, successFunc, errorFunc)
      }
    }

    Vue.prototype.$getApi = (path, jsonInput, successFunc=()=>{}, errorFunc=getApiErrorDefaultFunc, getToken=true, token=null) => {
      if (getToken) {
        firebase.auth().currentUser.getIdToken(/* forceRefresh */ true).then(function(idToken) {
          getToApi(path, jsonInput, idToken, successFunc, errorFunc)
        }).catch(function(error) {
          console.log('---rinrin-api-plugin-$getApi--firebase-error-----')
          console.log(error)
          console.log('-------------------------------------------------')
        })
      }else{
        if (token === null) {
          throw new Error('getTokenをfalseにする場合はTokenを引数に与えてください')
        }
        getToApi(path, jsonInput, token, successFunc, errorFunc)
      }
    }
  }
}
  
export default RinRinApi