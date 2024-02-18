<template>
  <div > 
    <el-row :gutter="20">
      <el-col :span="10"
        ><div class="grid-content bg-purple">
          <div style="text-align: center;  line-height"></div>
          <img
            src="@/assets/images/t21.jpg"
            alt=""
            style=" background: no-repeat center center; width: 100%;
              height: 100%;
              margin: 20px;
            "
          /></div
      ></el-col>
      <el-col :span="12"
        ><div class="grid-content bg-purple">
          <div style="text-align: center;  line-height"></div>
          <img
            src="@/assets/images/t22.jpg"
            alt=""
            style=" background: no-repeat center center;width: 80%;
              height: 80%;
              margin: 20px;
            "
          /></div
      ></el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: "FrontendShowImg",

  data() {
    return {};
  },

  mounted() {},

  methods: {},
};
</script>

<style lang="less" scoped>
</style>