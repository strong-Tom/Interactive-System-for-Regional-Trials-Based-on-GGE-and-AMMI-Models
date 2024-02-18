import Vue from "vue";
import VueRouter from "vue-router";
import Router from "vue-router";

Vue.use(Router);

const routes = [
  {
    path: "/",
    component: () => import("../views/loginRegister.vue"),
  },

  {
    path: "/main",
    // redirect: "/login",
    name: "main",
    
    // component: () => import("../views/loginRegister.vue"),
    component: () => import("../views/main.vue"),
    // component: () => import("../views/loginRegister.vue"),
    // component: () => import("../views/tree/index.vue"),

    children: [




      {
        path: "/home",
        name: "home",
        component: () => import("../views/home/index.vue"),
        meta: { requireAuth: true },
      },

      {
        path: "/tree",
        name: "tree",
        component: () => import("../views/tree/index.vue"),
        meta: { requireAuth: true },
      },
      {
        path: "/user",
        name: "user",
        component: () => import("../views/user/index.vue"),
        meta: { requireAuth: true },
      },
      {
        path: "/test",
        name: "test",
        component: () => import("../aatest/test.vue"),
        // meta:{requireAuth:true}
      },
      {
        path: "/treeShow",
        name: "treeShow",
        component: () => import("../views/treeShow"),
        meta: { requireAuth: true },
      },
      {
        path: "/uploadExcel",
        name: "uploadExcel",
        component: () => import("../views/uploadExcel"),
        meta: { requireAuth: true },
      },
      {
        path: "/uploadVideo",
        name: "uploadVideo",
        component: () => import("../views/uploadVideo"),
        meta: { requireAuth: true },
      },
      {
        path: "/videoInfo",
        name: "videoInfo",
        component: () => import("../views/videoInfo"),
        meta: { requireAuth: true },
      },

      {
        path: "/videoSearch",
        name: "videoSearch",
        component: () => import("../views/videoSearch"),
        meta: { requireAuth: true },
      },
      {
        path: "/userCenter",
        name: "userCenter",
        component: () => import("../views/UserCenter"),
        meta: { requireAuth: true },
      },
      {
        path: "/modifyUser",
        name: "modifyUser",
        component: () => import("../views/ModifyUser"),
        meta: { requireAuth: true },
      },
      {
        path: "/modifyPassword",
        name: "modifyPassword",
        component: () => import("../views/ModifyPassword"),
        meta: { requireAuth: true },
      },
      {
        path: "/featureExtraction",
        name: "featureExtraction",
        component: () => import("../views/featureExtraction"),
        meta: { requireAuth: true },
      },
      {
        path: "/trainingResults",
        name: "trainingResults",
        component: () => import("../views/trainingResults"),
        meta: { requireAuth: true },
      },
      {
        path: "/ruleExtraction",
        name: "ruleExtraction",
        component: () => import("../views/ruleExtraction"),
        meta: { requireAuth: true },
      },
      {
        path: "/ruleExtractionResults",
        name: "ruleExtractionResults",
        component: () => import("../views/ruleExtractionResults"),
        meta: { requireAuth: true },
      },
      {
        path: "/scatter",
        name: "scatter",
        component: () => import("../views/scatter"),
        meta: { requireAuth: true },
      },
      {
        path: "/AMMI",
        name: "AMMI",
        component: () => import("../views/AMMI"),
        meta: { requireAuth: true },
      },
      {
        path: "/GGE",
        name: "GGE",
        component: () => import("../views/GGE"),
        meta: { requireAuth: true },
        
      },
      {
        path: "/variety_yield_and_stability",
        name: "variety_yield_and_stability",
        component: () => import("../views/variety_yield_and_stability"),
        meta: { requireAuth: true },
        
      },
      {
        path: "/which_won_where",
        name: "which_won_where",
        component: () => import("../views/which_won_where"),
        meta: { requireAuth: true },
        
      },
         {
        path: "/map",
        name: "map",
        component: () => import("../views/map"),
        meta: { requireAuth: true },
        
      },
      {
        path: "/region1",
        name: "region1",
        component: () => import("../views/region1"),
        meta: { requireAuth: true },
        
      },
      {
        path: "/region",
        name: "region",
        component: () => import("../views/region"),
        meta: { requireAuth: true },
        
      },
      {
        path: "/region2",
        name: "region2",
        component: () => import("../views/region2"),
        meta: { requireAuth: true },
        
      },
      {
        path: "/region3_image",
        name: "region3_image",
        component: () => import("../views/region3_image"),
        meta: { requireAuth: true },
        
      },
      {
        path: "/growth_dq",
        name: "growth_dq",
        component: () => import("../views/growth_dq"),
        meta: { requireAuth: true },
        
      },
      {
        path: "/growth_qq",
        name: "growth_qq",
        component: () => import("../views/growth_qq"),
        meta: { requireAuth: true },
        
      },
      {
        path: "/diameter_dq",
        name: "diameter_dq",
        component: () => import("../views/diameter_dq"),
        meta: { requireAuth: true },
        
      },
      {
        path: "/diameter_qq",
        name: "diameter_qq",
        component: () => import("../views/diameter_qq"),
        meta: { requireAuth: true },
        
      },
      {
        path: "/heat_dq",
        name: "heat_dq",
        component: () => import("../views/heat_dq"),
        meta: { requireAuth: true },
        
      },
      {
        path: "/heat_qq",
        name: "heat_qq",
        component: () => import("../views/heat_qq"),
        meta: { requireAuth: true },
        
      },
      {
        path: "/heat_xhy",
        name: "heat_xhy",
        component: () => import("../views/heat_xhy"),
        meta: { requireAuth: true },
        
      },
      {
        path: "/heat_hqy",
        name: "heat_hqy",
        component: () => import("../views/heat_hqy"),
        meta: { requireAuth: true },
        
      },
      {
        path: "/heat_yzy",
        name: "heat_yzy",
        component: () => import("../views/heat_yzy"),
        meta: { requireAuth: true },
        
      },
      {
        path: "/heat_qsy",
        name: "heat_qsy",
        component: () => import("../views/heat_qsy"),
        meta: { requireAuth: true },
        
      },
      {
        path: "/show_img_hqy",
        name: "show_img_hqy",
        component: () => import("../views/show_img_hqy"),
        meta: { requireAuth: true },
        
      },
      {
        path: "/show_img_qsy",
        name: "show_img_qsy",
        component: () => import("../views/show_img_qsy"),
        meta: { requireAuth: true },
        
      },
      {
        path: "/show_img_qsy1",
        name: "show_img_qsy1",
        component: () => import("../views/show_img_qsy1"),
        meta: { requireAuth: true },
        
      },
      {
        path: "/phenomena",
        name: "phenomena",
        component: () => import("../views/phenomena"),
        meta: { requireAuth: true },
        
      },
      {
        path: "/fy",
        name: "fy",
        component: () => import("../views/fy"),
        meta: { requireAuth: true },
        
      },
      {
        path: "/qq",
        name: "qq",
        component: () => import("../views/qq"),
        meta: { requireAuth: true },
        
      },
      {
        path: "/lj",
        name: "lj",
        component: () => import("../views/lj"),
        meta: { requireAuth: true },
        
      },
      {
        path: "/dq",
        name: "dq",
        component: () => import("../views/dq"),
        meta: { requireAuth: true },
        
      },
      {
        path: "/hr",
        name: "hr",
        component: () => import("../views/hr"),
        meta: { requireAuth: true },
        
      },
      {
        path: "/nh",
        name: "nh",
        component: () => import("../views/nh"),
        meta: { requireAuth: true },
        
      },
      {
        path: "/gn",
        name: "gn",
        component: () => import("../views/gn"),
        meta: { requireAuth: true },
        
      },
      {
        path: "/introduction",
        name: "introduction",
        component: () => import("../views/introduction"),
        meta: { requireAuth: true },
      },
      {
        path: "/region11",
        name: "region11",
        component: () => import("../views/region11"),
        meta: { requireAuth: true },
      },
      {
        path: "/region12",
        name: "region12",
        component: () => import("../views/region12"),
        meta: { requireAuth: true },
      },
      {
        path: "/region15",
        name: "region15",
        component: () => import("../views/region15"),
        meta: { requireAuth: true },
      },
      {
        path: "/heat_other",
        name: "heat_other",
        component: () => import("../views/heat_other"),
        meta: { requireAuth: true },
      },
      {
        path: "/show_img_wood",
        name: "show_img_wood",
        component: () => import("../views/show_img_wood"),
        meta: { requireAuth: true },
      },
    ],
  },
];
const router = new VueRouter({
  //若为history模式打包到django后会出现页面跳转路由失效
  // mode: "history",
  routes,
});
export default router;
