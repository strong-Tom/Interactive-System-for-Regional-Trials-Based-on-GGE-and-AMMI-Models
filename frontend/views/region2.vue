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
        

        show: true,
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
        text: "银中杨生长指标(平均树高)",
      },
      tooltip: {
        trigger: "axis",
      },
      legend: {
        data: [
          "Ⅰ(三江平原栽培区)",
          "Ⅱ(松嫩平原东部栽培区)",
          "Ⅲ(松嫩平原西部栽培区)",
        ],
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
        name: "树龄(年)",
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
          "3",
          "4",
          "5",
          "6",
          "7",
          "8",
          "9",
          "10",
          "11",
          "12",
          "13",
          "14",
          "15",
        ],
      },
      yAxis: {
        type: "value",
        name: "树高(m)",
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
          name: "Ⅰ(三江平原栽培区)",
          type: "line",
          symbolSize: 20,   //设定实心点的大小  
        //   stack: "Total",
          data: [
            5.0, 7.0, 9.0, 11.0, 12.5, 14.5, 16.0, 17.0, 18.5, 19.5, 20.5, 21.5,
            22.0,
          ],
          tooltip: {
            show: false,
            trigger: "item",
            // extraCssText: "max-width:40%;white-space:pre-wrap",
            extraCssText: "width:20%;height:40%;",
            //tooltip增加图片背景
            formatter: function (params) {
                var res = "银中杨" + "<br/>";
              var str = res+`<div style = "background:url( ${require("@/assets/images/银中杨.jpg")}) no-repeat center center ;width:90%;height:90%;padding:22px 20px;font-size: 16px; background-size: contain;"></div>`;
              return str;
            },
          },
        },
        {
          name: "Ⅱ(松嫩平原东部栽培区)",
          type: "line",
          symbolSize: 20,   //设定实心点的大小  
        //   stack: "Total",
          data: [
            4.5, 6.5, 8.5, 10.5, 12, 13.5, 15, 16.5, 17.5, 19, 19.5, 20.5,
            21,
          ],
          tooltip: {
            show: false,
            trigger: "item",
            // extraCssText: "max-width:40%;white-space:pre-wrap",
            extraCssText: "width:20%;height:40%;",
            //tooltip增加图片背景
            formatter: function (params) {
                var res = "银中杨" + "<br/>";
              var str = res+`<div style = "background:url( ${require("@/assets/images/银中杨.jpg")}) no-repeat center center ;width:90%;height:90%;padding:22px 20px;font-size: 16px; background-size: contain;"></div>`;
              return str;
            },
          },
        },
        {
          name: "Ⅲ(松嫩平原西部栽培区)",
          type: "line",
          symbolSize: 20,   //设定实心点的大小  
        //   stack: "Total",//数据堆叠
          data: [
            4, 6, 8, 10, 11.5, 13.5, 15, 16, 17.5, 18.5, 19.5, 20,
            20.5,
          ],
          tooltip: {
            show: false,
            trigger: "item",
            extraCssText: "max-width:40%;white-space:pre-wrap",
            extraCssText: "width:20%;height:40%;",
            //tooltip增加图片背景
            formatter: function (params) {
                var res = "银中杨" + "<br/>";
              var str = res+`<div style = "background:url( ${require("@/assets/images/银中杨.jpg")}) no-repeat center center ;width:90%;height:90%;padding:22px 20px;font-size: 16px; background-size: contain;"></div>`;
              return str;
            },
          },
        },
        // {
        //   name: 'Direct',
        //   type: 'line',
        //   stack: 'Total',
        //   data: [320, 332, 301, 334, 390, 330, 320]
        // },
        // {
        //   name: 'Search Engine',
        //   type: 'line',
        //   stack: 'Total',
        //   data: [820, 932, 901, 934, 1290, 1330, 1320]
        // }
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