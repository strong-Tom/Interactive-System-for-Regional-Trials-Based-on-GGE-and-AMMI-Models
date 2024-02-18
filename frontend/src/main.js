import Vue from "vue";
import App from "./App.vue";
import router from "../router";
import ElementUI from "element-ui";
import "element-ui/lib/theme-chalk/index.css";
import "./assets/less/index.less";
import store from "../store";
import http from "axios";
import "../api/mock";
// 此处省略其他包名
import lCharts from "l-charts/packages";
// import XLSX from 'xlsx/dist/xlsx.full.min'
import EleForm from "vue-ele-form";
import EleFormVideoUploader from "vue-ele-form-video-uploader";
// 注册 ele-form
// 全局引入
import EleUploadVideo from "vue-ele-upload-video";
//引入BootstrapVue及其相关css
import BootstrapVue from "bootstrap-vue";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
// vxe-table
import './plugins/vxe-table'
// 全局使用axios，this.$axios
import axios from "axios";
Vue.prototype.$axios=axios
// 全局使用echarts，this.$echarts
// import echarts from "echarts";
import * as echarts from 'echarts';

Vue.prototype.$echarts = echarts;


Vue.component(EleUploadVideo.name, EleUploadVideo);
Vue.use(EleForm, {
  // 对所有具有上传属性的组件适用
  upload: {
    fileSize: 1000,
  },
  // 可以在这里设置全局的 video-uploader 属性
  // 具体属性列表请看下面 #attrs
  "video-uploader": {
    action: "http://127.0.0.1:8000/api/video/", // 上传地址
  },
});
Vue.use(BootstrapVue);
// 注册 video-uploader 组件
Vue.component("video-uploader", EleFormVideoUploader);

// 此处省略其他包名及设置
Vue.use(lCharts);

//全局脚本，注册elment
Vue.config.productionTip = false;
Vue.use(ElementUI);
Vue.prototype.$http = http;
// Vue.use(Xcharts)


//路由守卫
router.beforeEach((to, from, next) => {
  // console.log(to);
  // console.log(from);
  if (to.meta.requireAuth) {
    // 判断该路由是否需要登录权限
    if (JSON.parse(localStorage.getItem("islogin"))) {
      //判断本地是否存在access_token
      next();
    } else {
      next({
        path: "/",
      });
    }
  } else {
    next();
  }
  /*如果本地 存在 token 则 不允许直接跳转到 登录页面*/
  // 防止登录一次后点击退出路由守卫失效
  if (to.fullPath == "/login") {
    if (JSON.parse(localStorage.getItem("islogin"))) {
      next({
        path: from.fullPath,
      });
    } else {
      next();
    }
  }
});
new Vue({
  store,
  router,
  render: (h) => h(App),
}).$mount("#app");
