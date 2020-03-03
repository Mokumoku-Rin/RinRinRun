<template>
  <div>
    -----------------------------------------------<br>
    <button @click="postTestButton">post test</button>
  </div>
</template>

<script>
export default {
  methods: {
    postTestButton(){ 
      this.$sendApi('test', {name:'aaa'})
    }
  }
}
</script>
