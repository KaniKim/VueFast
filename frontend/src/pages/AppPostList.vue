<template>
  <v-app id="inspire">
    <v-app-bar app :clipped-left="true" color="indigo">
      <v-app-bar-nav-icon @click="drawer = !drawer"> </v-app-bar-nav-icon>
      <v-toolbar-title>Vue.js - FastAPI</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn text flat href="/" v-text="'Home'"></v-btn>
      <v-btn text href="/postlist.html" v-text="'PostList'"></v-btn>
      <v-btn text href="/postdetail.html" v-text="'PostDetail'"></v-btn>
      <v-menu>
        <template v-slot:activator="{ props }">
          <v-btn text v-bind="props">
            <v-icon> mdi-dots-vertical</v-icon>
            Anonymous
          </v-btn>
        </template>
        <v-list dense left bottom>
          <v-list-item link>
            <v-list-item-title>Login</v-list-item-title>
          </v-list-item>
          <v-list-item link>
            <v-list-item-title>Register</v-list-item-title>
          </v-list-item>
          <v-list-item link>
            <v-list-item-title>Logout</v-list-item-title>
          </v-list-item>
          <v-list-item link>
            <v-list-item-title>Password Change</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-app-bar>
    <v-navigation-drawer v-model="drawer" :clipped="true" app>
      <v-list dense nav>
        <v-list-item v-for="item in items" :key="item.title" link>
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-main>
      <PostList />
    </v-main>
    <v-footer app>
      <span>&copy; 2022</span>
    </v-footer>
  </v-app>
</template>

<script>
import PostList from "../components/PostList.vue";
export default {
  components: { PostList },

  data: () => ({
    drawer: false,
    items: [
      { title: "Dashboard", icon: "mdi-view-dashboard" },
      { title: "Photos", icon: "mdi-image" },
      { title: "About", icon: "mdi-help-box" },
    ],
  }),
};
</script>
