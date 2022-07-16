<template>
  <v-app>
    <LayoutFullVue></LayoutFullVue>
    <v-main>
      <MainFullVue></MainFullVue>
    </v-main>
  </v-app>
</template>

<script>
import LayoutFullVue from "./components/LayoutFull.vue";
import MainFullVue from "./components/MainFull.vue";

export default {
  name: "App",

  components: {
    LayoutFullVue,
    MainFullVue
  },

  data: () => ({
    //
  }),
};
</script>
