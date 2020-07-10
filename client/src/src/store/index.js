import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    myGPSLocations:[],
    myRunTimeList:[],
    myRunStartTime: -1,
    myRunNowDistance: 0,
    myRunCheckedLandmarkID: [],
    isRunning: false,
    myLandmarkVisits: [],
    runningCourseData: null,
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
    },
    setMyRunNowDistance(state, distance){
      state.myRunNowDistance = distance
    },
    setIsRuning(state, running){
      state.isRunning = running
    },
    addMyRunCheckedLandmarkID(state, input_id){
      state.myRunCheckedLandmarkID.push(input_id)
    },
    clearMyRunCheckedLandmarkID(state){
      state.myRunCheckedLandmarkID.length = 0
    },
    addMyLandmarkVisits(state, visit){
      state.myLandmarkVisits.push(visit)
    },
    clearMyLandmarkVisits(state){
      state.myLandmarkVisits.length = 0
    },
    setRunnigCourseData(state, data){
      state.runningCourseData = data
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
