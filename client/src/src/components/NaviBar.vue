<template>
  <nav class="navibar">
    <div class="navibar_content navibar_content_left">
      <router-link class="navibar_link" :class="[active==0 || active=='Today' ? 'is-active' : '']" to="/home">
        <div class="navibar_img">
          <font-awesome-icon icon="chart-bar"></font-awesome-icon>
        </div>
        <div class="navibar_label">
          今日の記録
        </div>
      </router-link>
    </div>
    <div class="navibar_content navibar_content_center">
      <router-link class="navibar_link" to="/search-course">
        <div class="navibar_img">
          <font-awesome-icon icon="running"></font-awesome-icon>
        </div>
        <div class="navibar_label">
          ランニング
        </div>
      </router-link>
    </div>
    <div class="navibar_content navibar_content_right">
      <router-link class="navibar_link" :class="[active==2 || active=='Friends' ? 'is-active' : '']" to="/friends">
        <div class="navibar_img">
          <font-awesome-icon icon="user-friends"></font-awesome-icon>
        </div>
        <div class="navibar_label">
          フレンド
        </div>
      </router-link>
    </div>
  </nav>
</template>

<style lang="scss">
@import "@/assets/scss/base/_variables.scss";

.navibar {
  display: flex;
  justify-content: space-around;
  align-items: center;
  background: $white;
  color: $black;
  width: 100%;
  height: 4rem;
  padding: 0.3rem;
  border-top: 1px solid $black;
  line-height: 1;
}

.navibar_link {
  display: flex;
  flex-direction: column;
  align-items: center;
  font-size: 0.8rem;

  &.is-active {
    color: $orange;
    pointer-events: none;
  }
}

.navibar_img {
  margin-bottom: 0.25rem;
  font-size: 225%;
  z-index: 1;
}

.navibar_label {
  z-index: 1;
}

.navibar_content_center {
  display: flex;
  flex-direction: column;
  position: relative;
  bottom: 1.5rem;
  color: $white;

  &::before {
    position: absolute;
    content: '';
    right: 50%;
    left: 50%;
    transform: translateX(-50%);
    bottom: -1.5rem;
    margin: 0 auto;
    width: 6rem;
    height: 6rem;
    border-radius: 50%;
    background: $red;
    z-index: 0;
  }
}
</style>

<script>
export default {
  props: {
    active: {
      type: [Number, String],
      required: true
    }
  },
  methods: {
  }
}
</script>
