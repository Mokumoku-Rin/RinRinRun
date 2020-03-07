import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    myGPSLocations:[],
    myRunTimeList:[],
    myRunStartTime: -1,
  },
  mutations: {
    addMyGPSLocation(state, location){
      state.myGPSLocations.push(location)
    },
    clearMyGPSLocation(state){
      state.myGPSLocations.length = 0
    },
    addMyRunTimeList(state, time){
      state.myRunTimeList.push(time)
    },
    clearMyRunTimeList(state){
      state.myRunTimeList.length = 0
    },
    resetMyRunStartTime(state){
      const tempDate = new Date()
      state.myRunStartTime = tempDate.getTime()
    }
  },
  actions: {
  },
  modules: {
  },
  getters: {
    myRunElapsedTime: state => {
      const tempDate = new Date()
      return tempDate.getTime() - state.myRunStartTime
    }
  }
})
