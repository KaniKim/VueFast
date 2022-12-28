<template>
  <v-app>
    <v-main>
      <BarDrawer/>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script setup>
import BarDrawer from "./components/LayoutComponent/NavBar";
</script>
