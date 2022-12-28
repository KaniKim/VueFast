<template>
  <div>
    <v-navigation-drawer>
      <v-list v-for="item in items" v-if="loggedIn">
        <v-list-item>
          <router-link :to="{path: item.value}" style="text-decoration: none; color: inherit;">{{ item.title }}
          </router-link>
        </v-list-item>
      </v-list>
      <v-list v-for="item in items_not_login" v-if="!loggedIn">
        <v-list-item>
          <router-link :to="{path: item.value}" style="text-decoration: none; color: inherit;">{{ item.title }}
          </router-link>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>
<script>
export default {
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
        value: "/login",
      },
      {
        title: "sing up",
        value: "/sign",
      },
    ]
  }),
};
</script>
