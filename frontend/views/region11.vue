<template>
  <div>
    <div class="head" style="display: flex;justify-content:space-around;">
      <h5>(Ⅰ) 北部丘陵寒冷区</h5>
      <el-button type="primary" size="default" @click="tz">
        跳转到下一个生态区页面</el-button>
    </div>
    <el-table :data="tableData" height="610px" border style="width: 100%"
      :header-cell-style="{ textAlign: 'center', color: '#000' }" :cell-style="{ textAlign: 'center' }">
      <el-table-column prop="data1" label="地市"> </el-table-column>
      <el-table-column prop="data2" label="测定小区"> </el-table-column>
      <el-table-column prop="data3" label="地点"> </el-table-column>
      <el-table-column prop="data4" label="坡度"> </el-table-column>

      <el-table-column prop="data5" label="土壤类型"> </el-table-column>
      <el-table-column prop="data6" label="树种"> </el-table-column>
      <el-table-column prop="data7" label="林龄"> </el-table-column>

      <el-table-column prop="data8" label="密度(株/hm²)" width="120px"> </el-table-column>
      <el-table-column label="总生长量">
        <el-table-column prop="data9" label="D1.3（cm）" width="120px"> </el-table-column>
        <el-table-column prop="data10" label="H(m)"> </el-table-column>
        <el-table-column prop="data11" label="V(m³)"> </el-table-column>
      </el-table-column>
      <el-table-column label="年均生长量">
        <el-table-column prop="data12" label="D1.3（cm）" width="130">
        </el-table-column>
        <el-table-column prop="data13" label="H(m)"> </el-table-column>
        <el-table-column prop="data14" label="V(m³)"> </el-table-column>
      </el-table-column>

      <el-table-column prop="data15" label="年蓄积生长量(m³/hm²)" width="200px">
      </el-table-column>
      <el-table-column prop="data16" label="备注"> </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: "FrontendRegion11",

  data() {
    return {
      tableData: [
        {
          data1: "黑河(E)",
          data2: "黑河郊区（E1）",
          data3: "西岗子镇",
          data4: "平",
          data5: "黑土",
          data6: "银中杨",
          data7: 5,
          data8: 5000,
          data9: 5.5,
          data10: 5,
          data11: 0.0058,
          data12: 1.1,
          data13: 1,
          data14: 0.0012,
          data15: 5.8,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "",
          data4: "平",
          data5: "黑土",
          data6: "小黑杨",
          data7: 5,
          data8: 1667,
          data9: 5.4,
          data10: 6.5,
          data11: 0.0074,
          data12: 1.08,
          data13: 1.3,
          data14: 0.0015,
          data15: 2.47,
          data16: "",
        },
        {
          data1: "",
          data2: "嫩江县(E2)",
          data3: "大西江农场",
          data4: "平",
          data5: "黑土",
          data6: "中黑防",
          data7: 7,
          data8: 2500,
          data9: 6.4,
          data10: 7.5,
          data11: 0.0118,
          data12: 0.91,
          data13: 1.07,
          data14: 0.0017,
          data15: 4.21,
          data16: "冻害",
        },
        {
          data1: "",
          data2: "",
          data3: "通往大西江农场路旁",
          data4: "平",
          data5: "黑钙土",
          data6: "小黑杨",
          data7: 22,
          data8: 1667,
          data9: 16.7,
          data10: 16.4,
          data11: 0.167,
          data12: 0.76,
          data13: 0.75,
          data14: 0.0076,
          data15: 12.65,
          data16: "",
        },
        {
          data1: "",
          data2: "北安(E2)",
          data3: "",
          data4: "平",
          data5: "暗棕壤",
          data6: "银中杨",
          data7: 8,
          data8: 1111,
          data9: 13.57,
          data10: 9.79,
          data11: 0.0657,
          data12: 1.7,
          data13: 1.22,
          data14: 0.0082,
          data15: 9.12,
          data16: "",
        },
        {
          data1: "伊春（L）",
          data2: "嘉荫县（L1）",
          data3: "嘉荫县街区",
          data4: "平",
          data5: "黑钙土",
          data6: "银中杨",
          data7: 11,
          data8: "单行3m",
          data9: 12.9,
          data10: "",
          data11: "-",
          data12: 1.17,
          data13: 0,
          data14: 0,
          data15: "-",
          data16: "破肚子",
        },
        {
          data1: "",
          data2: "伊春市区(L2)",
          data3: "带岭林科所门前",
          data4: "平",
          data5: "森林暗棕壤",
          data6: "斯大林",
          data7: 30,
          data8: "单行3m",
          data9: 54.1,
          data10: 25.1,
          data11: 2.4542,
          data12: 1.8,
          data13: 0.84,
          data14: 0.0818,
          data15: "-",
          data16: "单行",
        },
        {
          data1: "",
          data2: "",
          data3: "带岭区碧水林场",
          data4: "平",
          data5: "暗棕壤",
          data6: "小黑杨",
          data7: 24,
          data8: 1111,
          data9: 17.3,
          data10: 17.1,
          data11: 0.1866,
          data12: 0.72,
          data13: 0.71,
          data14: 0.0078,
          data15: 8.64,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "带岭区永翠林场",
          data4: "5°",
          data5: "暗棕壤",
          data6: "大青杨",
          data7: 17,
          data8: 833,
          data9: 21.9,
          data10: 19.2,
          data11: 0.3302,
          data12: 1.29,
          data13: 1.13,
          data14: 0.0194,
          data15: 16.19,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "伊春林科院植物园",
          data4: "平",
          data5: "暗棕壤",
          data6: "香杨",
          data7: 24,
          data8: 1111,
          data9: 21.9,
          data10: 19.4,
          data11: 0.3338,
          data12: 0.91,
          data13: 0.81,
          data14: 0.0139,
          data15: 15.45,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "伊春林科院试验站",
          data4: "平",
          data5: "暗棕壤",
          data6: "伊林7(大青杨)",
          data7: 24,
          data8: "单行3m",
          data9: 27.4,
          data10: 20.9,
          data11: 0.5533,
          data12: 1.14,
          data13: 0.87,
          data14: 0.0231,
          data15: "-",
          data16: "单行",
        },
        {
          data1: "",
          data2: "铁力市(L3)",
          data3: "王杨乡工农林场",
          data4: "平",
          data5: "黑土",
          data6: "A5",
          data7: 5,
          data8: 3333,
          data9: 8.5,
          data10: 8.6,
          data11: 0.0235,
          data12: 1.7,
          data13: 1.72,
          data14: 0.0047,
          data15: 15.67,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "",
          data4: "平",
          data5: "黑土",
          data6: "A43",
          data7: 4,
          data8: 2222,
          data9: 9.1,
          data10: 10.1,
          data11: 0.0316,
          data12: 2.28,
          data13: 2.53,
          data14: 0.0079,
          data15: 17.56,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "王杨乡农场8连",
          data4: "平",
          data5: "黑土",
          data6: "银中杨",
          data7: 4,
          data8: 3333,
          data9: 6.3,
          data10: 9.8,
          data11: 0.0152,
          data12: 1.58,
          data13: 2.45,
          data14: 0.0038,
          data15: 12.65,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "王杨乡红星农场",
          data4: "平",
          data5: "黑土",
          data6: "小黑杨",
          data7: 5,
          data8: 3333,
          data9: 6.6,
          data10: 7.4,
          data11: 0.0124,
          data12: 1.32,
          data13: 1.48,
          data14: 0.0025,
          data15: 8.27,
          data16: "",
        },
      ],
    };
  },

  mounted() { },

  methods: {
    tz() {
      this.$router.push({ path: "/region12" });
    },
  },
};
</script>

<style lang="less" scoped></style>