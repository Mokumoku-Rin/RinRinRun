<template>
  <div class="background"></div>
</template>

<style lang="scss">
@import "@/assets/scss/_variables.scss";
@import "@/assets/scss/_components.scss";

.background {
  position: fixed;
  background: linear-gradient(top, $yellow, $orange);
  width: 100vw;
  height: 100vh;
  overflow-x: hidden;
}
</style>
