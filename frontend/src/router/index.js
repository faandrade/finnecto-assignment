/**
 * router/index.ts
 *
 * Automatic routes for `./src/pages/*.vue`
 */

// Composables
import { createRouter, createWebHistory } from "vue-router";
//import { routes } from "vue-router/auto-routes";

const routes = [
  {
    path: "/",
    name: "home",
    component: () => import("@/components/Orders.vue"),
  },
];

const router = createRouter({
  history: createWebHistory("/"),
  routes,
});

export default router;
