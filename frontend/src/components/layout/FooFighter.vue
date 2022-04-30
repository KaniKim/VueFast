<template>
  <v-footer padless fixed width="100%" bottom class="bg-grey-lighten-1">
    <v-container fluid>
      <v-row justify="center">
        <v-btn
          v-for="link in links"
          :key="link"
          color="white"
          variant="text"
          class="mx-2"
          rounded="xl"
        >
          {{ link }}
        </v-btn>
        <v-col class="text-center text-white mt-4" cols="12">
          {{ new Date().getFullYear() }} — <strong>HomePage</strong>
        </v-col>
      </v-row>
    </v-container>
  </v-footer>
</template>
<script>
export default {
  data: () => ({
    links: ["Home", "About Us", "Category", "Contact Us"],
  }),
};
</script>
