import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import axios from 'axios'
import VueAxios from 'vue-axios'
import firebase from 'firebase'

import RinRinApi from './plugins/rinrin-api'

Vue.config.productionTip = false
Vue.use(VueAxios, axios)
Vue.use(RinRinApi)

const firebaseConfig = {
  apiKey: "AIzaSyCVXhTVDoB3jKj_yAhtxiDU2dDxmf5v9LI",
  authDomain: "rinrinrun-ad626.firebaseapp.com",
  databaseURL: "https://rinrinrun-ad626.firebaseio.com",
  projectId: "rinrinrun-ad626",
  storageBucket: "rinrinrun-ad626.appspot.com",
  messagingSenderId: "131261806721",
  appId: "1:131261806721:web:98c7d935f5381a70517580",
  measurementId: "G-BPWRR07DV4"
}

firebase.initializeApp(firebaseConfig)
firebase.analytics()

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
