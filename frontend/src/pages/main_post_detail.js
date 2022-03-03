import { createApp } from "vue";
import AppPostDetail from "./AppPostDetail.vue";
import router from "../router";
import store from "../store";
import vuetify from "../plugins/vuetify";
import { loadFonts } from "../plugins/webfontloader";

loadFonts();

createApp(AppPostDetail).use(router).use(store).use(vuetify).mount("#app");
