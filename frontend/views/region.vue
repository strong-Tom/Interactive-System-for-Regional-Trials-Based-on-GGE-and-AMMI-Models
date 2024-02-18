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
        // show: false,
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
        position: function (point, params, dom, rect, size) {
          // 鼠标坐标和提示框位置的参考坐标系是：以外层div的左上角那一点为原点，x轴向右，y轴向下
          // 提示框位置
          var x = 0; // x坐标位置
          var y = 0; // y坐标位置

          // 当前鼠标位置
          var pointX = point[0];
          var pointY = point[1];
          // 提示框大小
          var boxWidth = size.contentSize[0];
          var boxHeight = size.contentSize[1];

          // boxWidth > pointX 说明鼠标左边放不下提示框
          if (boxWidth > pointX) {
            x = 5;
          } else {
            // 左边放的下
            x = pointX - boxWidth;
          }

          // boxHeight > pointY 说明鼠标上边放不下提示框
          if (boxHeight > pointY) {
            y = 5;
          } else {
            // 上边放得下
            y = pointY - boxHeight;
          }
          return [x, y];
        },

        zIndex: 400,
        // extraCssText: "width:410%;height:310%;",
      },

      title: {
        text: "各地树高对比",
      },
      tooltip: {
        trigger: "axis",
      },
      legend: {
        data: [
          "小黑杨",
          "小黑14",
          "银中杨",
          "大青杨",
          "青山杨",
          "A43",
          "A15",
          "中黑防",
          "中绥12",
          "迎春5号",
        ],
      },
      grid: {
        left: "3%",
        right: "4%",
        bottom: "3%",
        containLabel: true,
      },
      toolbox: {
        feature: {
          saveAsImage: {},
        },
      },
      xAxis: {
        name: "区域",
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
        data: ["(Ⅰ)区", "(Ⅱ)区", "(Ⅲ)区", "(Ⅳ)区", "(Ⅴ)区"],
      },
      yAxis: {
        name: "树高(m)",
        splitLine: { show: false },
        type: "value",
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
          // type: "scatter",
          type: "scatter",
          symbolSize: 20, //设定实心点的大小
          // symbol: 'triangle',

          symbol: "emptyCircle",
          //   stack: "Total",
          data: [20.7, 23.4, 28, 17, 20],
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
                `<div style = "background:url( ${require("@/assets/images/tree/小黑杨叶片.png")}) no-repeat center center ;width:80%;height:90%;padding:22px 20px;font-size: 16px; background-size: contain;"></div>`;
              return str;
            },
          },
        },
        {
          name: "小黑14",
          type: "scatter",
          symbolSize: 20, //设定实心点的大小
          // symbol: 'rect',
          //   stack: "Total",
          // connectNulls: true,
          data: [18, 16.4, 15.9, ,],
          tooltip: {
            show: false,
            trigger: "item",
            // extraCssText: "max-width:40%;white-space:pre-wrap",
            extraCssText: "width:20%;height:40%;",
            //tooltip增加图片背景
            formatter: function (params) {
              var res = "小黑14" + "<br/>";
              var str =
                res +
                `<div style = "background:url( ${require("@/assets/images/小黑14.jpg")}) no-repeat center center ;width:90%;height:100%;padding:22px 20px;font-size: 16px; background-size: contain;"></div>`;
              return str;
            },
          },
        },
        {
          name: "银中杨",
          type: "scatter",
          symbolSize: 20, //设定实心点的大小
          // symbol: 'arrow',

          symbol: "emptyCircle",
          //   stack: "Total",//数据堆叠
          data: [16.8, 16.5, 15.5, , 7.5],
          tooltip: {
            show: false,
            trigger: "item",
            // extraCssText: "max-width:40%;white-space:pre-wrap",
            extraCssText: "width:20%;height:40%;",
            //tooltip增加图片背景
            formatter: function (params) {
              var res = "银中杨" + "<br/>";
              var str =
                res +
                `<div style = "background:url( ${require("@/assets/images/tree/银中杨叶片.png")}) no-repeat center center ;width:90%;height:90%;padding:22px 20px;font-size: 16px; background-size: contain;"></div>`;
              return str;
            },
          },
        },
        {
          name: "大青杨",
          type: "scatter",
          symbolSize: 20, //设定实心点的大小
          //   stack: "Total",//数据堆叠
          // symbol: 'diamond',
          data: [20.9, , 22.2, ,],
          tooltip: {
            show: false,
            trigger: "item",
            // extraCssText: "max-width:40%;white-space:pre-wrap",
            extraCssText: "width:20%;height:40%;",
            //tooltip增加图片背景
            formatter: function (params) {
              var res = "大青杨" + "<br/>";
              var str =
                res +
                `<div style = "background:url( ${require("@/assets/images/大青杨.png")}) no-repeat center center ;width:90%;height:90%;padding:22px 20px;font-size: 16px; background-size: contain;"></div>`;
              return str;
            },
          },
        },
        {
          name: "青山杨",
          type: "scatter",
          symbolSize: 20, //设定实心点的大小

          symbol: "emptyCircle",
          //   stack: "Total",//数据堆叠
          data: [3.6, 8.9, 18.7, 7.4, 7.2],
          tooltip: {
            show: false,
            trigger: "item",
            // extraCssText: "max-width:40%;white-space:pre-wrap",
            extraCssText: "width:20%;height:40%;",
            //tooltip增加图片背景
            formatter: function (params) {
              var res = "青山杨" + "<br/>";
              var str =
                res +
                `<div style = "background:url( ${require("@/assets/images/tree/青山杨叶片.png")}) no-repeat center center ;width:90%;height:90%;padding:22px 20px;font-size: 16px; background-size: contain;"></div>`;
              return str;
            },
          },
        },
        {
          name: "A43",
          type: "scatter",
          symbolSize: 20, //设定实心点的大小
          //   stack: "Total",//数据堆叠
          data: [10.1, , 20.5, ,],
          tooltip: {
            show: false,
            trigger: "item",
            // extraCssText: "max-width:40%;white-space:pre-wrap",
            extraCssText: "width:20%;height:40%;",
            //tooltip增加图片背景
            formatter: function (params) {
              var res = "A43" + "<br/>";
              var str =
                res +
                `<div style = "background:url( ${require("@/assets/images/s.jpeg")}) no-repeat center center ;width:90%;height:90%;padding:22px 20px;font-size: 16px; background-size: contain;"></div>`;
              return str;
            },
          },
        },
        {
          name: "A15",
          type: "scatter",
          symbolSize: 20, //设定实心点的大小

          symbol: "emptyCircle",
          //   stack: "Total",//数据堆叠
          data: [20.7, , 21.5, ,],
          tooltip: {
            show: false,
            trigger: "item",
            // extraCssText: "max-width:40%;white-space:pre-wrap",
            extraCssText: "width:20%;height:40%;",
            //tooltip增加图片背景
            formatter: function (params) {
              var res = "A15" + "<br/>";
              var str =
                res +
                `<div style = "background:url( ${require("@/assets/images/s.jpeg")}) no-repeat center center ;width:90%;height:90%;padding:22px 20px;font-size: 16px; background-size: contain;"></div>`;
              return str;
            },
          },
        },
        {
          name: "中黑防",
          type: "scatter",
          symbolSize: 20, //设定实心点的大小
          //   stack: "Total",//数据堆叠
          data: [7.5, , 19, , 10.5],
          tooltip: {
            show: false,
            trigger: "item",
            // extraCssText: "max-width:40%;white-space:pre-wrap",
            extraCssText: "width:20%;height:40%;",
            //tooltip增加图片背景
            formatter: function (params) {
              var res = "中黑防" + "<br/>";
              var str =
                res +
                `<div style = "background:url( ${require("@/assets/images/中黑防.png")}) no-repeat center center ;width:90%;height:90%;padding:22px 20px;font-size: 16px; background-size: contain;"></div>`;
              return str;
            },
          },
        },
        {
          name: "中绥12",
          type: "scatter",
          symbolSize: 20, //设定实心点的大小
          //   stack: "Total",//数据堆叠

          symbol: "emptyCircle",
          data: [, , 16, , 16],
          tooltip: {
            show: false,
            trigger: "item",
            // extraCssText: "max-width:40%;white-space:pre-wrap",
            extraCssText: "width:20%;height:40%;",
            //tooltip增加图片背景
            formatter: function (params) {
              var res = "中绥12" + "<br/>";
              var str =
                res +
                `<div style = "background:url( ${require("@/assets/images/中绥12.jpg")}) no-repeat center center ;width:90%;height:100%;padding:22px 20px;font-size: 16px; background-size: contain;"></div>`;
              return str;
            },
          },
        },
        {
          name: "迎春5号",
          type: "scatter",
          symbolSize: 20, //设定实心点的大小
          //   stack: "Total",//数据堆叠
          data: [17.3, 10.5, , , 20.7],
          tooltip: {
            show: false,
            trigger: "item",
            // extraCssText: "max-width:40%;white-space:pre-wrap",
            extraCssText: "width:20%;height:40%;",
            //tooltip增加图片背景
            formatter: function (params) {
              var res = "迎春5号" + "<br/>";
              var str =
                res +
                `<div style = "background:url( ${require("@/assets/images/迎春5号.png")}) no-repeat center center ;width:90%;height:90%;padding:22px 20px;font-size: 16px; background-size: contain;"></div>`;
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