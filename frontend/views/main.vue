<template>
  <el-container style="height: 100%">
    <el-aside width="auto">
      <!-- 自定义的CommonAside组件 -->
      <common-aside></common-aside>
    </el-aside>
    <el-container>
      <el-header>
        <!-- 自定义的CommonHeader组件 -->
        <common-header></common-header>
      </el-header>
      <el-main>
        <!-- 只在main部分显示路由 -->
        <router-view></router-view>
      </el-main>
    </el-container>
  </el-container>

</template>
<script>
import CommonAside from "../src/components/CommonAside";
import CommonHeader from "../src/components/CommonHeader";
export default {
  name: "main",
  components: {
    CommonAside,
    CommonHeader,
  },
  data() {
    return {};
  },
};
</script>

<style lang="less" scoped>
.el-header {
  background-color: #333;
}
.el-main {
  padding-top: 0px;
}
</style>
