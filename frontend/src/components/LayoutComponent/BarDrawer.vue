<template>
  <v-navigation-drawer>
    <v-list v-if="loggedIn" v-for="item in items">
      <v-list-item>
        <router-link style="text-decoration: none; color: inherit;" :to="{path: item.value}">{{item.title}}</router-link>
      </v-list-item>
    </v-list>
    <v-list v-if="!loggedIn" v-for="item in items_not_login">
      <v-list-item>
        <router-link style="text-decoration: none; color: inherit;" :to="{path: item.value}">{{item.title}}</router-link>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>
<script>
export default {
  data: () => ({
    loggedIn: false,
    group: null,
    items: [
      {
        title: 'Korean Food',
        value: 'kr',
      },
      {
        title: 'Chinese Food',
        value: 'ch',
      },
      {
        title: 'Japanese Food',
        value: 'jp',
      },
      {
        title: 'Western Food',
        value: 'ws',
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
}
</script>
