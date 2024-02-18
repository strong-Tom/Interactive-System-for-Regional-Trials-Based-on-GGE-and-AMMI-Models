<template>
  <div>
    <div class="head" style="display: flex;justify-content:space-around;">
      <h5>(Ⅴ) 东南部山地湿润、半湿润区</h5>
    </div>
    <el-table
      :data="tableData"
      height="610px"
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
          data1: "牡丹江(F)",
          data2: "宁安县(F2)",
          data3: "宁安县市郊",
          data4: "平",
          data5: "暗棕壤",
          data6: "小黑杨",
          data7: 17,
          data8: 500,
          data9: 28.8,
          data10: 19,
          data11: 0.551,
          data12: 1.69,
          data13: 1.12,
          data14: 0.0324,
          data15: 16.21,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "",
          data4: "平",
          data5: "暗棕壤",
          data6: "迎春5号",
          data7: 4,
          data8: 2500,
          data9: 9,
          data10: 11,
          data11: 0.0338,
          data12: 2.25,
          data13: 2.75,
          data14: 0.0085,
          data15: 21.13,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "",
          data4: "平",
          data5: "暗棕壤",
          data6: "中黑防",
          data7: 4,
          data8: 2500,
          data9: 9,
          data10: 10.5,
          data11: 0.0322,
          data12: 2.25,
          data13: 2.63,
          data14: 0.0081,
          data15: 20.13,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "",
          data4: "平",
          data5: "暗棕壤",
          data6: "中绥12",
          data7: 17,
          data8: 625,
          data9: 27.1,
          data10: 16,
          data11: 0.4102,
          data12: 1.59,
          data13: 0.94,
          data14: 0.0241,
          data15: 15.08,
          data16: "烂皮病",
        },
        {
          data1: "",
          data2: "东宁县(F3)",
          data3: "东宁县周围",
          data4: "平",
          data5: "草甸土",
          data6: "小黑杨",
          data7: 6,
          data8: 1667,
          data9: 6.1,
          data10: 6.5,
          data11: 0.0093,
          data12: 1.02,
          data13: 1.08,
          data14: 0.0016,
          data15: 2.58,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "",
          data4: "平",
          data5: "草甸土",
          data6: "小黑杨",
          data7: 20,
          data8: 833,
          data9: 22.6,
          data10: 20,
          data11: 0.3659,
          data12: 1.13,
          data13: 1,
          data14: 0.0183,
          data15: 15.24,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "",
          data4: "平",
          data5: "白浆土",
          data6: "银中杨",
          data7: 10,
          data8: 1250,
          data9: 10.9,
          data10: 7.5,
          data11: 0.0327,
          data12: 1.09,
          data13: 0.75,
          data14: 0.0033,
          data15: 4.09,
          data16: "",
        },
        {
          data1: "",
          data2: "",
          data3: "暖泉乡二村",
          data4: "平",
          data5: "暗棕壤",
          data6: "小黑杨",
          data7: 6,
          data8: 2500,
          data9: 9.9,
          data10: 8,
          data11: 0.0291,
          data12: 1.65,
          data13: 1.33,
          data14: 0.0049,
          data15: 12.13,
          data16: "",
        },
        {
          data1: "鸡西(G)",
          data2: "鸡东县(G1)",
          data3: "永和镇新和村",
          data4: "5°",
          data5: "草甸白浆土",
          data6: "迎春5号",
          data7: 5,
          data8: 833,
          data9: 11.6,
          data10: 11,
          data11: 0.0549,
          data12: 2.32,
          data13: 2.2,
          data14: 0.011,
          data15: 9.15,
          data16: "",
        },
        {
          data1: "",
          data2: "市内(G1)",
          data3: "恒山区",
          data4: "5°",
          data5: "暗棕壤",
          data6: "迎春5号",
          data7: 12,
          data8: 833,
          data9: 23,
          data10: 16,
          data11: 0.2999,
          data12: 1.92,
          data13: 1.33,
          data14: 0.025,
          data15: 20.82,
          data16: "",
        },
        {
          data1: "",
          data2: "虎林市(G2)",
          data3: "虎宝林场",
          data4: "平",
          data5: "白浆土",
          data6: "迎春5号",
          data7: 15,
          data8: 556,
          data9: 28.5,
          data10: 20.7,
          data11: 0.5905,
          data12: 1.9,
          data13: 1.38,
          data14: 0.0394,
          data15: 21.88,
          data16: "",
        },
      ],
    };
  },

  mounted() {},

  methods: {},
};
</script>
    
    <style lang="less" scoped>
</style>