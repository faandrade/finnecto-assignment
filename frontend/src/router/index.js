import { createRouter, createWebHistory } from "vue-router";
import OrdersView from "../views/OrdersView.vue";

const router = createRouter({
  //history: createWebHistory(import.meta.env.BASE_URL),
  history: createWebHistory("/"),
  routes: [
    {
      path: "/",
      name: "orders",
      component: OrdersView,
    },
  ],
});

export default router;
