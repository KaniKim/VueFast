<template>
  <v-app id="inspire">
    <MainMenu />
    <v-main>
      <PostInput />
    </v-main>
    <v-footer app>
      <span>&copy; 2022</span>
    </v-footer>
  </v-app>
</template>

<script>
import MainMenu from "../components/MainMenu.vue";
import PostInput from "../components/PostInput.vue";
export default {
  components: { MainMenu, PostInput },
};
</script>