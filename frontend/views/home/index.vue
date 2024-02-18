<template>
  <div class="big">
    <!-- <el-image
      :src="require('../../src/assets/images/tree.jpeg')"
      fit="fill"
      :lazy="true"
    ></el-image> -->
    <div class="image">
      <el-card class="box-card">
        <!-- <h2>Welcome to the Expert system for Poplar-site Matching in Songnen Plain</h2> -->
      </el-card>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {};
  },
  methods: {},
  mounted() {},
};
</script>
<style lang="less" scoped>
.big {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  .image {
    // border: 3px outset #ff0000;
    position: relative;
    width: 1600px;
    height: 800px;
    width: 100%;
    height: 100%;
    background: url("../../src/assets/images/tree.jpeg");
    background-size:cover;
    .box-card {
      position:absolute;
      left: 10%;
      top: 40%;

    }
  }
}
</style>