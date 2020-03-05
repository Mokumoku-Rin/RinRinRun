import Vue from 'vue'
import VueRouter from 'vue-router'
import firebase from 'firebase'

Vue.use(VueRouter)

const routes = [
  // --------------dev---------------
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/Home.vue')
  },
  {
    path: '/home',
    name: 'Home',
    component: () => import('../views/Home.vue')
  },
  //--------------------------------

  // -------producrtion-------------
  // {
  //   path: '/',
  //   name: 'Home',
  //   component: () => import('../views/Home.vue')
  // },
  // ------------------------------

  {
    path: '/search-course',
    name: 'SearchCourse',
    component: () => import('../views/SearchCourse.vue')
  },
  {
    path: '/choice-course',
    name: 'ChoiceCourse',
    component: () => import('../views/ChoiceCourse.vue')
  },


  // -------before login------------
  {
    path: '/login-home',
    name: 'Login',
    component: () => import('../views/Login/LoginHome.vue')
  },
  {
    path: '/mail-login',
    name: 'LoginHome',
    component: () => import('../views/Login/MailLogin.vue')
  },
  {
    path: '/mail-register',
    name: 'MailRegister',
    component: () => import('../views/Login/MailRegister.vue')
  },
  {
    path: '/forget-password',
    name: 'ForgetPassword',
    component: () => import('../views/Login/ForgetPassword.vue')
  }
]

const router = new VueRouter({
  routes
})

// 未ログインでも遷移できるページ
const loginWhiteList = [
  '/login-home',
  '/mail-login',
  '/mail-register',
  '/forget-password',
]

router.beforeEach((to, from, next) => {
  if (loginWhiteList.indexOf(to.path) !== -1) {
    next()
  } else {
    firebase.auth().onAuthStateChanged(user => {
      if (user) {
        console.log('login済み')
        next()
      } else {
        console.log('未login')
        next({path: '/login-home'})
      }
    })
  }
})

export default router
