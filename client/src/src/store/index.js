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
    runnigCourseData: null,
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
      console.log('push id ',input_id)
      state.myRunCheckedLandmarkID.push(input_id)
      console.log('push id ',input_id)
      console.log(state.myRunCheckedLandmarkID)
    },
    clearMyRunCheckedLandmarkID(state){
      state.myRunCheckedLandmarkID.length = 0
    },
    addMyLandmarkVisits(state, id, time){
      state.myLandmarkVisits.push({id:id, time:time})
    },
    clearMyLandmarkVisits(state){
      state.myLandmarkVisits.length = 0
    },
    setRunnigCourseData(state, data){
      state.runnigCourseData = data
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
