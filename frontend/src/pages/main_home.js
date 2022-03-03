import { createApp } from "vue";
import AppHome from "./AppHome.vue";
import router from "../router";
import store from "../store";
import vuetify from "../plugins/vuetify";
import { loadFonts } from "../plugins/webfontloader";

loadFonts();

createApp(AppHome).use(router).use(store).use(vuetify).mount("#app");
