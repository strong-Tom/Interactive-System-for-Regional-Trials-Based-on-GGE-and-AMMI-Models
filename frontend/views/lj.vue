<template>
    <div>
      <div style="text-align: center;"><h1>龙江地区历年气候情况</h1></div>
      <div v-show="0 === number">
        <div id="container_lj_tem" style="height: 300%; width: 100%"></div>
        <div id="container_lj_hum" style="height: 300%; width: 100%"></div>
        <div id="container_lj_sum" style="height: 300%; width: 100%"></div>
        <div id="container_lj_rai" style="height: 300%; width: 100%"></div>
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
        lj_tem: null,
        lj_hum: null,
        lj_sum: null,
        lj_rai: null,
        number: 0,
        date: null,
      };
    },
  
    mounted() {
      this.$axios({
        method: "get",
        url: "http://127.0.0.1:8000/api/compute_date/",
      }).then((res) => {
        // this.date=JSON.stringilj(res.data.date);
        this.date = res.data.date;
        //   console.log(this.date, typeof this.date);
      });
      this.$axios({
        method: "get",
        url: "http://127.0.0.1:8000/api/qx/",
      }).then((res) => {
        // this.date=JSON.stringilj(res.data.date);
        let lj_tem_list = [];
        let lj_hum_list = [];
        let lj_sum_list = [];
        let lj_rai_list = [];
  
        for (let i = 0; i < 108; i++) {
          lj_tem_list.push(res.data[i].lj_tem);
          lj_hum_list.push(res.data[i].lj_hum);
          lj_sum_list.push(res.data[i].lj_sum);
          lj_rai_list.push(res.data[i].lj_rai)
        }
        this.lj_tem = lj_tem_list;
        this.lj_hum = lj_hum_list;
        this.lj_sum = lj_sum_list;
        this.lj_rai = lj_rai_list;
      });
      setTimeout(() => {
        this.draw_lj_tem();
        this.draw_lj_hum();
        this.draw_lj_sum();
        this.draw_lj_rai();
      }, 1000);
    },
  
    methods: {
      lj() {
        top.location.href = "/#/lj";
      },
      draw_lj_tem() {
        var dom = document.getElementById("container_lj_tem");
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
              data: this.lj_tem,
            },
          ],
        };
  
        if (option && typeof option === "object") {
          myChart.setOption(option);
        }
  
        window.addEventListener("resize", myChart.resize);
      },
      draw_lj_hum() {
        var dom = document.getElementById("container_lj_hum");
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
              data: this.lj_hum,
            },
          ],
        };
  
        if (option && typeof option === "object") {
          myChart.setOption(option);
        }
  
        window.addEventListener("resize", myChart.resize);
      },
      draw_lj_sum() {
        var dom = document.getElementById("container_lj_sum");
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
              data: this.lj_sum,
            },
          ],
        };
  
        if (option && typeof option === "object") {
          myChart.setOption(option);
        }
  
        window.addEventListener("resize", myChart.resize);
      },
      draw_lj_rai() {
        var dom = document.getElementById("container_lj_rai");
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
              data: this.lj_rai,
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