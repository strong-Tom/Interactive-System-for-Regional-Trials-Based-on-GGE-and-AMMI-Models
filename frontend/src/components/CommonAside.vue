<template>
  <el-menu
    default-active="1-4-1"
    class="el-menu-vertical-demo"
    @open="handleOpen"
    @close="handleClose"
    :collapse="isCollapse"
    background-color="#545c64"
    text-color="white"
    active-text-color="yellow"
  >
    <!-- <h4  style='text-align: center'>{{isCollapse?'系统':'人工林适地适树专家系统'}}</h4> -->

    <el-submenu index="1-4">
          <template slot="title">Front Page</template>
          <el-menu-item index="1-4-1" @click="()=>{this.$router.push('/home')}">Home</el-menu-item>
          <el-menu-item index="1-4-2" @click="()=>{this.$router.push('/introduction')}">Introduction</el-menu-item>
        </el-submenu>
    
    <!-- 一级菜单 -->
    <el-menu-item
      v-for="item in noChildren"
      :index="item.path"
      :key="item.path"
      @click="clickMenu(item)"
    >
      <i :class="'el-icon-' + item.icon"></i>
      <span slot="title">{{ item.label }}</span>
    </el-menu-item>

    <!-- 二级菜单 -->
    <!-- 1 -->
    <el-submenu
    
      v-for="item in hasChildren"
      :index="item.label"
      :key="item.label"
    >
      <template slot="title">
        <i :class="'el-icon-' + item.icon"></i>
        <span slot="title">{{ item.label }}</span>
      </template>
      <!-- 2 -->
      <el-menu-item-group v-for="subitem in item.children" :key="subitem.path">
        <el-menu-item @click="clickMenu(subitem)" :index="subitem.label">
          {{ subitem.label }}
        </el-menu-item>
      </el-menu-item-group>
    </el-submenu>
    <!-- test选项 -->
    <!-- <el-menu-item
      @click="
        () => {
          this.$router.push({ path: '/test' });
        }
      "
    >
      <h2>test</h2>
    </el-menu-item> -->
    <!-- test选项 -->
  </el-menu>
</template>
<style lang="less" scoped>
@import "../assets/less/CommonAside.less";
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 18vw;
  min-height: 400px;
}
.el-menu {
  height: 100%;
  border: none;
  .h3 {
    color: #fff;
    text-align: center;
    line-height: 48px;
  }
}

</style>
<script>
export default {
  data() {
    return {
      // isCollapse: false,
      menu: [

        // 无子菜单
        // {
        //   path: "/",
        //   name: "home",
        //   label: "Front Page",
        //   icon: "s-home",
        //   url: "Home/Home",
        // },
        {
          path: "/map",
          name: "map",
          label: "Map",
          icon: "map-location",
          url: "/map",
        },
        // 有子菜单
        // {
        //   path: "/uploadExcel",
        //   name: "uploadExcel",
        //   label: "file download",
        //   icon: "files",
        //   url: "/uploadExcel",
        // },
        {
          path: "/uploadExcel",
          name: "uploadExcel",
          label: "Example Data",
          icon: "files",
          url: "/uploadExcel",
        },

          {
          label: "GGE Model",
          icon: "crop",
          children: [
            {
              path: "/variety_yield_and_stability",
              name: "variety_yield_and_stability",
              label: "Variety Yield and Stability",
              icon: "right",
            },
            {
              path: "/which_won_where",
              name: "which_won_where",
              label: "Which won Where",
              icon: "crop",
            },
          ],
        },

        {
          label: "User Management",
          icon: "setting",
          children: [
            {
              path: "/modifyUser",
              name: "modifyUser",
              label: "Modify User",
              icon: "setting",
            },
            {
              path: "/modifyPassword",
              name: "modifyPassword",
              label: "Change Password",
              icon: "setting",
            },
          ],
        },
        // {
        //   path: "/tree",
        //   name: "tree",
        //   label: "preview data",
        //   icon: "s-management",
        //   // url: "MallManage/MallManage",
        // },
        // {
        //   path: "/uploadVideo",
        //   name: "uploadVideo",
        //   label: "上传视频",
        //   icon: "upload",
        //   url: "/uploadVideo",
        // },


        // {
        //   path: "/featureExtraction",
        //   name: "featureExtraction",
        //   label: "特征提取",
        //   icon: "loading ",
        //   url: "/featureExtraction",
        // },
        // {
        //   path: "/ruleExtraction",
        //   name: "ruleExtraction",
        //   label: "规则生成",
        //   icon: "s-grid",
        //   url: "/ruleExtraction",
        // },
        {
          path: "/scatter",
          name: "scatter",
          label: "Scatter",
          icon: "more",
          url: "/scatter",
        },
        {
          path: "/AMMI",
          name: "AMMI",
          label: "AMMI Model",
          icon: "crop",
          url: "/AMMI",
        },

      ],
    };
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
    clickMenu(item) {
      this.$router.push({
        name: item.name,
      });
      this.$store.commit("selectMenu", item);
    },
  },
  computed: {
    noChildren() {
      return this.menu.filter((item) => !item.children);
    },
    hasChildren() {
      return this.menu.filter((item) => item.children);
    },
    isCollapse() {
      return this.$store.state.tab.isCollapse;
    },
  },
};
</script>
