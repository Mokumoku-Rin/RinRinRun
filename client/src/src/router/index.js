import Vue from 'vue'
import VueRouter from 'vue-router'
import firebase from 'firebase'

Vue.use(VueRouter)

const routes = [
  // --------------dev---------------
  {
    path: '/',
    name: 'DevHome',
    component: () => import('../views/DevHome.vue')
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
    path: '/friends',
    name: 'Friends',
    component: () => import('../views/Friends.vue')
  },
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
  {
    path: '/course-info',
    name: 'CourseInfo',
    component: () => import('../views/CourseInfo.vue')
  },
  {
    path: '/landmark-info',
    name: 'LandmarkInfo',
    component: () => import('../views/LandmarkInfo.vue')
  },
  {
    path: '/take-picture',
    name: 'TakePicture',
    component: () => import('../views/TakePicture.vue')
  },
  {
    path: '/running-info',
    name: 'RunningInfo',
    component: () => import('../views/RunnningInfo.vue')
  },
  {
    path: '/running-goal',
    name: 'RunningGoal',
    component: () => import('../views/RunningGoal.vue')
  },
  {
    path: '/run-map-test',
    name: 'RunMapTest',
    component: () => import('../views/RunMapTest.vue')
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
  },

  // -------開発者ページ--------------
  {
    path: '/dev/landmark-register',
    name: 'LandmarkRegister',
    component: () => import('../views/LandmarkRegister.vue')
  },
  {
    path: '/dev/course-register',
    name: 'CourseRegister',
    component: () => import('../views/CourseRegister.vue')
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
