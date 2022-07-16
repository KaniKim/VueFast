<template>
    <v-app-bar color="grey-lighten-2">
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
    </v-app-bar>
     <v-navigation-drawer color="grey-darken-2" permanent v-model="drawer">
    </v-navigation-drawer>
</template>

<script>
export default {
  data() {
    return  {drawer: false};
  }
};

</script>