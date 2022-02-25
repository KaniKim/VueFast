import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import Vuelidate from "vuelidate";
import "./style.css";

createApp(App).use(store).use(router).use(Vuelidate).mount("#app");
