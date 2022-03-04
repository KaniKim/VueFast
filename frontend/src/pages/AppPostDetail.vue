<template>
  <v-app id="inspire">
    <MainMenu />
    <v-main>
      <PostDetail />
    </v-main>
    <v-footer app>
      <span>&copy; 2022</span>
    </v-footer>
  </v-app>
</template>

<script>
import MainMenu from "../components/MainMenu.vue";
import PostDetail from "../components/PostDetail.vue";
export default {
  components: { MainMenu, PostDetail },
};
</script>
