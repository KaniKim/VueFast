import {defineNuxtConfig} from "nuxt/config";

export default defineNuxtConfig({
  css: [
    "vuetify/lib/styles/main.sass"
  ],
  build: {
    transpile: ["vuetify"]
  },
});
