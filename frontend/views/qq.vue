<template>
    <div>
      <div style="text-align: center;"><h1>齐齐哈尔地区历年气候情况</h1></div>
      <div v-show="0 === number">
        <div id="container_qq_tem" style="height: 300%; width: 100%"></div>
        <div id="container_qq_hum" style="height: 300%; width: 100%"></div>
        <div id="container_qq_sum" style="height: 300%; width: 100%"></div>
        <div id="container_qq_rai" style="height: 300%; width: 100%"></div>
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
        qq_tem: null,
        qq_hum: null,
        qq_sum: null,
        qq_rai: null,
        number: 0,
        date: null,
      };
    },
  
    mounted() {
      this.$axios({
        method: "get",
        url: "http://127.0.0.1:8000/api/compute_date/",
      }).then((res) => {
        // this.date=JSON.stringiqq(res.data.date);
        this.date = res.data.date;
        //   console.log(this.date, typeof this.date);
      });
      this.$axios({
        method: "get",
        url: "http://127.0.0.1:8000/api/qx/",
      }).then((res) => {
        // this.date=JSON.stringiqq(res.data.date);
        let qq_tem_list = [];
        let qq_hum_list = [];
        let qq_sum_list = [];
        let qq_rai_list = [];
  
        for (let i = 0; i < 108; i++) {
          qq_tem_list.push(res.data[i].qq_tem);
          qq_hum_list.push(res.data[i].qq_hum);
          qq_sum_list.push(res.data[i].qq_sum);
          qq_rai_list.push(res.data[i].qq_rai)
        }
        this.qq_tem = qq_tem_list;
        this.qq_hum = qq_hum_list;
        this.qq_sum = qq_sum_list;
        this.qq_rai = qq_rai_list;
      });
      setTimeout(() => {
        this.draw_qq_tem();
        this.draw_qq_hum();
        this.draw_qq_sum();
        this.draw_qq_rai();
      }, 1000);
    },
  
    methods: {
      qq() {
        top.location.href = "/#/qq";
      },
      draw_qq_tem() {
        var dom = document.getElementById("container_qq_tem");
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
              data: this.qq_tem,
            },
          ],
        };
  
        if (option && typeof option === "object") {
          myChart.setOption(option);
        }
  
        window.addEventListener("resize", myChart.resize);
      },
      draw_qq_hum() {
        var dom = document.getElementById("container_qq_hum");
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
              data: this.qq_hum,
            },
          ],
        };
  
        if (option && typeof option === "object") {
          myChart.setOption(option);
        }
  
        window.addEventListener("resize", myChart.resize);
      },
      draw_qq_sum() {
        var dom = document.getElementById("container_qq_sum");
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
              data: this.qq_sum,
            },
          ],
        };
  
        if (option && typeof option === "object") {
          myChart.setOption(option);
        }
  
        window.addEventListener("resize", myChart.resize);
      },
      draw_qq_rai() {
        var dom = document.getElementById("container_qq_rai");
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
              data: this.qq_rai,
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