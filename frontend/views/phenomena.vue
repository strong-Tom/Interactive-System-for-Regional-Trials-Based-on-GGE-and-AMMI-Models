<template>
  <div class="main">
    <div style="text-align: center" class="box">
      <div style="margin-bottom: 30px">
        <h1>松嫩平原杨树栽培区历年气象数据</h1>
      </div>
      <el-button type="primary" size="default" @click="fy" >富裕</el-button>
      <el-button type="primary" size="default" @click="qq">齐齐哈尔</el-button>
      <el-button type="primary" size="default" @click="lj">龙江</el-button>
      <el-button type="primary" size="default" @click="dq">大庆</el-button>
      <el-button type="primary" size="default" @click="hr">哈尔滨</el-button>
      <el-button type="primary" size="default" @click="nh">讷河</el-button>
      <el-button type="primary" size="default" @click="gn">甘南</el-button>
    </div>
  </div>
</template>

<script>
import * as echarts from "echarts";
import { timeout } from "q";
export default {
  name: "FrontendPhenomena",

  data() {
    return {};
  },

  methods: {
    fy() {
      top.location.href = "/#/fy";
    },
    qq() {
      top.location.href = "/#/qq";
    },
    lj() {
      top.location.href = "/#/lj";
    },
    dq() {
      top.location.href = "/#/dq";
    },
    hr() {
      top.location.href = "/#/hr";
    },
    nh() {
      top.location.href = "/#/nh";
    },
    gn() {
      top.location.href = "/#/gn";
    },
    change: function (index) {
      this.number = index; //重要处
    },
  },
};
</script>

<style lang="less" scoped>
.el-button {
    width: 14vw;
    margin: 20px;
    font-size: 20px;
}
.btn_anniu {
  width: 14%;
  padding: 20px 0;
  font-size: 15px;
  font-weight: bold;
  border: 0 solid #fff;
  color: #000;
  outline: none;
  background: #fff;
}
.newStyle {
  border-bottom: 2px solid #f0892e;
  color: #f0892e;
  font-size: 15px;
  font-weight: bold;
}
.main {
  width: 100%;
  height: 100%;
  position: relative;
  // background: pink;
  .box {
    position: absolute;
    top: 20%;
    left: 5%;
    // background: red;
  }
}
</style>