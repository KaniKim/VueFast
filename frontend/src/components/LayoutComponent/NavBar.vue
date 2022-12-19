<template>
  <v-app-bar color="primary">
    <v-app-bar-nav-icon @click.stop="drawer = !drawer">
    </v-app-bar-nav-icon>
    <v-app-bar-title>Back Door Welcome</v-app-bar-title>
  </v-app-bar>
  <BarDrawer v-model="drawer"></BarDrawer>
  <v-footer app bottom fixed width="100%" padless>
    <div class="px-4 py-2 text-center w-100">
      {{ new Date().getFullYear() }} — <strong>Back Door</strong>
    </div>
  </v-footer>
</template>
<script>
import BarDrawer from "@/components/LayoutComponent/BarDrawer";
export default {
  components: {BarDrawer},
  data() {
    return  {
      drawer: false
    }
  },
  watch: {
    group () {
      this.drawer = true
    },
  },
}

</script>
