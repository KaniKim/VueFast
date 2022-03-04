<template>
  <v-app id="inspire">
    <MainMenu />
    <v-main>
      <PostList />
    </v-main>
    <v-footer app>
      <span>&copy; 2022</span>
    </v-footer>
  </v-app>
</template>

<script>
import MainMenu from "../components/MainMenu.vue";
import PostList from "../components/PostList.vue";
export default {
  components: { MainMenu, PostList },
};
</script>
