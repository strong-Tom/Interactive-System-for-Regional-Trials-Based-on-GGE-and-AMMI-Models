<template>
  <div>
    <div style="text-align: center;"><h1>富裕地区历年气候情况</h1></div>
    <div v-show="0 === number">
      <div id="container_fy_tem" style="height: 300%; width: 100%"></div>
      <div id="container_fy_hum" style="height: 300%; width: 100%"></div>
      <div id="container_fy_sum" style="height: 300%; width: 100%"></div>
      <div id="container_fy_rai" style="height: 300%; width: 100%"></div>
    </div>
  </div>
</template>
  
  <script>
import * as echarts from "echarts";
import { timeout } from "q";
export default {
  name: "FrontendPhenomena",

  data() {
    return {
      fy_tem: null,
      fy_hum: null,
      fy_sum: null,
      fy_rai: null,
      number: 0,
      date: null,
    };
  },

  mounted() {
    this.$axios({
      method: "get",
      url: "http://127.0.0.1:8000/api/compute_date/",
    }).then((res) => {
      // this.date=JSON.stringify(res.data.date);
      this.date = res.data.date;
      //   console.log(this.date, typeof this.date);
    });
    this.$axios({
      method: "get",
      url: "http://127.0.0.1:8000/api/qx/",
    }).then((res) => {
      // this.date=JSON.stringify(res.data.date);
      let fy_tem_list = [];
      let fy_hum_list = [];
      let fy_sum_list = [];
      let fy_rai_list = [];

      for (let i = 0; i < 108; i++) {
        fy_tem_list.push(res.data[i].fy_tem);
        fy_hum_list.push(res.data[i].fy_hum);
        fy_sum_list.push(res.data[i].fy_sum);
        fy_rai_list.push(res.data[i].fy_rai)
      }
      this.fy_tem = fy_tem_list;
      this.fy_hum = fy_hum_list;
      this.fy_sum = fy_sum_list;
      this.fy_rai = fy_rai_list;
    });
    setTimeout(() => {
      this.draw_fy_tem();
      this.draw_fy_hum();
      this.draw_fy_sum();
      this.draw_fy_rai();
    }, 1000);
  },

  methods: {
    fy() {
      top.location.href = "/#/fy";
    },
    draw_fy_tem() {
      var dom = document.getElementById("container_fy_tem");
      var myChart = echarts.init(dom, null, {
        renderer: "canvas",
        useDirtyRect: false,
      });
      var app = {};

      var option;

      option = {
        title: {
          text: "月均温度折线图",
        },
        tooltip: {
          trigger: "axis",
        },
        legend: {
          data: ["月均日照时数"],
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
          data: this.date,
        },
        yAxis: {
          type: "value",
          name: "月均温度(°C)",
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
            name: "月均温度(°C)",
            type: "line",
            symbolSize: 20, //设定实心点的大小
            //   stack: "Total",
            // data: [
            //   4.8, 6.0, 7.6, 9.2, 10.7, 12.4, 13.9, 15.4, 16.2, 16.8, 17.4,
            //   17.9, 18.3,
            // ],
            data: this.fy_tem,
          },
        ],
      };

      if (option && typeof option === "object") {
        myChart.setOption(option);
      }

      window.addEventListener("resize", myChart.resize);
    },
    draw_fy_hum() {
      var dom = document.getElementById("container_fy_hum");
      var myChart = echarts.init(dom, null, {
        renderer: "canvas",
        useDirtyRect: false,
      });
      var app = {};

      var option;

      option = {
        title: {
          text: "空气相对湿度折线图",
        },
        tooltip: {
          trigger: "axis",
        },
        legend: {
          data: ["空气相对湿度(%)"],
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
          data: this.date,
        },
        yAxis: {
          type: "value",
          name: "空气相对湿度(%)",
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
            name: "空气相对湿度(%)",
            type: "line",
            symbolSize: 20, //设定实心点的大小
            //   stack: "Total",
            // data: [
            //   4.8, 6.0, 7.6, 9.2, 10.7, 12.4, 13.9, 15.4, 16.2, 16.8, 17.4,
            //   17.9, 18.3,
            // ],
            data: this.fy_hum,
          },
        ],
      };

      if (option && typeof option === "object") {
        myChart.setOption(option);
      }

      window.addEventListener("resize", myChart.resize);
    },
    draw_fy_sum() {
      var dom = document.getElementById("container_fy_sum");
      var myChart = echarts.init(dom, null, {
        renderer: "canvas",
        useDirtyRect: false,
      });
      var app = {};

      var option;

      option = {
        title: {
          text: "月均日照时数折线图",
        },
        tooltip: {
          trigger: "axis",
        },
        legend: {
          data: ["月均日照时数 (小时）"],
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
          data: this.date,
        },
        yAxis: {
          type: "value",
          name: "月均日照时数 (小时）",
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
            name: "月均日照时数 (小时）",
            type: "line",
            symbolSize: 20, //设定实心点的大小
            //   stack: "Total",
            // data: [
            //   4.8, 6.0, 7.6, 9.2, 10.7, 12.4, 13.9, 15.4, 16.2, 16.8, 17.4,
            //   17.9, 18.3,
            // ],
            data: this.fy_sum,
          },
        ],
      };

      if (option && typeof option === "object") {
        myChart.setOption(option);
      }

      window.addEventListener("resize", myChart.resize);
    },
    draw_fy_rai() {
      var dom = document.getElementById("container_fy_rai");
      var myChart = echarts.init(dom, null, {
        renderer: "canvas",
        useDirtyRect: false,
      });
      var app = {};

      var option;

      option = {
        title: {
          text: "月均降雨量折线图",
        },
        tooltip: {
          trigger: "axis",
        },
        legend: {
          data: ["月均降雨量 (mm)"],
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
          data: this.date,
        },
        yAxis: {
          type: "value",
          name: "月均降雨量 (mm)",
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
            name: "月均降雨量 (mm)",
            type: "line",
            symbolSize: 20, //设定实心点的大小
            //   stack: "Total",
            // data: [
            //   4.8, 6.0, 7.6, 9.2, 10.7, 12.4, 13.9, 15.4, 16.2, 16.8, 17.4,
            //   17.9, 18.3,
            // ],
            data: this.fy_rai,
          },
        ],
      };

      if (option && typeof option === "object") {
        myChart.setOption(option);
      }

      window.addEventListener("resize", myChart.resize);
    },

    // ------------------------------------------

    change: function (index) {
      this.number = index; //重要处
    },
  },
};
</script>
  
  <style lang="less" scoped>
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
</style>