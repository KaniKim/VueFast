<template>
  <v-app-bar :drawer="drawer" color="primary">
    <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
    <v-app-bar-title>Back Door JJal Bang</v-app-bar-title>
  </v-app-bar>
  <BarDrawer v-model="drawer"></BarDrawer>
</template>
<script>
import BarDrawer from "./BarDrawer";

export default {
  name: "NavBar",
  components: {BarDrawer},
  data() {
    return {
      drawer: false
    };
  },
};

</script>
