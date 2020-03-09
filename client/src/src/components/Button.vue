<template>
  <div class="button-wrapper">
    <router-link class="button" :class="[reverse ? 'is-reverse' : '', color=='red' ? 'is-red' : '' ]" :to="link" v-if="link">
      <font-awesome-icon v-if="icon" :icon="icon"></font-awesome-icon>{{label}}
    </router-link>
    <a class="button" :class="[reverse ? 'is-reverse' : '', color=='red' ? 'is-red' : '' ]" @click="func" v-else-if="func">
      <font-awesome-icon v-if="icon" :icon="icon"></font-awesome-icon>{{label}}
    </a>
  </div>
</template>

<style lang="scss">
@import "@/assets/scss/base/_variables.scss";

.button {
  display: block;
  height: auto;
  width: 100%;
  padding: .75rem 0;
  font-weight: $weight-bold;
  font-size: 1.25rem;
  background: $white;
  color: $orange;
  border: 1px solid $orange;
  border-radius: 2%;
  svg {
    margin-right: .5rem;
  }

  &.is-reverse {
    background: transparent;
    color: $white;
    border-color: $white;
    border-radius: 2%;
  }
  &.is-red {
    background: $red;
    color: $white;
    border-color: $red;
    &.is-reverse {
      background: transparent;
      border-color: $black;
      color: $black;
    }
  }
}
</style>

<script>
export default {
  props: {
    link: {
      type: [Object, String]
    },
    func: {
      type: Function
    },
    icon: {
      type: [String, Array],
      default: ''
    },
    label: {
      type: String,
      required: true
    },
    reverse: {
      type: Boolean,
      default: false
    },
    color: {
      type: String,
      default: 'orange'
    }
  }
}
</script>
