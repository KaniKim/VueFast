import { createApp } from "vue";
import VueRouter from "vue-router";
import App from "./App.vue";
import store from "./store";
import "./main.css";
import './assets/tailwind.css'

createApp(App).use(store).use(VueRouter).mount("#app");
