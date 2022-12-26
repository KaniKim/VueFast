import * as VueRouter from "vue-router";
import {store} from "@/store";

const routes = [
  {path: "/", component: () => import("@/components/LoggedHomeComponent/HomeMain")},
  {path: "/login", component: () => import("@/components/NotLoggedHomeComponent/HomeMainLogin")},
  {path: "/sign", component: () => import("@/components/NotLoggedHomeComponent/HomeMainSign")},
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
