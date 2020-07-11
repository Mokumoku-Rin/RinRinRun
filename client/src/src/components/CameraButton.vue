<template>
  <footer class="camera_button_wrapper" :class="active ? 'is-active' : ''">
    <Button label="撮影" :func="func" color="red" icon="camera" v-if="func"></Button>
    <Button label="撮影" :link="link" color="red" icon="camera" v-else-if="active"></Button>
    <Button label="撮影場所に移動してください" :link="link" color="red" :reverse="true" v-else></Button>
  </footer>
</template>

<style lang="scss">
@import "@/assets/scss/base/_variables.scss";

.camera_button_wrapper {
  bottom: 0;
  left: 0;
  right: 0;
  top: 92.2vh;
  background: $white;
  pointer-events: none;
  width: 50vw;

  &.is-active {
    pointer-events: auto;
  }
}
</style>

<script>
import Button from '@/components/Button.vue'

export default {
  props: {
    active: {
      type: Boolean,
      default: false
    },
    link: {
      type: [Object, String],
      default: function() {
        return {path: '/home'}
      }
    },
    func: {
      type: Function
    }
  },
  components: {
    Button
  }
}
</script>
