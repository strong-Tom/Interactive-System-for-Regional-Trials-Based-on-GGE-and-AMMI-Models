<template>
  <div
    style="
      display: flex;
      justify-content: space-between;
      margin-top: 10px;
      height: 100%;
    "
  >
    <!-- 黑龙江地图 -->
    <div
      style="backgroundcolor: pink; height: 150%; width: 150%"
      ref="charts"
      class="map"
    ></div>
    <!-- 右侧工具栏 -->
    <div class="tool_box">
      <!-- 划分区说明 -->
      <div class="litter">
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span><h5>黑龙江省杨树栽培生态区划分</h5></span>
          </div>
          <div class="text item">
            <a :href="'#/region11'" style="color: red">(Ⅰ) 北部丘陵寒冷区</a>
          </div>
          <div class="text item">
            <a :href="'#/region12'" style="color: red">(Ⅱ) 东部低湿平原区</a>
          </div>
          <div class="text item">
            <a :href="'#/region3_image'" style="color: red"
              >(Ⅲ) 西部半干旱平原区</a
            >
          </div>
          <div class="text item">(Ⅳ) 南部缓丘半干旱、半湿润区</div>
          <div class="text item">
            <a :href="'#/region15'" style="color: red"
              >(Ⅴ) 东南部山地湿润、半湿润区</a
            >
          </div>
        </el-card>
      </div>
      <div class="textt" style="margin-top: 10px"><h6>不同立地</h6></div>
      <!-- 地点按钮组 -->
      <div class="button_club">
        <div class="heat">
          <!-- 第一行 -->
          <el-row :gutter="20">
            <el-col :span="12"
              ><el-button
                type="primary"
                size="mini"
                @click="heat_dq"
                class="xhy"
                >大庆</el-button
              ></el-col
            >
            <el-col :span="12"
              ><el-button
                type="primary"
                size="mini"
                @click="heat_qq"
                class="yzy"
                >齐齐哈尔</el-button
              ></el-col
            >
          </el-row>
          <el-row :gutter="20">
            <el-col :span="12"
              ><el-button
                type="primary"
                size="mini"
                @click="heat_other"
                class="xhy"
                >其他立地</el-button
              ></el-col
            >
          </el-row>
        </div>
      </div>
      <!-- <div class="textt"><h6>径向增长量</h6></div> -->
      <!-- 按钮组 -->
      <!-- <div class="button_club">
        <div class="bt">
          <el-button type="primary" size="mini" @click="growth_dq" class="xhy"
            >大庆</el-button
          >
          <el-button type="primary" size="mini" @click="growth_qq" class="yzy"
            >齐齐哈尔</el-button
          >
        </div>
      </div> -->
      <!-- <div class="textt"><h6>胸径(箱型图)</h6></div> -->
      <!-- 按钮组 -->
      <!-- <div class="button_club">
        <div class="bt">
          <el-button type="primary" size="mini" @click="diameter_dq" class="xhy"
            >大庆</el-button
          >
          <el-button type="primary" size="mini" @click="diameter_qq" class="yzy"
            >齐齐哈尔</el-button
          >
        </div>
      </div> -->
      <div class="textt" style="margin-top: 10px"><h6>不同品种</h6></div>
      <!-- 树种按钮组 -->
      <div class="button_club">
        <div class="heat">
          <!-- 第一行 -->
          <!-- <el-row :gutter="20">
            <el-col :span="12"
              ><el-button
                type="primary"
                size="mini"
                @click="heat_dq"
                class="xhy"
                >大庆</el-button
              ></el-col
            >
            <el-col :span="12"
              ><el-button
                type="primary"
                size="mini"
                @click="heat_qq"
                class="yzy"
                >齐齐哈尔</el-button
              ></el-col
            >
          </el-row> -->
          <!-- 第2行 -->
          <el-row :gutter="20">
            <el-col :span="12">
              <el-button
                type="primary"
                size="mini"
                @click="heat_xhy"
                class="yzy"
                >小黑杨</el-button
              ></el-col
            >
            <el-col :span="12">
              <el-button
                type="primary"
                size="mini"
                @click="heat_hqy"
                class="yzy"
                >黑青杨</el-button
              ></el-col
            >
          </el-row>

          <!-- 第3行 -->
          <el-row :gutter="20">
            <el-col :span="12">
              <el-button
                type="primary"
                size="mini"
                @click="heat_yzy"
                class="yzy"
                >银中杨</el-button
              ></el-col
            >
            <el-col :span="12">
              <el-button
                type="primary"
                size="mini"
                @click="heat_qsy"
                class="yzy"
                >青山杨</el-button
              ></el-col
            >
          </el-row>
          <el-row :gutter="20">
            <el-col :span="12">
              <el-button
                type="primary"
                size="mini"
                @click="heat_yzy"
                class="yzy"
                >其他品种</el-button
              ></el-col
            >
          </el-row>
        </div>
      </div>
    </div>
  </div>
</template>
   
  <script>
import axios from "axios";
import Cookies from "js-cookie";
import * as echarts from "echarts";
import { posix } from "path";
//   import shengfen from "echarts/map/json/china.json";
// import shengfen from "echarts/map/json/province/heilongjiang.json";
// import shengfen from "./d6.json";
import shengfen from "../views/t.json";
// import shengfen from "./hlj2.json";
export default {
  data() {
    return {
      //   airData: [{ name: "黑河市", value: 1 }],
      airData: [
        {
          name: "(Ⅰ)",
          value: 1,
          tooltip: {
            show: true,
            trigger: "item",
            extraCssText: "max-width:200px; white-space:pre-wrap",
            formatter: function (params) {
              return `<div>该区域适合种植小黑杨、小黑14、银中杨、小青黑、大青杨等，点击能查看详细信息</div>`;
            },
          },
        },
        {
          name: "(Ⅱ)",
          value: 2,
          tooltip: {
            show: true,
            trigger: "item",
            extraCssText: "max-width:200px; white-space:pre-wrap",
            formatter: function (params) {
              return `<div>该区域适合种植小黑杨、小黑14、银中杨、青山杨、大青杨、小青黑、北京3、北京605、A100等，点击能查看详细信息</div>`;
            },
          },
        },
        {
          name: "(Ⅲ)",
          value: 3,
          tooltip: {
            show: true,
            trigger: "item",
            extraCssText: "max-width:200px; white-space:pre-wrap",
            formatter: function (params) {
              return `<div>该区域适合种植<span style='color:red;'>黑青杨、中雄4号、龙丰1号、银中杨、青山杨</span>、银中杨、小青黑、小黑杨、小黑14、白城3、A43、A15、中黑防、中绥12等，点击能查看详细信息</div>`;
            },
          },
        },
        {
          name: "(Ⅳ)",
          value: 4,
          tooltip: {
            show: true,
            trigger: "item",
            extraCssText: "max-width:200px; white-space:pre-wrap",
            formatter: function (params) {
              return `<div>该区域适合种植迎春5号、小黑杨、小黑14、小青黑、青山杨、银中杨，点击能查看详细信息</div>`;
            },
          },
        },
        {
          name: "(Ⅴ)",
          value: 5,
          tooltip: {
            show: true,
            trigger: "item",
            extraCssText: "max-width:200px; white-space:pre-wrap",
            formatter: function (params) {
              return `<div>该区域适合种植小黑杨、小黑14、迎春5号、大青杨、银中杨等，点击能查看详细信息</div>`;
            },
          },
        },
      ],
    };
  },

  //
  created() {
    this.$nextTick(() => {
      this.initCharts();
    });
  },

  methods: {
    heat_other() {
      top.location.href = "/#/heat_other";
    },
    heat_dq() {
      top.location.href = "/#/heat_dq";
    },
    heat_qq() {
      top.location.href = "/#/heat_qq";
    },
    heat_xhy() {
      top.location.href = "/#/heat_xhy";
    },
    heat_hqy() {
      top.location.href = "/#/heat_hqy";
    },
    heat_yzy() {
      top.location.href = "/#/heat_yzy";
    },
    heat_qsy() {
      top.location.href = "/#/heat_qsy";
    },
    growth_dq() {
      top.location.href = "/#/growth_dq";
    },
    growth_qq() {
      top.location.href = "/#/growth_qq";
    },
    diameter_dq() {
      top.location.href = "/#/diameter_dq";
    },
    diameter_qq() {
      top.location.href = "/#/diameter_qq";
    },
    xhy() {
      top.location.href = "/#/region1";
    },
    yzy() {
      top.location.href = "/#/region2";
    },
    initCharts() {
      const charts = echarts.init(this.$refs["charts"]);
      const option = {
        backgroundColor: "white", //地图组件的背景色
        // 提示浮窗样式
        tooltip: {
          extraCssText: "width:20%;height:10%;",

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
        },
        // visualMap: { //分段型视觉映射组件
        //     show: true,
        //     type: 'piecewise',
        //     left: 50,
        //     bottom: 50,
        //     showLabel: true,
        //     itemWidth: 10,
        //     itemHeight: 10,
        //     inverse: true,
        //     // lt:小于; lte:小于等于; gt:大于; gte:大于等于;
        //     pieces: [
        //         {
        //             lt: 5,
        //             label: "<5ms",
        //             color: "#83CBAC"
        //         },
        //         {
        //             gte: 5,
        //             lte: 10,
        //             label: "5-10ms",
        //             color: "#55BB8A"
        //         },
        //         {
        //             gt: 10,
        //             lte: 15,
        //             label: "10-15ms",
        //             color: "#30A162"
        //         },
        //         {
        //             gt: 15,
        //             lte: 30,
        //             label: "15-30ms",
        //             color: "#9ABEFA"
        //         },
        //         {
        //             gt: 30,
        //             lte: 30,
        //             label: '30-30ms',
        //             color: "#78A9F9"
        //         },
        //         {
        //             gt: 30,
        //             label: '>30ms',
        //             color: "#5693F7"
        //         }
        //     ]
        // },
        // 地图配置
        geo: {
          regions: [
            {
              //   地图区域的样式设置
              name: "(Ⅰ)",
              // itemStyle: {
              //   areaColor: "red",
              //   color: "red",
              // },
              label: {
                color: "red",
                fontSize: 30,
              },
            },
            {
              //   地图区域的样式设置
              name: "(Ⅱ)",
              // itemStyle: {
              //   areaColor: "red",
              //   color: "red",
              // },
              label: {
                color: "red",
                fontSize: 30,
              },
            },
            {
              //   地图区域的样式设置
              name: "(Ⅲ)",
              // itemStyle: {
              //   areaColor: "red",
              //   color: "red",
              // },
              label: {
                color: "red",
                fontSize: 30,
              },
            },
            {
              //   地图区域的样式设置
              name: "(Ⅳ)",
              // itemStyle: {
              //   areaColor: "red",
              //   color: "red",
              // },
              label: {
                color: "red",
                fontSize: 30,
              },
            },
            {
              //   地图区域的样式设置
              name: "(Ⅴ)",
              // itemStyle: {
              //   areaColor: "red",
              //   color: "red",
              // },
              label: {
                color: "red",
                fontSize: 30,
              },
            },
            {
              //   地图区域的样式设置
              name: "哈尔滨市",
              label: {
                color: "#DAA10F",
                fontSize: 15,
              },
            },
            {
              //   地图区域的样式设置
              name: "黑河市",
              label: {
                color: "#DAA10F",
                fontSize: 15,
              },
            },
            {
              //   地图区域的样式设置
              name: "齐齐哈尔市",
              label: {
                color: "#DAA10F",
                fontSize: 15,
              },
            },
            {
              //   地图区域的样式设置
              name: "双鸭山市",
              label: {
                color: "#DAA10F",
                fontSize: 15,
              },
            },
            {
              //   地图区域的样式设置
              name: "佳木斯市",
              label: {
                color: "#DAA10F",
                fontSize: 15,
              },
            },
            {
              //   地图区域的样式设置
              name: "鹤岗市",
              label: {
                color: "#DAA10F",
                fontSize: 15,
              },
            },
            {
              //   地图区域的样式设置
              name: "伊春市",
              label: {
                color: "#DAA10F",
                fontSize: 15,
              },
            },
            {
              //   地图区域的样式设置
              name: "绥化市",
              label: {
                color: "#DAA10F",
                fontSize: 15,
              },
            },
            {
              //   地图区域的样式设置
              name: "鸡西市",
              label: {
                color: "#DAA10F",
                fontSize: 15,
              },
            },
            {
              //   地图区域的样式设置
              name: "七台河市",
              label: {
                color: "#DAA10F",
                fontSize: 15,
              },
            },
            {
              //   地图区域的样式设置
              name: "牡丹江市",
              label: {
                color: "#DAA10F",
                fontSize: 15,
              },
            },
            {
              //   地图区域的样式设置
              name: "大庆市",
              label: {
                color: "#DAA10F",
                fontSize: 15,
              },
            },
          ],
          map: "china",
          aspectScale: 1.2, //长宽比,0.75的含义为宽是高的0.75,假如高为100,宽就只有75;0.5的含义就是宽只有高的一半,假如高为100,宽就只有50
          zoom: 2.3, //视觉比例大小,1.2即为原有大小的1.2倍
          roam: false, //是否开启鼠标缩放和平移漫游。默认不开启。可以不用设置,如果只想要开启缩放或者平移，可以设置成 'scale' 或者 'move'。
          top: "55%", //地图距离顶部的距离
          //   top: "auto", //地图距离顶部的距离
          left: "27%",
          label: {
            // 通常状态下的样式
            normal: {
              show: true,

              textStyle: {
                color: "black", //地图上文字的颜色
                fontSize: "10px",
              },
            },

            // 鼠标放上去的样式
            emphasis: {
              textStyle: {
                color: "rgba(242, 153, 74, 1)",
              },
            },
          },

          // 地图区域的样式设置
          itemStyle: {
            normal: {
              areaColor: "white", //地图填充色
              borderColor: "rgba(36, 215, 309, 1)", //地图分割线颜色
              borderWidth: 1,
            },
            // 鼠标放上去高亮的样式
            emphasis: {
              areaColor: "pink", //地图填充色
              borderColor: "#08EFEF", //地图分割线颜色
              borderWidth: 1,
            },
          },
        },
        series: [
          {
            selectedMode: false, //取消地图区域点击事件
            geoIndex: 0, //将数据和第0个geo配置关联在一起
            type: "map",
            data: this.airData,
          },
        ],
      };
      // 地图注册，第一个参数的名字必须和option.geo.map一致
      echarts.registerMap("china", shengfen); //第一个参数为配置设置的名称，第二个参数为引入的地图名称
      charts.setOption(option);
      charts.on("click", function (params) {
        // switch (params.value) {
        //   case 3:
        //     top.location.href = "/#/region1";
        //     break;
        // }
        // top.location.href = "/#/region";
        if (params.value == 3) {
          top.location.href = "/#/phenomena";
        } else {
          // top.location.href = "/#/region";
        }
      });
      // charts.on("mouseover", function () { //取消鼠标移入地图区域高亮
      //     charts.dispatchAction({
      //         type: 'legendUnSelect'
      //     });
      // });
    },
  },
};
</script>
   
<style lang="less" scoped>
@import "../src/assets/less/map.less";
</style>