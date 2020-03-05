<template>
  <div>
    -----------------------------------------------<br>
    <button @click="getSessionButton">session get test</button><br>
    <button @click="postTestButton">post test</button><br>
    <button @click="getTestButton">get test</button>
  </div>
</template>

<script>
export default {
  methods: {
    getSessionButton(){
      this.$getApi('/session', {name:'this is get test'})
    },
    postTestButton(){ 
      this.$postApi('/test', {name:'this is post test'})
    },
    getTestButton(){
      this.$getApi('/test', {name:'this is get test'})
    }
  }
}
</script>
