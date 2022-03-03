import { createApp } from "vue";
import AppPostList from "./AppPostList.vue";
import router from "../router";
import store from "../store";
import vuetify from "../plugins/vuetify";
import { loadFonts } from "../plugins/webfontloader";

loadFonts();

createApp(AppPostList).use(router).use(store).use(vuetify).mount("#app");
