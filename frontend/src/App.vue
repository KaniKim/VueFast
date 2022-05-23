<template>
  <v-app :dark="true">
    <v-main>
      <DrawNav></DrawNav>
      <router-view/>
      <FooFighter></FooFighter>
    </v-main>
  </v-app>
</template>

<script>

import DrawNav from "@/components/layout/DrawNav";
import FooFighter from "@/components/layout/FooFighter";
export default {
  name: "App",
  components: {FooFighter, DrawNav},
  data: () => ({
    //
  }),
};
</script>
