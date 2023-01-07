<template>
  <v-navigation-drawer v-model="drawerOpen">
    <v-list v-for="item in items" v-show="loggedIn" v-bind:key="item">
      <v-list-item>
        <nuxt-link :to="{path: item.value}" style="text-decoration: none; color: inherit;">{{ item.title }}
        </nuxt-link>
      </v-list-item>
    </v-list>
    <v-list v-for="item in items_not_login" v-show="!loggedIn" v-bind:key="item">
      <v-list-item>
        <NuxtLink :to="{path: item.value}" style="text-decoration: none; color: inherit;">{{ item.title }}
        </NuxtLink>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>
<script>
export default {
  props: ["drawer"],
  name: "BarDrawer",
  data: () => ({
    loggedIn: false,
    group: null,
    items: [
      {
        title: "Korean Food",
        value: "kr",
      },
      {
        title: "Chinese Food",
        value: "ch",
      },
      {
        title: "Japanese Food",
        value: "jp",
      },
      {
        title: "Western Food",
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
    }
  }
};
</script>
