import { createRouter, createWebHistory } from "vue-router";
import { parseJwt } from "@/plugins/login";
import Cookies from "js-cookie";

import { refreshToken } from "@/plugins/login";
import RegisterHome from "@/components/Auth/RegisterHome";
import LoginHome from "@/components/Auth/LoginHome";
import WriteForm from "@/components/Post/WriteForm";
import CategoryPost from "@/components/Category/CategoryPost";
import CategoryMain from "@/components/Category/CategoryMain";
import KaniHome from "@/components/Home/KaniHome";
import MyHome from "@/components/Home/MyHome";
import PostComment from "@/components/Post/PostComment";

const routes = [
  {
    path: "/",
    name: "Home",
    component: KaniHome,
    meta: { unauthorized: false },
  },
  {
    path: "/login",
    name: "Login",
    component: LoginHome,
    meta: { unauthorized: true },
  },
  {
    path: "/register",
    name: "Register",
    component: RegisterHome,
    meta: { unauthorized: true },
  },
  {
    path: "/category/post/id/:object",
    name: "PostId",
    component: PostComment,
    meta: { unauthorized: false },
  },
  {
    path: "/category/post/:cate",
    name: "CatePost",
    component: CategoryPost,
    meta: { unauthorized: false },
  },
  {
    path: "/my",
    name: "MyHome",
    component: MyHome,
    meta: { unauthorized: false },
  },
  {
    path: "/write",
    name: "Write",
    component: WriteForm,
    meta: { unauthorized: false },
  },
  {
    path: "/category",
    name: "Category",
    component: CategoryMain,
    meta: { unauthorized: false },
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach(async (to, from, next) => {
  if (
    Cookies.get("access_token") === null &&
    Cookies.get("refresh_token") !== null
  ) {
    await refreshToken();
  }

  if (Cookies.get("access_token")) {
    if (parseJwt(Cookies.get("access_token")).exp < Date.now() / 1000) {
      Cookies.delete("access_token");
      next("/login");
    }
  }

  if (
    to.matched.some((record) => record.meta.unauthorized) ||
    Cookies.get("access_token")
  ) {
    return next();
  }

  return next("/login");
});

export default router;
