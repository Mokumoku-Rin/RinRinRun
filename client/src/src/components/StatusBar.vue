<template>
  <nav class="statusbar">
    <div class="statusbar_left">
      <a v-if="leftLink" @click="goTo(leftLink)">
        <font-awesome-icon icon="chevron-left"></font-awesome-icon>
      </a>
      <a v-else-if="leftFunc" @click="leftFunc">
        <font-awesome-icon icon="chevron-left"></font-awesome-icon>
      </a>
    </div>
    <div class="statusbar_center">
      <h1 v-if="center" class="statusbar_title">{{center}}</h1>
    </div>
    <div class="statusbar_right">
      <a v-if="avatar" @click="rightFunc">
        <img class="statusbar_avatar" :src="avatar" alt="アバター">
      </a>
      <a v-else-if="rightFunc" @click="$emit('rightFunc')">
        <font-awesome-icon icon="times"></font-awesome-icon>
      </a>
    </div>
  </nav>
</template>

<style lang="scss">
@import "@/assets/scss/base/_variables.scss";

.statusbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: transparent;
  padding: .8rem 1.5rem;
  font-size: 1.25rem;
  color: $white;

  a {
    color: $white;
  }
}

.statusbar_left, .statusbar_right {
  width: 1.75rem;
  height: 1.75rem;
}

.statusbar_center {
  margin: 0 auto;
  h1{
    font-weight: $weight-bold;
  }
}

.statusbar_avatar {
  border: 1px solid $white;
  border-radius: 50%;
  background: $white;
}
</style>

<script>
import router from '../router'

export default {
  props: {
    leftLink: {
      type: String
    },
    leftFunc: {
      type: Function
    },
    center: {
      type: String
    },
    rightLink: {
      type: String
    },
    rightFunc: {
      type: Function
    },
    avatar: {
      type: String
    },
    color: {
      type: String
    }
  },
  methods: {
    goTo(path) {
      router.push(path)
    }
  }
}
</script>
