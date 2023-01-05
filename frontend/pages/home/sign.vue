<template>
  <v-app>
    <v-main>
      <NavBar></NavBar>
      <HomeMainSign></HomeMainSign>
    </v-main>
  </v-app>
</template>
<script>
import NavBar from "../../layout/NavBar";

export default {
  name: "sign",
  components: {NavBar}
};
</script>
