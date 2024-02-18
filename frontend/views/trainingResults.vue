<template>
  <div>
    <div
      style="
        display: flex;
        justify-content: center;
        align-items: center;
        color: red;
      "
    >
      <!-- <h2>提取完成，以下为结果</h2> -->
    </div>
    <div class="btn_switch">
      <button
        class="btn_anniu"
        @click="change(0)"
        :class="{ newStyle: 0 === number }"
      >
        表格
      </button>
      <button
        class="btn_anniu"
        @click="change(1)"
        :class="{ newStyle: 1 === number }"
      >
        特征重要性散点图
      </button>
      <button
        class="btn_anniu"
        @click="change(2)"
        :class="{ newStyle: 2 === number }"
      >
        饼图
      </button>
      <button
        class="btn_anniu"
        @click="change(3)"
        :class="{ newStyle: 3 === number }"
      >
        roc曲线
      </button>
    </div>
    <div>
      <div v-show="0 === number">
        <div style="display: flex; justify-content: space-evenly">
          <!-- 表格 -->
          <div>
            <el-table
              :data="this.vimps_json"
              border
              @selection-change="changeFun"
              ref="multipleTable"
              style="
                width: 100%;
                height: 400px;
                overflowx: hidden;
                overflow-y: auto;
              "
            >
              <el-table-column prop="name" label="特征名称" width="200">
              </el-table-column>
              <el-table-column prop="value" label="值" width="200">
              </el-table-column>
              <el-table-column
                type="selection"
                width="55"
                @selection-change="changeFun"
                :reserve-selection="true"
              >
              </el-table-column>
            </el-table>
          </div>
          <div>
            <el-button type="primary" @click="draw_roc">生成roc曲线</el-button>
          </div>
        </div>
      </div>
      <div v-show="1 === number">
        <!-- 散点图 -->
        <div class="sandianWrap">
          <div
            id="echart1"
            style="float: left; width: 1000px; height: 400px"
          ></div>
        </div>
      </div>
      <div
        v-show="2 === number"
        style="display: flex; justify-content: center; align-items: center"
      >
        <!-- 饼图 -->
        <div class="echart" id="mychart" :style="myChartStyle"></div>
      </div>
      <div
        v-show="3 === number"
        style="display: flex; justify-content: center; align-items: center"
      >
        <!-- roc图 -->

        <el-image
          style="width: 600px; height: 500px"
          :src="roc_img"
          :fit="fit"
        ></el-image>
      </div>
    </div>
  </div>
</template>
<script>
import * as echarts from "echarts";
export default {
  data() {
    return {
      roc_img: null,
      multipleSelection: null,
      xname: null,
      myChart1: null, // 定义变量用来存放echarts实例(散点图)
      sandianData: null,
      number: 0,
      query: {
        key: this.$route.query.key,
        vimps_dict: this.$route.query.vimps_dict,
      },
      myChart: {},
      pieData: [],
      pieName: [],
      myChartStyle: { float: "left", width: "1250px", height: "400px" }, //图表样式
      vimps_json: null,
    };
  },
  mounted() {
    
    
    this.sanDianDataConvert(this.vimps_json);
    this.drawEcharts(); //画散点图
    this.initDate(); //数据初始化
    this.initEcharts();
    var picInfo = this.myChart.getDataURL();
    let noPrefix = picInfo.replace(/^data:image\/\w+;base64,/, "");


  },
  created() {
    // var d=this.query.vimps_dict
    // this.pieData = JSON.parse(this.query.vimps_dict);
    this.pieData=JSON.parse(localStorage.getItem("vimps_json"));

    this.vimps_json = JSON.parse(localStorage.getItem("vimps_json"));

  },
  methods: {
    draw_roc() {
      this.$axios({
        method: "post",
        url: "http://127.0.0.1:8000/api/draw_roc/",
        data: this.multipleSelection,
      }).then((res) => {
        if (res.data.code == 0) {
          this.$message.success("roc曲线已生成");
          this.roc_img = res.data.src;
        }
      });
    },
    //复选框状态改变
    changeFun(val) {
      this.multipleSelection = val;
      console.log(this.multipleSelection);
    },
    sanDianDataConvert(a) {
      var arr = [];
      for (const key in a) {
        // console.log(a[key].name,a[key].value);
        arr.push(a[key].name);
      }
      this.xname = arr;
    },
    // 画图方法(散点图)
    drawEcharts() {
      this.myChart1 = echarts.init(document.getElementById("echart1"));
      this.myChart1.setOption({
        xAxis: {
          data: this.xname,
          type: "category",
          name: "变量", // x轴的名字，可以理解成单位
          nameTextStyle: {
            // x轴的名字的样式相关
            color: "#BFBFBF",
            nameLocation: "start",
          },
          splitLine: {
            //去除网格线
            // show: false,
          },
          splitArea: { show: false }, //去除网格区域，否则会有一片区域
          axisLabel: {
            interval: 0,
            rotate: 90,
            // 设置x轴的文字的样式
            textStyle: {
              show: true,
              color: "#BDBDBD",
              fontSize: "12",
            },
          },
          axisLine: {
            show: true, // 把x轴从实线变成虚线
            lineStyle: {
              // 设置x轴线条样式的颜色
              color: "#BDBDBD",
              width: 1,
              type: "solid",
            },
          },
          scale: true, // 设置数据自动缩放，要不然数据多的话就堆一块了
        },
        yAxis: {
          type: "value",
          name: "特征重要性",
          nameTextStyle: {
            color: "#BFBFBF",
            nameLocation: "end",
          },
          axisTick: {
            show: false, // 去掉y轴的凸出刻度
          },
          axisLine: {
            // show: false, // 把y轴从实线变成虚线
          },
          splitLine: {
            //去除网格线
            show: true,
            lineStyle: {
              type: "dashed", //设置网格线类型 dotted：虚线   solid:实线
            },
          },
          splitArea: { show: false }, //去除网格区域
          axisLabel: {
            // 设置y轴的文字的样式
            textStyle: {
              show: true,
              color: "#BDBDBD",
              fontSize: "12",
            },
          },
          scale: true, // 设置数据自动缩放，要不然数据就堆一块了
          // show: false,
        },
        grid: {
          left: "10%",
          bottom: "35%",
          // 位置
          show: true,
          x: 36,
          y: 40,
          x2: 72,
          y2: 36,
          borderWidth: 0, // 去除图表的边框
        },
        series: [
          {
            // name: "一班",
            symbolSize: 10, // 散点图的大小
            // data: this.sandianData,
            data: this.vimps_json,

            type: "scatter", // 类型为散点图
            itemStyle: {
              // 设置散点图的透明度
              opacity: 0.85,
            },
          },
        ],
        title: {
          // title为标题部分，有一级标题text，二级标题subtext。这里我们使用二级标题，再修改一下这个二级标题的位置即可出现我们想要的效果了，当然样式也可以通过title.subtextStyle去配置
          // subtext: "特征重要性散点图",
          left: 100, // 距离左边位置
          top: 0, // 距离上面位置
          subtextStyle: {
            // 设置二级标题的样式
            color: "#BFBFBF",
          },
        },
        color: ["#4CD3D4", "#60BD65", "#46A7EA", "#E99E44", "#DC403F"], // 控制圆环图的颜色
      });
      // 自适应
      window.addEventListener("resize", () => {
        this.myChart1.resize();
      });
    },
    change: function (index) {
      this.number = index; //重要处
    },
    initDate() {
      for (let i = 0; i < this.pieData.length; i++) {
        // this.xData[i] = i;
        // this.yData =this.xData[i]*this.xData[i];
        this.pieName[i] = this.pieData[i].name;
      }
    },
    initEcharts() {
      // 饼图
      const option = {
        animation: false,
        legend: {
          // 图例
          data: this.pieName,
          right: "0%",
          top: "0%",
          orient: "vertical",
        },
        title: {
          // 设置饼图标题，位置设为顶部居中
          text: "特征重要性饼图",
          top: "0%",
          left: "center",
        },
        series: [
          {
            type: "pie",
            label: {
              show: true,
              formatter: "{b} : {c} ({d}%)", // b代表名称，c代表对应值，d代表百分比
            },
            radius: "40%", //饼图半径
            data: this.pieData,
            // data:this.vimps_dict
          },
        ],
      };
      // console.log(this.seriesData);
      const optionFree = {
        xAxis: {},
        yAxis: {},
        series: [
          {
            data: this.seriesData,
            type: "line",
            smooth: true,
          },
        ],
      };
      this.myChart = echarts.init(document.getElementById("mychart"));
      this.myChart.setOption(option);

      // 随着屏幕大小调节图表
      window.addEventListener("resize", () => {
        this.myChart.resize();
      });
    },
  },
};
</script>
<style lang='less' scoped>
.btn_anniu {
  width: 25%;
  padding: 25px 0;
  font-size: 29px;
  font-weight: bold;
  border: 0 solid #fff;
  color: #000;
  outline: none;
  background: #fff;
}
.newStyle {
  border-bottom: 2px solid #f0892e;
  color: #f0892e;
  font-size: 29px;
  font-weight: bold;
}
.sandianWrap {
  width: 100%;
  height: 100%;
  #echart1 {
    width: 100%;
    height: 400px;
  }
}
</style>