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
        齐齐哈尔地区相关性分析热力图
      </button>
      <button
        class="btn_anniu"
        @click="change(3)"
        :class="{ newStyle: 3 === number }"
      >
        齐齐哈尔地区速生用材树种生长量汇总表
      </button>
      <button
        class="btn_anniu"
        @click="change(4)"
        :class="{ newStyle: 4 === number }"
      >
        齐齐哈尔栽培区杨树品种木材物理力学属性
      </button>
      <button
        class="btn_anniu"
        @click="change(5)"
        :class="{ newStyle: 5 === number }"
      >
        青杨类杨树材性方差分析表
      </button>
      <button
        class="btn_anniu"
        @click="change(6)"
        :class="{ newStyle: 6 === number }"
      >
      青杨类各品种材性性状秩次表
      </button>
      <button
        class="btn_anniu"
        @click="change(7)"
        :class="{ newStyle: 7 === number }"
      >
      青杨类各地点材性性状秩次表
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

      <!-- 齐齐哈尔地区速生用材树种生长量汇总表 -->
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
      <!-- 表1： 齐齐哈尔栽培区杨树品种木材物理力学属性 -->
      <div v-show="4 === number">
        <el-table
          :data="tableData1"
          height="480px"
          border
          style="width: 100%"
          :header-cell-style="{ textAlign: 'center', color: '#000' }"
          :cell-style="{ textAlign: 'center' }"
        >
          <el-table-column prop="data1" label="树种"> </el-table-column>
          <el-table-column prop="data2" label="不同样地"> </el-table-column>
          <el-table-column prop="data3" label="含水率"> </el-table-column>
          <el-table-column prop="data4" label="绝干密度(g/cm³)" width="150px">
          </el-table-column>

          <el-table-column prop="data5" label="抗弯强度(MPa)" width="150px">
          </el-table-column>
          <el-table-column prop="data6" label="抗弯弹性(MPa)" width="150px">
          </el-table-column>
          <el-table-column label="硬度/N">
            <el-table-column prop="data7" label="端面"> </el-table-column>

            <el-table-column prop="data8" label="弦向" width="120px">
            </el-table-column>
            <el-table-column prop="data9" label="径向" width="120px">
            </el-table-column>
          </el-table-column>
          <el-table-column label="顺纹抗剪强度(MPa)">
            <el-table-column prop="data10" label="弦向"> </el-table-column>
            <el-table-column prop="data11" label="径向"> </el-table-column>
          </el-table-column>
          <el-table-column prop="data12" label="顺纹抗压强度(MPa)" width="150">
          </el-table-column
          ><el-table-column label="横纹抗剪强度(MPa)">
            <el-table-column prop="data13" label="弦向"> </el-table-column>
            <el-table-column prop="data14" label="径向"> </el-table-column>
          </el-table-column>
          <el-table-column prop="data15" label="冲击韧性(kj/m²)" width="200px">
          </el-table-column>
        </el-table>
          <el-button type="danger" size="medium" @click="to_img">表1 </el-button
          >齐齐哈尔栽培区杨树品种木材物理力学属性
        </h5>
      </div>
      <!-- 表2：青杨类杨树材性方差分析表 -->
      <div v-show="5 === number">
        <el-table
          :data="tableData2"
          height="480px"
          border
          style="width: 100%"
          :header-cell-style="{ textAlign: 'center', color: '#000' }"
          :cell-style="{ textAlign: 'center' }"
        >
          <el-table-column prop="data1" label="性状"> </el-table-column>
          <el-table-column prop="data2" label="因素"> </el-table-column>
          <el-table-column prop="data3" label="df"> </el-table-column>
          <el-table-column prop="data4" label="均方" >
          </el-table-column>

          <el-table-column prop="data5" label="F" >
          </el-table-column>
          <el-table-column prop="data6" label="Sig0.05" >
          </el-table-column>
        </el-table>
        <h5>
          <el-tooltip
            class="item"
            effect="dark"
            content="品种间材性存在明显差异。其中，绝干密度、硬度（端面、弦向、径向）、抗弯强度、抗弯弹性模量、顺纹抗压强度、横纹抗压强度（弦向、径向）、顺纹抗剪强度、冲击韧性、握钉力（端面、弦向、径向）等差异显著，含水率和冲击力两项指标各品种间差异不显著"
            placement="top-start"
            ><el-button type="danger" size="medium">表2 </el-button></el-tooltip
          >青杨类杨树材性方差分析表
        </h5>
      </div>
     <!-- 表3：青杨类各品种材性性状秩次表 -->
      <div v-show="6 === number">
        <el-table
          :data="tableData3"
          height="400px"
          border
          style="width: 100%"
          :header-cell-style="{ textAlign: 'center', color: '#000' }"
          :cell-style="{ textAlign: 'center' }"
        >
          <el-table-column prop="data1" label="树种"> </el-table-column>
          <el-table-column prop="data2" label="含水率"> </el-table-column>
          <el-table-column prop="data3" label="绝干密度(g/cm³)" width="150px">
          </el-table-column>

          <el-table-column prop="data4" label="抗弯强度(MPa)" width="150px">
          </el-table-column>
          <el-table-column prop="data5" label="抗弯弹性(MPa)" width="150px">
          </el-table-column>
          <el-table-column label="硬度/N">
            <el-table-column prop="data6" label="端面"> </el-table-column>

            <el-table-column prop="data7" label="弦向" width="120px">
            </el-table-column>
            <el-table-column prop="data8" label="径向" width="120px">
            </el-table-column>
          </el-table-column>
          <el-table-column label="顺纹抗剪强度(MPa)">
            <el-table-column prop="data9" label="弦向"> </el-table-column>
            <el-table-column prop="data10" label="径向"> </el-table-column>
          </el-table-column>
          <el-table-column prop="data11" label="顺纹抗压强度(MPa)" width="150">
          </el-table-column
          ><el-table-column label="横纹抗剪强度(MPa)">
            <el-table-column prop="data12" label="弦向"> </el-table-column>
            <el-table-column prop="data13" label="径向"> </el-table-column>
          </el-table-column>
          <el-table-column label="握钉力(N/mm)">
            <el-table-column prop="data14" label="端面"> </el-table-column>

            <el-table-column prop="data15" label="弦向" width="120px">
            </el-table-column>
            <el-table-column prop="data16" label="径向" width="120px">
            </el-table-column>
          </el-table-column>
          <el-table-column prop="data17" label="冲击韧性(kj/m²)" width="180px">
          </el-table-column>
          <el-table-column prop="data18" label="合计">
          </el-table-column>
        </el-table>
        <h5>
          <el-tooltip
            class="item"
            effect="dark"
            content="青杨类各品种大径材材性综合表现优良次序是中雄4号杨＞小黑杨＞龙丰2号杨＞青山杨＞黑青杨"
            placement="top-start"
            ><el-button type="danger" size="medium">表3 </el-button></el-tooltip
          >青杨类各品种材性性状秩次表
        </h5>
      </div>
      <!-- 表4：青杨类各地点材性性状秩次表 -->
      <div v-show="7 === number">
        <el-table
          :data="tableData4"
          height="220px"
          border
          style="width: 100%"
          :header-cell-style="{ textAlign: 'center', color: '#000' }"
          :cell-style="{ textAlign: 'center' }"
        >
          <el-table-column prop="data1" label="树种"> </el-table-column>
          <el-table-column prop="data2" label="含水率"> </el-table-column>
          <el-table-column prop="data3" label="绝干密度(g/cm³)" width="150px">
          </el-table-column>

          <el-table-column prop="data4" label="抗弯强度(MPa)" width="150px">
          </el-table-column>
          <el-table-column prop="data5" label="抗弯弹性(MPa)" width="150px">
          </el-table-column>
          <el-table-column label="硬度/N">
            <el-table-column prop="data6" label="端面"> </el-table-column>

            <el-table-column prop="data7" label="弦向" width="120px">
            </el-table-column>
            <el-table-column prop="data8" label="径向" width="120px">
            </el-table-column>
          </el-table-column>
          <el-table-column label="顺纹抗剪强度(MPa)">
            <el-table-column prop="data9" label="弦向"> </el-table-column>
            <el-table-column prop="data10" label="径向"> </el-table-column>
          </el-table-column>
          <el-table-column prop="data11" label="顺纹抗压强度(MPa)" width="150">
          </el-table-column
          ><el-table-column label="横纹抗剪强度(MPa)">
            <el-table-column prop="data12" label="弦向"> </el-table-column>
            <el-table-column prop="data13" label="径向"> </el-table-column>
          </el-table-column>
          <el-table-column label="握钉力(N/mm)">
            <el-table-column prop="data14" label="端面"> </el-table-column>

            <el-table-column prop="data15" label="弦向" width="120px">
            </el-table-column>
            <el-table-column prop="data16" label="径向" width="120px">
            </el-table-column>
          </el-table-column>
          <el-table-column prop="data17" label="冲击韧性(kj/m²)" width="180px">
          </el-table-column>
          <el-table-column prop="data18" label="合计">
          </el-table-column>
        </el-table>
        <h5>
          <el-tooltip
            class="item"
            effect="dark"
            content="错海林场青杨类大径材材性综合秩次值为21，富裕林场青杨类大径材材性综合秩次值27，错海林场青杨类大径材材性综合表现好于富裕林场的"
            placement="top-start"
            ><el-button type="danger" size="medium">表4 </el-button></el-tooltip
          >青杨类各地点材性性状秩次表
        </h5>
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
      tableData4: [
        {
          data1: "错海林场",
          data2: 1,
          data3: 1,
          data4: 1,
          data5: 1,
          data6: 2,
          data7: 1,
          data8: 1,
          data9: 2,
          data10: 2,
          data11: 1,
          data12: 1,
          data13: 1,
          data14: 2,
          data15: 2,
          data16: 1,
          data17: 1,
          data18: 21,
        },
        {
          data1: "富裕林场",
          data2: 2,
          data3: 2,
          data4: 2,
          data5: 2,
          data6: 1,
          data7: 2,
          data8: 2,
          data9: 1,
          data10: 1,
          data11: 2,
          data12: 2,
          data13: 2,
          data14: 1,
          data15: 1,
          data16: 2,
          data17: 2,
          data18: 27,
        },
      ],
      tableData3: [
        {
          data1: "黑青杨",
          data2: 3,
          data3: 5,
          data4: 5,
          data5: 5,
          data6: 5,
          data7: 5,
          data8: 5,
          data9: 5,
          data10: 5,
          data11: 5,
          data12: 5,
          data13: 5,
          data14: 5,
          data15: 5,
          data16: 5,
          data17: 3,
          data18: 76,
        },
        {
          data1: "龙丰2号杨",
          data2: 2,
          data3: 1,
          data4: 1,
          data5: 1,
          data6: 4,
          data7: 2,
          data8: 4,
          data9: 3,
          data10: 4,
          data11: 1,
          data12: 2,
          data13: 1,
          data14: 2,
          data15: 2,
          data16: 2,
          data17: 5,
          data18: 37,
        },
        {
          data1: "青山杨",
          data2: 4,
          data3: 4,
          data4: 3,
          data5: 4,
          data6: 3,
          data7: 4,
          data8: 3,
          data9: 2,
          data10: 2,
          data11: 3,
          data12: 4,
          data13: 2,
          data14: 4,
          data15: 4,
          data16: 4,
          data17: 2,
          data18: 52,
        },
        {
          data1: "小黑杨",
          data2: 5,
          data3: 3,
          data4: 4,
          data5: 3,
          data6: 1,
          data7: 3,
          data8: 2,
          data9: 1,
          data10: 3,
          data11: 2,
          data12: 3,
          data13: 4,
          data14: 3,
          data15: 3,
          data16: 3,
          data17: 4,
          data18: 34,
        },
        {
          data1: "中雄4号杨",
          data2: 1,
          data3: 2,
          data4: 2,
          data5: 2,
          data6: 2,
          data7: 1,
          data8: 1,
          data9: 4,
          data10: 1,
          data11: 4,
          data12: 1,
          data13: 3,
          data14: 1,
          data15: 1,
          data16: 1,
          data17: 1,
          data18: 28,
        },
      ],
      tableData2: [
        {
          data1: "含水率",
          data2: "品种",
          data3: 4,
          data4: 3.319,
          data5: 3.92,
          data6: 0.006,
        },
        {
          data1: "",
          data2: "地点",
          data3: 1,
          data4: 1.082,
          data5: 1.278,
          data6: 0.261,
        },
        {
          data1: "绝干密度",
          data2: "品种",
          data3: 4,
          data4: 0.01,
          data5: 20.809,
          data6: 0,
        },
        {
          data1: "",
          data2: "地点",
          data3: 1,
          data4: 0.015,
          data5: 29.982,
          data6: 0,
        },
        {
          data1: "硬度（端面）",
          data2: "品种",
          data3: 4,
          data4: 703032.5,
          data5: 28.306,
          data6: 0,
        },
        {
          data1: "",
          data2: "地点",
          data3: 1,
          data4: 38025,
          data5: 1.53,
          data6: 0.219,
        },
        {
          data1: "硬度（弦向）",
          data2: "品种",
          data3: 4,
          data4: 589930,
          data5: 12.74,
          data6: 0,
        },
        {
          data1: "",
          data2: "地点",
          data3: 1,
          data4: 65025,
          data5: 1.404,
          data6: 0.239,
        },
        {
          data1: "硬度（径向）",
          data2: "品种",
          data3: 4,
          data4: 276136.5,
          data5: 4.937,
          data6: 0,
        },
        {
          data1: "",
          data2: "地点",
          data3: 1,
          data4: 804609,
          data5: 14.385,
          data6: 0,
        },
        {
          data1: "顺纹抗压强度",
          data2: "品种",
          data3: 4,
          data4: 164.701,
          data5: 11.487,
          data6: 0,
        },
        {
          data1: "",
          data2: "地点",
          data3: 1,
          data4: 25,
          data5: 1.744,
          data6: 0.19,
        },
        {
          data1: "横纹抗压强度",
          data2: "品种",
          data3: 4,
          data4: 5.389,
          data5: 8.54,
          data6: 0,
        },
        {
          data1: "（弦向）",
          data2: "地点",
          data3: 1,
          data4: 8.18,
          data5: 12.962,
          data6: 0.001,
        },
        {
          data1: "横纹抗压强度",
          data2: "品种",
          data3: 4,
          data4: 9.236,
          data5: 10.491,
          data6: 0,
        },
        {
          data1: "（径向）",
          data2: "地点",
          data3: 1,
          data4: 4.58,
          data5: 5.202,
          data6: 0.025,
        },
        {
          data1: "抗弯强度",
          data2: "品种",
          data3: 4,
          data4: 890.117,
          data5: 13.047,
          data6: 0,
        },
        {
          data1: "",
          data2: "地点",
          data3: 1,
          data4: 613.364,
          data5: 8.991,
          data6: 0.003,
        },
        {
          data1: "抗弯弹性模量",
          data2: "品种",
          data3: 4,
          data4: 15509480.42,
          data5: 25.13,
          data6: 0,
        },
        {
          data1: "",
          data2: "地点",
          data3: 1,
          data4: 11668803.33,
          data5: 18.907,
          data6: 0,
        },
        {
          data1: "顺纹抗剪强度",
          data2: "品种",
          data3: 4,
          data4: 8.969,
          data5: 7.676,
          data6: 0,
        },
        {
          data1: "（弦向）",
          data2: "地点",
          data3: 1,
          data4: 5.852,
          data5: 5.0081,
          data6: 0.027,
        },
        {
          data1: "顺纹抗剪强度",
          data2: "品种",
          data3: 4,
          data4: 10.871,
          data5: 3.545,
          data6: 0,
        },
        {
          data1: "（径向）",
          data2: "地点",
          data3: 1,
          data4: 47.376,
          data5: 59.033,
          data6: 0,
        },
        {
          data1: "握钉力（端面）",
          data2: "品种",
          data3: 4,
          data4: 53.336,
          data5: 8096,
          data6: 0,
        },
        {
          data1: "",
          data2: "地点",
          data3: 1,
          data4: 5.376,
          data5: 0.816,
          data6: 0.368,
        },
        {
          data1: "握钉力（弦向）",
          data2: "品种",
          data3: 4,
          data4: 67.119,
          data5: 6.52,
          data6: 0,
        },
        {
          data1: "",
          data2: "地点",
          data3: 1,
          data4: 22.533,
          data5: 2.189,
          data6: 0.142,
        },
        {
          data1: "握钉力（径向）",
          data2: "品种",
          data3: 4,
          data4: 163.333,
          data5: 9.616,
          data6: 0,
        },
        {
          data1: "",
          data2: "地点",
          data3: 1,
          data4: 105.094,
          data5: 6.188,
          data6: 0.014,
        },
        {
          data1: "冲击力",
          data2: "品种",
          data3: 4,
          data4: 931.654,
          data5: 3.317,
          data6: 0.013,
        },
        {
          data1: "",
          data2: "地点",
          data3: 1,
          data4: 9.075,
          data5: 0.032,
          data6: 0.818,
        },
      ],
      tableData1: [
        {
          data1: "青山杨",
          data2: "LJ",
          data3: "14.80±",
          data4: "0.37±",
          data5: "72.60±",
          data6: "8340±",
          data7: "1984±",
          data8: "1465±",
          data9: "1795±",
          data10: "8.70±",
          data11: "10.10±",
          data12: "30.70±",
          data13: "5.30±",
          data14: "7.10±",
          data15: "50.60±",
        },
        {
          data1: "",
          data2: "FU",
          data3: 1.38,
          data4: 0.02,
          data5: 10.18,
          data6: 714,
          data7: 217,
          data8: 288,
          data9: 195,
          data10: 0.89,
          data11: 0.97,
          data12: 4.89,
          data13: 0.88,
          data14: 1.14,
          data15: 16.84,
        },
        {
          data1: "",
          data2: "LJ",
          data3: "14.60±",
          data4: "0.37±",
          data5: "58.60±",
          data6: "6744±",
          data7: "2222±",
          data8: "1721±",
          data9: "1762±",
          data10: "8.43±",
          data11: "10±1.02",
          data12: "32.17±",
          data13: "5.20±",
          data14: "6.50±",
          data15: "52.80±",
        },
        {
          data1: "",
          data2: "FU",
          data3: 0.88,
          data4: 0.03,
          data5: 6.05,
          data6: 584,
          data7: 177,
          data8: 116,
          data9: 110,
          data10: 0.55,
          data11: "",
          data12: 2.85,
          data13: 0.71,
          data14: 1,
          data15: 21.24,
        },
        {
          data1: "黑青杨",
          data2: "LJ",
          data3: "13.28±",
          data4: "0.38±",
          data5: "59.06±",
          data6: "7947±",
          data7: "2162±",
          data8: "1534±",
          data9: "1801±",
          data10: "6.77±",
          data11: "7.62±",
          data12: "31.33±",
          data13: "5.47±",
          data14: "5.69±",
          data15: "40.30±",
        },
        {
          data1: "",
          data2: "FU",
          data3: 0.66,
          data4: 0.01,
          data5: 5.96,
          data6: 785,
          data7: 137,
          data8: 141,
          data9: 214,
          data10: 0.89,
          data11: 0.64,
          data12: 2.62,
          data13: 0.49,
          data14: 0.3,
          data15: 11.75,
        },
        {
          data1: "",
          data2: "LJ",
          data3: "15.14±",
          data4: "0.32±",
          data5: "52.20±",
          data6: "6534±",
          data7: "1914±",
          data8: "1354±",
          data9: "1534±",
          data10: "7.68±",
          data11: "9.35±",
          data12: "28.35±",
          data13: "4.85±",
          data14: "4.92±",
          data15: "53.20±",
        },
        {
          data1: "",
          data2: "FU",
          data3: 0.65,
          data4: 0.02,
          data5: 4.67,
          data6: 643,
          data7: 146,
          data8: 145,
          data9: 170,
          data10: 0.51,
          data11: 0.49,
          data12: 2.11,
          data13: 0.72,
          data14: 0.78,
          data15: 21.21,
        },
        {
          data1: "龙丰2号",
          data2: "LJ",
          data3: "14.50±",
          data4: "0.44±",
          data5: "73.91±",
          data6: "9376±",
          data7: "2097±",
          data8: "1782±",
          data9: "1817±",
          data10: "8.55±",
          data11: "8.56±",
          data12: "36.87±",
          data13: "7.87±",
          data14: "7.67±",
          data15: "50±",
        },
        {
          data1: "",
          data2: "FU",
          data3: 0.77,
          data4: 0.03,
          data5: 4.76,
          data6: 474,
          data7: 205,
          data8: 208,
          data9: 210,
          data10: 1.76,
          data11: 0.95,
          data12: 7.08,
          data13: 1.44,
          data14: 1.64,
          data15: 12.75,
        },
        {
          data1: "",
          data2: "LJ",
          data3: "13.84±",
          data4: "0.38±",
          data5: "70.38±",
          data6: "9143±",
          data7: "2008±",
          data8: "1721±",
          data9: "1699±",
          data10: "8.40±",
          data11: "10.64±",
          data12: "36.79±",
          data13: "4.91±",
          data14: "6.20±",
          data15: "33.30±",
        },
        {
          data1: "",
          data2: "FU",
          data3: 0.64,
          data4: 0.01,
          data5: 5.44,
          data6: 889,
          data7: 140,
          data8: 313,
          data9: 210,
          data10: 0.29,
          data11: 0.54,
          data12: 1.35,
          data13: 0.81,
          data14: 0.95,
          data15: 18.77,
        },
        {
          data1: "中雄4号",
          data2: "LJ",
          data3: "14.10±",
          data4: "0.39±",
          data5: "68.33±",
          data6: "8670±",
          data7: "1894±",
          data8: "2028±",
          data9: "2060±",
          data10: "7.31±",
          data11: "9.60±",
          data12: "32.31±",
          data13: "5.49±",
          data14: "5.80±",
          data15: "56.17±",
        },
        {
          data1: "",
          data2: "FU",
          data3: 1.14,
          data4: 0.02,
          data5: 6.99,
          data6: 887,
          data7: 151,
          data8: 275,
          data9: 400,
          data10: 2.03,
          data11: 0.74,
          data12: 4.8,
          data13: 0.4,
          data14: 0.62,
          data15: 14.06,
        },
        {
          data1: "",
          data2: "LJ",
          data3: "13.75±",
          data4: "0.39±",
          data5: "64.36±",
          data6: "8396±",
          data7: "2361±",
          data8: "1768±",
          data9: "1830±",
          data10: "9.49±",
          data11: "10.63±",
          data12: "29.42±",
          data13: "6.36±",
          data14: "6.83±",
          data15: "60±",
        },
        {
          data1: "",
          data2: "FU",
          data3: 1.19,
          data4: 0.01,
          data5: 20.62,
          data6: 1148,
          data7: 143,
          data8: 159,
          data9: 232,
          data10: 0.78,
          data11: 0.65,
          data12: 1.51,
          data13: 0.84,
          data14: 0.95,
          data15: 14.7,
        },
        {
          data1: "小黑杨",
          data2: "LJ",
          data3: "14.74±",
          data4: "0.39±",
          data5: "59.05±",
          data6: "7830±",
          data7: "2578±",
          data8: "1731±",
          data9: "2049±",
          data10: "9.00±",
          data11: "9.13±",
          data12: "34.62±",
          data13: "5.45±",
          data14: "5.99±",
          data15: "49±",
        },
        {
          data1: "",
          data2: "FU",
          data3: 0.67,
          data4: 0.03,
          data5: 4.15,
          data6: 926,
          data7: 84,
          data8: 202,
          data9: 324,
          data10: 1.09,
          data11: 1.14,
          data12: 2.7,
          data13: 0.48,
          data14: 0.44,
          data15: 15.53,
        },
        {
          data1: "",
          data2: "LJ",
          data3: "15.12±",
          data4: "0.38±",
          data5: "64.75±",
          data6: "8227±",
          data7: "2405±",
          data8: "1721±",
          data9: "1800±",
          data10: "8.54±",
          data11: "10.70±",
          data12: "34.07±",
          data13: "5.39±",
          data14: "5.65±",
          data15: "44.08±",
        },
        {
          data1: "",
          data2: "FU",
          data3: 0.87,
          data4: 0.02,
          data5: 5.65,
          data6: 583,
          data7: 134,
          data8: 207,
          data9: 167,
          data10: 0.82,
          data11: 0.94,
          data12: 3.94,
          data13: 0.68,
          data14: 0.86,
          data15: 15.76,
        },
      ], //表1
      tableData: [
        {
          data1: "齐齐哈尔(D)",
          data2: "克山县(D1)",
          data3: "北联林场",
          data4: "3°",
          data5: "黑土",
          data6: "青山杨",
          data7: 4,
          data8: 625,
          data9: 4.2,
          data10: 3.6,
          data11: 0.0025,
          data12: 1.05,
          data13: 0.9,
          data14: 0.0006,
          data15: 0.39,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "",
          data4: "3°",
          data5: "黑土",
          data6: "小黑杨",
          data7: 4,
          data8: 1667,
          data9: 2.7,
          data10: 3,
          data11: 0.0009,
          data12: 0.68,
          data13: 0.75,
          data14: 0.0002,
          data15: 0.38,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "",
          data4: "3°",
          data5: "黑土",
          data6: "银中杨",
          data7: 4,
          data8: 1667,
          data9: 7.2,
          data10: 6.5,
          data11: 0.0128,
          data12: 1.8,
          data13: 1.63,
          data14: 0.0032,
          data15: 5.33,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "",
          data4: "3°",
          data5: "黑土",
          data6: "中黑防",
          data7: 4,
          data8: 1667,
          data9: 4.9,
          data10: 4.6,
          data11: 0.0043,
          data12: 1.23,
          data13: 1.15,
          data14: 0.0011,
          data15: 1.79,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "北联镇西新村",
          data4: "平",
          data5: "黑土",
          data6: "小黑杨",
          data7: 23,
          data8: 833,
          data9: 25.2,
          data10: 18.8,
          data11: 0.4223,
          data12: 1.1,
          data13: 0.82,
          data14: 0.0184,
          data15: 15.29,
          data16: "",
        },
        {
          data1: "",
          data2: "拜泉县(D2)",
          data3: "龙泉镇同乐村",
          data4: "平",
          data5: "黑土",
          data6: "小黑杨",
          data7: 21,
          data8: 833,
          data9: 25.2,
          data10: 20.5,
          data11: 0.4622,
          data12: 1.2,
          data13: 0.98,
          data14: 0.022,
          data15: 18.33,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "",
          data4: "平",
          data5: "黑土",
          data6: "银中杨",
          data7: 15,
          data8: 625,
          data9: 27.9,
          data10: 16.5,
          data11: 0.4478,
          data12: 1.86,
          data13: 1.1,
          data14: 0.0299,
          data15: 18.66,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "兴国乡",
          data4: "平",
          data5: "黑土",
          data6: "小黑杨",
          data7: 21,
          data8: 833,
          data9: 20.9,
          data10: 17.5,
          data11: 0.2742,
          data12: 1,
          data13: 0.83,
          data14: 0.0131,
          data15: 10.87,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "",
          data4: "平",
          data5: "黑土",
          data6: "小黑杨",
          data7: 21,
          data8: 833,
          data9: 21.9,
          data10: 17,
          data11: 0.2909,
          data12: 1.04,
          data13: 0.81,
          data14: 0.0139,
          data15: 11.53,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "拜泉镇破头山",
          data4: "10°",
          data5: "黑钙土",
          data6: "小黑杨",
          data7: 17,
          data8: 1111,
          data9: 16.9,
          data10: 17,
          data11: 0.1773,
          data12: 0.99,
          data13: 1,
          data14: 0.0104,
          data15: 11.59,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "",
          data4: "10°",
          data5: "黑钙土",
          data6: "银中杨",
          data7: 17,
          data8: 1111,
          data9: 19.7,
          data10: 23.2,
          data11: 0.3285,
          data12: 1.16,
          data13: 1.36,
          data14: 0.0193,
          data15: 21.47,
          data16: "",
        },
        {
          data1: "",
          data2: "讷河市(D2)",
          data3: "新江实验林场",
          data4: "平",
          data5: "栗钙土",
          data6: "银中杨",
          data7: 19,
          data8: 500,
          data9: 25.1,
          data10: 21.7,
          data11: 0.4867,
          data12: 1.32,
          data13: 1.14,
          data14: 0.0256,
          data15: 12.81,
          data16: "单株混交",
        },
        {
          data1: "",
          data2: "",
          data3: "狼洞山",
          data4: "平",
          data5: "栗钙土",
          data6: "小黑杨",
          data7: 19,
          data8: 667,
          data9: 15.8,
          data10: 16.7,
          data11: 0.1531,
          data12: 0.83,
          data13: 0.88,
          data14: 0.0081,
          data15: 5.37,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "",
          data4: "平",
          data5: "栗钙土",
          data6: "小黑杨",
          data7: 21,
          data8: 625,
          data9: 21.2,
          data10: 18.8,
          data11: 0.3036,
          data12: 1.01,
          data13: 0.9,
          data14: 0.0145,
          data15: 9.04,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "",
          data4: "平",
          data5: "栗钙土",
          data6: "银中杨",
          data7: 21,
          data8: 417,
          data9: 29,
          data10: 21.5,
          data11: 0.6351,
          data12: 1.38,
          data13: 1.02,
          data14: 0.0302,
          data15: 12.61,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "新江实验林场",
          data4: "平",
          data5: "栗钙土",
          data6: "银中杨",
          data7: 21,
          data8: 500,
          data9: 25,
          data10: 18.3,
          data11: 0.4044,
          data12: 1.19,
          data13: 0.87,
          data14: 0.0193,
          data15: 9.62,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "180亩",
          data4: "平",
          data5: "栗钙土",
          data6: "银中杨",
          data7: 21,
          data8: 625,
          data9: 25.8,
          data10: 21,
          data11: 0.4957,
          data12: 1.23,
          data13: 1,
          data14: 0.0236,
          data15: 14.75,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "",
          data4: "平",
          data5: "栗钙土",
          data6: "银中杨",
          data7: 21,
          data8: 833,
          data9: 21.5,
          data10: 16.7,
          data11: 0.2757,
          data12: 1.02,
          data13: 0.8,
          data14: 0.0131,
          data15: 10.94,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "",
          data4: "平",
          data5: "栗钙土",
          data6: "银中杨",
          data7: 21,
          data8: 1250,
          data9: 20.9,
          data10: 20.7,
          data11: 0.3266,
          data12: 1,
          data13: 0.99,
          data14: 0.0156,
          data15: 19.44,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "新江实验林场",
          data4: "平",
          data5: "栗钙土",
          data6: "A15",
          data7: 23,
          data8: 500,
          data9: 32.7,
          data10: 20.7,
          data11: 0.7678,
          data12: 1.42,
          data13: 0.9,
          data14: 0.0334,
          data15: 16.69,
          data16: "病害重",
        },
        {
          data1: "",
          data2: "",
          data3: "堤防站",
          data4: "平",
          data5: "栗钙土",
          data6: "B6",
          data7: 23,
          data8: 500,
          data9: 26.9,
          data10: 16.5,
          data11: 0.4176,
          data12: 1.17,
          data13: 0.72,
          data14: 0.0182,
          data15: 9.08,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "",
          data4: "平",
          data5: "栗钙土",
          data6: "白城3",
          data7: 23,
          data8: 500,
          data9: 25.7,
          data10: 17.3,
          data11: 0.4021,
          data12: 1.12,
          data13: 0.75,
          data14: 0.0175,
          data15: 8.74,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "",
          data4: "平",
          data5: "栗钙土",
          data6: "小黑杨",
          data7: 23,
          data8: 500,
          data9: 25.9,
          data10: 20.7,
          data11: 0.4919,
          data12: 1.13,
          data13: 0.9,
          data14: 0.0214,
          data15: 10.69,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "",
          data4: "平",
          data5: "栗钙土",
          data6: "小黑14",
          data7: 23,
          data8: 500,
          data9: 27,
          data10: 21,
          data11: 0.5407,
          data12: 1.17,
          data13: 0.91,
          data14: 0.0235,
          data15: 11.75,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "",
          data4: "平",
          data5: "栗钙土",
          data6: "北京杨",
          data7: 23,
          data8: 170,
          data9: 35.2,
          data10: 23.5,
          data11: 1.0086,
          data12: 1.53,
          data13: 1.02,
          data14: 0.0439,
          data15: 7.45,
          data16: "破肚子",
        },
        {
          data1: "",
          data2: "",
          data3: "",
          data4: "平",
          data5: "栗钙土",
          data6: "小青黑",
          data7: 23,
          data8: 500,
          data9: 28.5,
          data10: 21.3,
          data11: 0.6084,
          data12: 1.24,
          data13: 0.93,
          data14: 0.0265,
          data15: 13.22,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "",
          data4: "平",
          data5: "栗钙土",
          data6: "银中杨",
          data7: 23,
          data8: 500,
          data9: 31.1,
          data10: 24,
          data11: 0.8139,
          data12: 1.35,
          data13: 1.04,
          data14: 0.0354,
          data15: 17.69,
          data16: "",
        },
        {
          data1: "",
          data2: "富裕县(D3)",
          data3: "富路镇兴胜村",
          data4: "平",
          data5: "黑钙土",
          data6: "银中杨",
          data7: 20,
          data8: 500,
          data9: 31.8,
          data10: 22.5,
          data11: 0.794,
          data12: 1.59,
          data13: 1.13,
          data14: 0.0397,
          data15: 19.85,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "",
          data4: "平",
          data5: "黑钙土",
          data6: "小黑杨",
          data7: 23,
          data8: 833,
          data9: 26,
          data10: 24.6,
          data11: 0.5932,
          data12: 1.13,
          data13: 1.07,
          data14: 0.0258,
          data15: 21.48,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "",
          data4: "平",
          data5: "黑钙土",
          data6: "小黑杨",
          data7: 19,
          data8: 667,
          data9: 21.4,
          data10: 19,
          data11: 0.3125,
          data12: 1.13,
          data13: 1,
          data14: 0.0164,
          data15: 10.97,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "富裕林场",
          data4: "平",
          data5: "沙壤土",
          data6: "中黑防",
          data7: 12,
          data8: 1111,
          data9: 17,
          data10: 16.4,
          data11: 0.1728,
          data12: 1.42,
          data13: 1.37,
          data14: 0.0144,
          data15: 16,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "",
          data4: "平",
          data5: "沙壤土",
          data6: "银中杨",
          data7: 21,
          data8: 833,
          data9: 25.8,
          data10: 21.9,
          data11: 0.5178,
          data12: 1.23,
          data13: 1.04,
          data14: 0.0247,
          data15: 20.54,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "",
          data4: "平",
          data5: "沙壤土",
          data6: "小黑杨",
          data7: 27,
          data8: 833,
          data9: 23,
          data10: 21.8,
          data11: 0.4139,
          data12: 0.85,
          data13: 0.81,
          data14: 0.0153,
          data15: 12.77,
          data16: "",
        },
        {
          data1: "",
          data2: "龙江县(D3)",
          data3: "错海林场",
          data4: "平",
          data5: "沙壤土",
          data6: "小黑杨",
          data7: 23,
          data8: 625,
          data9: 20.2,
          data10: 16.8,
          data11: 0.2463,
          data12: 0.88,
          data13: 0.73,
          data14: 0.0107,
          data15: 6.69,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "",
          data4: "平",
          data5: "沙壤土",
          data6: "青山杨",
          data7: 9,
          data8: 833,
          data9: 14.9,
          data10: 18.2,
          data11: 0.1497,
          data12: 1.66,
          data13: 2.02,
          data14: 0.0166,
          data15: 13.86,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "",
          data4: "平",
          data5: "沙壤土",
          data6: "小黑杨",
          data7: 10,
          data8: 833,
          data9: 15.4,
          data10: 14.8,
          data11: 0.1285,
          data12: 1.54,
          data13: 1.48,
          data14: 0.0129,
          data15: 10.7,
          data16: "",
        },
        {
          data1: "",
          data2: "甘南县(D3)",
          data3: "甘南林场",
          data4: "平",
          data5: "栗钙土",
          data6: "小黑杨",
          data7: 3,
          data8: 3333,
          data9: 3.8,
          data10: 6,
          data11: 0.0035,
          data12: 1.27,
          data13: 2,
          data14: 0.0012,
          data15: 3.89,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "",
          data4: "平",
          data5: "栗钙土",
          data6: "青山杨",
          data7: 3,
          data8: 3333,
          data9: 6.3,
          data10: 8,
          data11: 0.0123,
          data12: 2.1,
          data13: 2.67,
          data14: 0.0041,
          data15: 14.44,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "",
          data4: "平",
          data5: "栗钙土",
          data6: "小黑杨",
          data7: 19,
          data8: 1111,
          data9: 16.6,
          data10: 17.4,
          data11: 0.1756,
          data12: 0.87,
          data13: 0.92,
          data14: 0.0092,
          data15: 10.27,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "音河镇山湾村",
          data4: "平",
          data5: "沙壤土",
          data6: "银中杨",
          data7: 16,
          data8: 400,
          data9: 20.7,
          data10: 14.4,
          data11: 0.2198,
          data12: 1.29,
          data13: 0.9,
          data14: 0.0137,
          data15: 5.5,
          data16: "",
        },
      ],
    };
  },
  methods: {
    to_img() {
      this.$router.push({ path: "/show_img_wood" });
    },
    tz() {
      this.$router.push({ path: "/heat_other" });
    },
    change: function (index) {
      this.number = index; //重要处
    },
  },
  mounted() {
    this.$axios({
      method: "get",
      url: "http://127.0.0.1:8000/api/heat_qq/",
    }).then((res) => {
      console.log(res.data);
      console.log(res.data.src);
      this.src = res.data.src;
    });
    this.$axios({
      method: "get",
      url: "http://127.0.0.1:8000/api/draw_box_plot_qq/",
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
.btn_anniu {
  width: 10%;
  padding: 15px;
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