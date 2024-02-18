<template>
  <div id="container" style="height: 100%"></div>
</template>
      <script>
import * as echarts from "echarts";
export default {
  data() {
    return {};
  },
  methods: {},
  mounted() {
    var dom = document.getElementById("container");
    var myChart = echarts.init(dom, null, {
      renderer: "canvas",
      useDirtyRect: false,
    });
    var app = {};

    var option;

    option = {
      tooltip: {
        show: false,
        trigger: "item", //坐标轴触发，主要在柱状图，折线图等会使用类目轴的图表中使用
        axisPointer: {
          // 坐标轴指示器，坐标轴触发有效
          type: "shadow", // 默认为直线，可选为：'line' | 'shadow'
        },
        alwaysShowContent: false,
        //   backgroundColor: "rgba(36, 215, 309, 1)", //提示框背景色
        borderColor: "rgba(255, 255, 0, 1)",
        triggerOn: "mousemove",
        enterable: true, //鼠标是否可进入提示框浮层中
        textStyle: {
          fontSize: "12",
          overflow: "break",
        },
        //   position: ['50%', '50%'],
        // position: function (point, params, dom, rect, size) {
        //    return [point[0] - 100, '10%']  //返回x、y（横向、纵向）两个点的位置
        // },
        //tooltip显示框合理计算位置，不会对周边数据造成遮挡

        zIndex: 400,
        // extraCssText: "width:40%;height:30%;",
      },

      title: {
        text: "齐齐哈尔样地杨树品种径向增长量情况",
      },
      tooltip: {
        trigger: "axis",
      },
      legend: {
        data: ["小黑杨", "青山杨"],
      },
      grid: {
        left: "3%",
        right: "8%",
        bottom: "3%",
        containLabel: true,
      },
      toolbox: {
        feature: {
          saveAsImage: {},
        },
      },
      xAxis: {
        name: "年份",
        axisTick: {
          show: true, // 显示刻度线和标签
          inside: true, // 刻度线朝向内部
          length: 10, // 刻度线长度
          lineStyle: {
            // color: "red", // 刻度线颜色
          },
        },
        splitLine: { show: false },
        type: "category",
        boundaryGap: false,
        data: [
          2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020,
          2021, 2022,
        ],
      },
      yAxis: {
        type: "value",
        name: "径向增长量(m)",
        splitLine: { show: false },
        axisLine: {
          // symbol: ['none', 'arrow'], // 设置箭头方向为朝右
          // symbolSize: [18, 30], // 设置箭头大小
          show: true,
          // 设置坐标轴线为实线
          lineStyle: {
            type: "solid",
          },
        },
        axisTick: {
          show: true, // 显示刻度线和标签
          inside: true, // 刻度线朝向内部
          length: 10, // 刻度线长度
          lineStyle: {
            // color: "red", // 刻度线颜色
          },
        },
      },
      series: [
        {
          name: "小黑杨",
          type: "line",
          symbolSize: 20, //设定实心点的大小
          //   stack: "Total",
          data: [
            0.161685655, 0.347036749, 0.391358734, 0.510903006, 0.668937422,
            0.59569289, 0.381740424, 0.245292268, 0.218313668, 0.231566314,
            0.201460496, 0.196642889, 0.186635789,
          ],
          tooltip: {
            show: false,
            trigger: "item",
            // extraCssText: "max-width:40%;white-space:pre-wrap",
            extraCssText: "width:20%;height:40%;",
            //tooltip增加图片背景
            formatter: function (params) {
              var res = "小黑杨" + "<br/>";
              var str =
                res +
                `<div style = "background:url( ${require("@/assets/images/小黑杨.jpeg")}) no-repeat center center ;width:90%;height:90%;padding:22px 20px;font-size: 16px; background-size: contain;"></div>`;
              return str;
            },
          },
        },

        {
          name: "青山杨",
          type: "line",
          symbolSize: 20, //设定实心点的大小
          //   stack: "Total",//数据堆叠
          data: [
            0.48052109, 0.661482809, 0.571880952, 0.732851009, 0.742463685,
            0.52038045, 0.364154749, 0.200975918, 0.400238908, 0.303774074,
            0.200547686, 0.281280638, 0.130204988,
          ],
          tooltip: {
            show: false,
            trigger: "item",
            extraCssText: "max-width:40%;white-space:pre-wrap",
            extraCssText: "width:20%;height:40%;",
            //tooltip增加图片背景
            formatter: function (params) {
              var res = "小黑杨" + "<br/>";
              var str =
                res +
                `<div style = "background:url( ${require("@/assets/images/小黑杨.jpeg")}) no-repeat center center ;width:90%;height:90%;padding:22px 20px;font-size: 16px; background-size: contain;"></div>`;
              return str;
            },
          },
        },
      ],
    };

    if (option && typeof option === "object") {
      myChart.setOption(option);
    }

    window.addEventListener("resize", myChart.resize);
  },
};
</script>
      <style lang="less" scoped>
</style>