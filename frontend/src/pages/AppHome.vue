<template>
  <v-app id="inspire">
    <MainMenu />
    <v-main>
      <HelloWorld />
    </v-main>
    <v-footer app>
      <span>&copy; 2022</span>
    </v-footer>
  </v-app>
</template>

<script>
import MainMenu from "../components/MainMenu.vue";
import HelloWorld from "../components/HelloWorld.vue";
export default {
  components: { HelloWorld, MainMenu },
};
</script>
