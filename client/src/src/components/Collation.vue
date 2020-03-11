<template>
  <div class="collation" :class="active ? 'is-active' : ''">
    <div class="collation_inner">
      <font-awesome-icon class="collation_icon" icon="spinner" spin></font-awesome-icon>
      <p class="collation_message">しばらくお待ち下さい</p>
    </div>
  </div>
</template>

<style lang="scss">
@import "@/assets/scss/base/_variables.scss";

.collation {
  display: none;

  &.is-active {
    display: block;
    position: absolute;
    top: 0;
    left: 0;
    height: 100vh;
    width: 100vw;
    z-index: 2;
    backdrop-filter: blur(3px);
    display: flex;
    justify-content: center;
    align-items: center;
    color: $black;
  }
}

.collation_inner {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

.collation_icon {
  font-size: 7.5rem;
  margin-bottom: 1rem;
}

.collation_message {
  font-size: 1.75rem;
  font-weight: $weight-bold;
}
</style>

<script>
export default {
  props: {
    active: {
      type: Boolean,
      default: false
    },
    func: {
      type: Function
    }
  }
}
</script>
