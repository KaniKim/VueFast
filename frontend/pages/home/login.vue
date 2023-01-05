<template>
  <v-app>
    <v-main>
      <NavBar></NavBar>
      <HomeMainLogin></HomeMainLogin>
    </v-main>
  </v-app>
</template>
<script>
import NavBar from "../../layout/NavBar";

export default {
  name: "login",
  components: {NavBar}
};
</script>
