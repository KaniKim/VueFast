<template>
  <div>
    <v-app>
      <NavHeader></NavHeader>
      <RouterView></RouterView>
      <NavFooter></NavFooter>
    </v-app>
  </div>
</template>

<script>
import NavHeader from "../components/layout/NavHeader";
import NavFooter from "../components/layout/NavFooter";

export default {
  components: {NavFooter, NavHeader}
};
</script>
