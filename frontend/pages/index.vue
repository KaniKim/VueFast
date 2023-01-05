<template>
  <v-app>
    <v-main>
      <NavBar/>
      <nuxt></nuxt>
    </v-main>
  </v-app>
</template>
<script>
import NavBar from "../layout/NavBar";

export default {
  name: "home",
  components: {
    NavBar,
  }
};

</script>

