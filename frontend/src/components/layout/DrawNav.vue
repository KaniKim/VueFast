<template>
  <div>
  <v-app-bar
    color="gray"
    prominent
    src="https://cdn.vuetifyjs.com/images/backgrounds/vbanner.jpg"
  >
    <v-app-bar-nav-icon
      variant="text"
      @click.stop="drawer = !drawer"
    ></v-app-bar-nav-icon>

    <v-toolbar-title>Hello From Kani</v-toolbar-title>
    <v-spacer></v-spacer>
  </v-app-bar>

  <v-navigation-drawer v-model="drawer" temporary>
    <v-list>
      <div v-if="cookie === true">
        <v-list-item
          v-for="(item, key) in items_drawer_true"
          :key="key"
          :to="item.route"
        >
          <v-list-item>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item>
        </v-list-item>
      </div>
      <div v-else>
        <v-list-item
          v-for="(item, key) in items_drawer_false"
          :key="key"
          :to="item.route"
        >
          <v-list-item>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item>
        </v-list-item>
      </div>
    </v-list>
  </v-navigation-drawer>
    </div>
</template>
<script>
import Cookies from "js-cookie";

export default {
  data: () => ({
    drawer: false,
    items_drawer_false: [
      {
        title: "Login",
        route: "/login",
        value: false,
      },
      {
        title: "Register",
        route: "/register",
        value: false,
      },
    ],
    items_drawer_true: [
      {
        title: "Home",
        route: "/",
        value: true,
      },

      {
        title: "Write",
        route: "/write",
        value: true,
      },
      {
        title: "Category",
        route: "/category",
        value: true,
      },
    ],
  }),
  created() {
    this.$forceUpdate();
  },
  computed: {
    cookie() {
      return !!Cookies.get("access_token");
    },
  },

  watch: {
    group() {
      this.drawer = false;
    },
  },
};
</script>
