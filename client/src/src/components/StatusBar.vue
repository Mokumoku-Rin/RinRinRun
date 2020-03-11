<template>
  <nav class="statusbar" :class="backgroundColor=='white' ? 'is-white' : '' ">
    <div class="statusbar_left">
      <router-link v-if="leftLink" :to="leftLink">
        <font-awesome-icon icon="chevron-left"></font-awesome-icon>
      </router-link>
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
      <a v-else-if="rightFunc" @click="rightFunc">
        <font-awesome-icon icon="times"></font-awesome-icon>
      </a>
    </div>
  </nav>
</template>

<style lang="scss">
@import "@/assets/scss/base/_variables.scss";

.statusbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;

  display: flex;
  justify-content: space-between;
  align-items: center;
  background: transparent;
  padding: .8rem 1.5rem;
  font-size: 1.25rem;
  color: $white;
  z-index: 1;

  a {
    color: $white;
  }
  &.is-white {
    background: $white;
    color: $orange;
    border-bottom: 1px solid $black;

    a {
      color: $red;
    }
  }
}

.statusbar_left, .statusbar_right {
  width: 1.75rem;
  height: 1.75rem;
}

.statusbar_center {
  margin: 0 auto;
  display: -webkit-box;
  overflow: hidden;
  text-overflow: ellipsis;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
  text-align: center;
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

export default {
  props: {
    leftLink: {
      type: [String, Object]
    },
    leftFunc: {
      type: Function
    },
    center: {
      type: String
    },
    rightLink: {
      type: [String, Object]
    },
    rightFunc: {
      type: Function
    },
    avatar: {
      type: String
    },
    backgroundColor: {
      type: String,
      default: 'orange'
    }
  }
}
</script>
