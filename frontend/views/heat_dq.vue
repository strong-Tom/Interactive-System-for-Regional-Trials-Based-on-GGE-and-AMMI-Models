<template>
  <div>
    <div class="btn_switch">
      <button
        class="btn_anniu"
        @click="change(0)"
        :class="{ newStyle: 0 === number }"
      >
        径向增长量
      </button>
      <button
        class="btn_anniu"
        @click="change(1)"
        :class="{ newStyle: 1 === number }"
      >
        箱型图
      </button>
      <button
        class="btn_anniu"
        @click="change(2)"
        :class="{ newStyle: 2 === number }"
      >
        大庆地区相关性分析热力图
      </button>
      <button
        class="btn_anniu"
        @click="change(3)"
        :class="{ newStyle: 3 === number }"
      >
        大庆地区速生用材树种生长量汇总表
      </button>
      <el-button type="primary" size="default" @click="tz">
        跳转到下一个地点页面</el-button
      >
    </div>

    <div>
      <div v-show="0 === number">
        <div id="container" style="height: 600%"></div>
      </div>
      <div v-show="1 === number">
        <div
          style="display: flex; align-items: center; justify-content: center"
        >
          <img :src="src_box" />
        </div>
      </div>
      <div v-show="2 === number">
        <div
          style="display: flex; align-items: center; justify-content: center"
        >
          <img :src="src" />
        </div>
      </div>
      <!-- 大庆地区速生用材树种生长量汇总表 -->
      <div v-show="3 === number">
        <el-table
          :data="tableData"
          height="550px"
          border
          style="width: 100%"
          :header-cell-style="{ textAlign: 'center', color: '#000' }"
          :cell-style="{ textAlign: 'center' }"
        >
          <el-table-column prop="data1" label="地市"> </el-table-column>
          <el-table-column prop="data2" label="测定小区"> </el-table-column>
          <el-table-column prop="data3" label="地点"> </el-table-column>
          <el-table-column prop="data4" label="坡度"> </el-table-column>

          <el-table-column prop="data5" label="土壤类型"> </el-table-column>
          <el-table-column prop="data6" label="树种"> </el-table-column>
          <el-table-column prop="data7" label="林龄"> </el-table-column>

          <el-table-column prop="data8" label="密度(株/hm²)" width="120px">
          </el-table-column>
          <el-table-column label="总生长量">
            <el-table-column prop="data9" label="D1.3（cm）" width="120px">
            </el-table-column>
            <el-table-column prop="data10" label="H(m)"> </el-table-column>
            <el-table-column prop="data11" label="V(m³)"> </el-table-column>
          </el-table-column>
          <el-table-column label="年均生长量">
            <el-table-column prop="data12" label="D1.3（cm）" width="130">
            </el-table-column>
            <el-table-column prop="data13" label="H(m)"> </el-table-column>
            <el-table-column prop="data14" label="V(m³)"> </el-table-column>
          </el-table-column>

          <el-table-column
            prop="data15"
            label="年蓄积生长量(m³/hm²)"
            width="200px"
          >
          </el-table-column>
          <el-table-column prop="data16" label="备注"> </el-table-column>
        </el-table>
      </div>
    </div>
  </div>
</template>
    <script>
import * as echarts from "echarts";
export default {
  data() {
    return {
      number: 0,
      src: null,
      src_box: null,
      tableData: [
        {
          data1: "大庆(C)",
          data2: "泰康县（C1）",
          data3: "泰康镇",
          data4: "平",
          data5: "沙土",
          data6: "小黑杨",
          data7: 17,
          data8: 833,
          data9: 22.1,
          data10: 19,
          data11: 0.3323,
          data12: 1.3,
          data13: 1.12,
          data14: 0.0195,
          data15: 16.28,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "白音诺勒乡",
          data4: "平",
          data5: "沙土",
          data6: "银中杨",
          data7: 22,
          data8: 667,
          data9: 19.3,
          data10: 12.7,
          data11: 0.1687,
          data12: 0.88,
          data13: 0.58,
          data14: 0.0077,
          data15: 5.11,
          data16: "",
        },
        {
          data1: "",
          data2: "大同区(C1)",
          data3: "红旗林场",
          data4: "平",
          data5: "沙土",
          data6: "青山杨",
          data7: 17,
          data8: 1111,
          data9: 18.7,
          data10: 18,
          data11: 0.2283,
          data12: 1.1,
          data13: 1.06,
          data14: 0.0134,
          data15: 14.92,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "",
          data4: "平",
          data5: "沙土",
          data6: "小黑杨",
          data7: 17,
          data8: 1111,
          data9: 15.5,
          data10: 15.2,
          data11: 0.1338,
          data12: 0.91,
          data13: 0.89,
          data14: 0.0079,
          data15: 8.74,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "",
          data4: "平",
          data5: "沙土",
          data6: "中黑防",
          data7: 17,
          data8: 1111,
          data9: 18.1,
          data10: 19,
          data11: 0.227,
          data12: 1.06,
          data13: 1.12,
          data14: 0.0134,
          data15: 14.84,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "",
          data4: "平",
          data5: "沙土",
          data6: "银中杨",
          data7: 17,
          data8: 1111,
          data9: 23.3,
          data10: 18.5,
          data11: 0.3576,
          data12: 1.37,
          data13: 1.09,
          data14: 0.021,
          data15: 23.37,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "",
          data4: "平",
          data5: "沙土",
          data6: "小黑杨",
          data7: 6,
          data8: 2386,
          data9: 6,
          data10: 4.9,
          data11: 0.0067,
          data12: 1,
          data13: 0.82,
          data14: 0.0011,
          data15: 3.02,
          data16: "",
        },
        {
          data1: "",
          data2: "肇州县（C2）",
          data3: "丰乐苗圃",
          data4: "平",
          data5: "黑钙土",
          data6: "A43",
          data7: 16,
          data8: 1111,
          data9: 19.6,
          data10: 20.5,
          data11: 0.286,
          data12: 1.23,
          data13: 1.28,
          data14: 0.0179,
          data15: 19.86,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "",
          data4: "平",
          data5: "黑钙土",
          data6: "B6",
          data7: 16,
          data8: 1111,
          data9: 21.8,
          data10: 17,
          data11: 0.2884,
          data12: 1.36,
          data13: 1.06,
          data14: 0.018,
          data15: 20.03,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "",
          data4: "平",
          data5: "黑钙土",
          data6: "A15",
          data7: 16,
          data8: 833,
          data9: 22.6,
          data10: 21.5,
          data11: 0.3945,
          data12: 1.41,
          data13: 1.34,
          data14: 0.0247,
          data15: 20.54,
          data16: "病害重",
        },
        {
          data1: "",
          data2: "",
          data3: "",
          data4: "平",
          data5: "黑钙土",
          data6: "小黑杨",
          data7: 23,
          data8: 500,
          data9: 32.1,
          data10: 28,
          data11: 1.0151,
          data12: 1.4,
          data13: 1.22,
          data14: 0.0441,
          data15: 22.07,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "肇州镇肇安村",
          data4: "平",
          data5: "黑钙土",
          data6: "小黑14",
          data7: 17,
          data8: 500,
          data9: 27.2,
          data10: 24.3,
          data11: 0.6383,
          data12: 1.6,
          data13: 1.43,
          data14: 0.0375,
          data15: 18.77,
          data16: "",
        },
      ],
    };
  },
  methods: {
    tz() {
      this.$router.push({ path: "/heat_qq" });
    },
    change: function (index) {
      this.number = index; //重要处
    },
  },
  mounted() {
    this.$axios({
      method: "get",
      url: "http://127.0.0.1:8000/api/heat_dq/",
    }).then((res) => {
      console.log(res.data);
      console.log(res.data.src);
      this.src = res.data.src;
    });
    this.$axios({
      method: "get",
      url: "http://127.0.0.1:8000/api/draw_box_plot_dq/",
    }).then((res) => {
      console.log(res.data);
      console.log(res.data.src);
      this.src_box = res.data.src;
    });
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
        text: "大庆样地杨树品种径向增长量情况",
      },
      tooltip: {
        trigger: "axis",
      },
      legend: {
        data: ["小黑杨", "龙丰一号杨", "2111杨", "青山杨"],
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
        name: "径向增长量归一化值",
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
            0.258108312, 0.424035802, 0.608638809, 0.677517977, 0.257183084,
            0.239774727, 0.326263388, 0.151244532, 0.069854679, 0.140624529,
            0.103454518, 0.133403731, 0.079539398,
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
          name: "龙丰一号杨",
          type: "line",
          symbolSize: 20, //设定实心点的大小
          //   stack: "Total",
          data: [
            0.62413637, 0.376316186, 0.417901141, 0.66991502, 0.190496304,
            0.195323578, 0.227404837, 0.111892191, 0.08924423, 0.195645396,
            0.117674863, 0.178729824, 0.085875195,
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
          name: "2111杨",
          type: "line",
          symbolSize: 20, //设定实心点的大小
          //   stack: "Total",//数据堆叠
          data: [
            0.332036003, 0.360225273, 0.478684568, 0.84862473, 0.422547393,
            0.39996983, 0.264987178, 0.145894303, 0.181073063, 0.237049329,
            0.132227083, 0.248142002, 0.120209182,
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
        {
          name: "青山杨",
          type: "line",
          symbolSize: 20, //设定实心点的大小
          //   stack: "Total",//数据堆叠
          data: [
            0.69383014, 0.424307336, 0.568894253, 0.818363755, 0.366822547,
            0.230160406, 0.210770855, 0.123859808, 0.253934731, 0.356353397,
            0.249891889, 0.362588626, 0.156645045,
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
.btn_anniu {
  width: 20%;
  padding: 20px;
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