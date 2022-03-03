<template>
  <v-app id="inspire">
    <v-app-bar app :clipped-left="true" dark color="indigo">
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

      <v-toolbar-title>Application</v-toolbar-title>
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
      <HelloWorld />
    </v-main>
    <v-footer app>
      <span>&copy; 2022</span>
    </v-footer>
  </v-app>
</template>

<script>
import HelloWorld from "./components/HelloWorld.vue";
export default {
  components: { HelloWorld },

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
