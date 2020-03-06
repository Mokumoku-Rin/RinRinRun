<template>
  <div class="background"></div>
</template>

<style lang="scss">
@import "@/assets/scss/base/_variables.scss";

.background {
  position: fixed;
  top:0;
  left: 0;
  background: linear-gradient(top, $yellow, $orange);
  width: 100vw;
  height: 100vh;
  overflow-x: hidden;
  z-index: -1;
}
</style>
