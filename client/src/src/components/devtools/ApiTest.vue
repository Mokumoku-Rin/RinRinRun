<template>
  <div>
    -----------------------------------------------<br>
    <button @click="postTestButton">post test</button><br>
    <button @click="getTestButton">get test</button>
  </div>
</template>

<script>
export default {
  methods: {
    postTestButton(){ 
      this.$postApi('/test', {name:'this is post test'})
    },
    getTestButton(){
      this.$getApi('/test', {name:'this is get test'})
    }
  }
}
</script>
