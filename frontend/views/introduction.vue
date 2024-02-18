<template>
    <div class="big">
      <!-- <el-image
        :src="require('@/assets/images/tree.jpeg')"
        fit="fill"
        :lazy="true"
      ></el-image> -->
      <div class="image">
        <el-card class="box-card">
          <!-- <h2>Welcome to Expert system for suitable tree in plantation</h2> -->
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
      width: 50%;
      height: 80%;
      background: url("../src/assets/images/功能图.png");
      background-size:cover;
      .box-card {
        position:absolute;
        left: 10%;
        top: 40%;
  
      }
    }
  }
  </style>