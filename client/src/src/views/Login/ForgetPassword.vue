<template>
  <div class="password_forget">
    <h1 class="title">パスワード忘れたの？</h1>
    <p class="subtitle">
      困ったね。<br>
      でも、今はどうもできないよ…
    </p>
  </div>
</template>

<style lang="scss">
@import "@/assets/scss/base/_variables.scss";

.password_forget {
  overflow-y: hidden;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.title, .subtitle {
  color: $white;
  margin: 1.5rem;
}
</style>

<script>


</script>
