import { createApp } from "vue";
import AppPostInput from "./AppPostInput.vue";
import router from "../router";
import store from "../store";
import vuetify from "../plugins/vuetify";
import { loadFonts } from "../plugins/webfontloader";

loadFonts();

createApp(AppPostInput).use(router).use(store).use(vuetify).mount("#app");
