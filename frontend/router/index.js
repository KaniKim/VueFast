import * as VueRouter from "vue-router";
import {store} from "../store";

const routes = [
  {path: "/", name: "home", component: "pages/index"},
  {path: "/home/login", name: "login", component: "pages/home/login"},
  {path: "/home/sign", name: "sign", component: "pages/home/sign"},
];

const router = VueRouter.createRouter({
  history: VueRouter.createWebHashHistory(),
  routes,
});

router.beforeEach(async (to, from, next) => {
  const accessToken = store.getters["accessToken"];
  const refreshToken = store.getters["refreshToken"];

  if (accessToken === null && refreshToken !== null) {
    await store.dispatch("refreshToken");
  }
  if (accessToken) {
    return next();
  }
  if (accessToken === null && refreshToken === null) {
    return next({name: "login"});
  }
  return next();
});

export default router;
