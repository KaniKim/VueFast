<template>
  <v-app>
    <main>
      <NavBar/>
      <router-view></router-view>
    </main>
  </v-app>
</template>
<script>
import NavBar from "../layout/NavBar";

export default {
  components: {
    NavBar,
  }
};

</script>

