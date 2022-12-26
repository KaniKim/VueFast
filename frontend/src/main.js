/**
 * main.js
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Components
import App from "./App.vue";

// Composables
import {createApp} from "vue";
import router from "@/routes";

// Plugins
import {registerPlugins} from "@/plugins";
import {store} from "@/store/index";
import VueCookies from "vue-cookies";

const app = createApp(App);

registerPlugins(app);

app.use(router);
app.use(store);
app.use(VueCookies);
app.mount("#app");

