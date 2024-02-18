//vuex，管理其他模块
import Vue from "vue";
import Vuex from "vuex";
import tab from "./tab";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    tab,
  },
  state: {
    //是否登录判断
    islogin: "",
  },
  mutations: {
    login: (state, n) => {
      //传入登录状态islogin
      let islogin = JSON.parse(n);
      localStorage.setItem("islogin", JSON.stringify(islogin));
    //   console.log('登录状态：',islogin);
      state.islogin = islogin;
    },
  },
});
