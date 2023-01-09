<template>
  <v-navigation-drawer v-model="drawerOpen">
    <v-list v-for="item in items" v-show="loggedInOrNot" v-bind:key="item">
      <v-list-item>
        <NuxtLink :to='{name: "jjal-id", params: { id: item.value }}'
                  style="text-decoration: none; color: inherit;">
          {{ item.title }}
        </NuxtLink>
      </v-list-item>
    </v-list>
    <v-list v-for="item in items_not_login" v-show="!loggedInOrNot" v-bind:key="item">
      <v-list-item>
        <NuxtLink :to="{path: item.value}" style="text-decoration: none; color: inherit;">{{ item.title }}
        </NuxtLink>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>
<script>
import store from "../../store";

export default {
  props: ["drawer"],
  name: "BarDrawer",
  data: () => ({
    group: null,
    items: [
      {
        title: "Korean JJAL",
        value: "kr",
      },
      {
        title: "Chinese JJAL",
        value: "ch",
      },
      {
        title: "Japanese JJAL",
        value: "jp",
      },
      {
        title: "Western JJAL",
        value: "ws",
      },
    ],
    items_not_login: [
      {
        title: "login",
        value: "/home/login",
      },
      {
        title: "sing up",
        value: "/home/sign",
      },
    ]
  }),
  computed: {
    drawerOpen() {
      return this.drawer;
    },
    loggedInOrNot() {
      return store.state.access_token !== null;
    }
  }
};
</script>
