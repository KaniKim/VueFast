<template>
  <NavBar></NavBar>
  <SignIn></SignIn>
</template>

<script>
import SignIn from "./components/SignComponent/SignIn.vue";
import NavBar from "./components/LayoutComponent/NavBar"

export default {
  name: "App",
  components: {
    SignIn,
    NavBar
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
