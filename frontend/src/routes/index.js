import * as VueRouter from 'vue-router'

const routes = [
  { path: '/', component: () => import("@/components/LoggedHomeComponent/HomeMain") },
  { path: '/login', component: () => import("@/components/NotLoggedHomeComponent/HomeMainLogin") },
  { path: '/sign', component: () => import("@/components/NotLoggedHomeComponent/HomeMainSign")},
]

const router = VueRouter.createRouter({
  history: VueRouter.createWebHashHistory(),
  routes,
})

export default router;
