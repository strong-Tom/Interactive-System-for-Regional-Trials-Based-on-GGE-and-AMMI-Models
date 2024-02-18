<template>
  <div>
    <div class="btn_switch">
      <button
        class="btn_anniu"
        @click="change(0)"
        :class="{ newStyle: 0 === number }"
      >
        黑青杨气象因子相关性分析热力图
      </button>

      <button
        class="btn_anniu"
        @click="change(1)"
        :class="{ newStyle: 1 === number }"
      >
        不同处理下黑青杨树高和胸径均值
      </button>

      <button
        class="btn_anniu"
        @click="change(2)"
        :class="{ newStyle: 2 === number }"
      >
        不同处理下黑青杨树高方差分析
      </button>
      <button
        class="btn_anniu"
        @click="change(3)"
        :class="{ newStyle: 3 === number }"
      >
        不同处理下黑青杨胸径方差分析
      </button>
      <button
        class="btn_anniu"
        @click="change(4)"
        :class="{ newStyle: 4 === number }"
      >
        不同处理下黑青杨材积方差分析
      </button>
      <el-button type="primary" size="default" @click="tz">
        跳转到下一个品种页面</el-button
      >
    </div>

    <div>
      <div v-show="0 === number">
        <div
          style="display: flex; align-items: center; justify-content: center"
        >
          <img :src="src" />
        </div>
      </div>
      <div v-show="1 === number">
        <el-table
          :data="tableData"
          height="350"
          border
          style="width: 100%"
          :header-cell-style="{ textAlign: 'center', color: '#000' }"
          :cell-style="{ textAlign: 'center' }"
        >
          <el-table-column prop="data1" label="区组" width="180">
          </el-table-column>
          <el-table-column label="修枝1/4" width="180">
            <el-table-column prop="data2" label="H(m)"> </el-table-column>
            <el-table-column prop="data3" label="D1.3(cm)"> </el-table-column>
          </el-table-column>
          <el-table-column label="修枝1/3" width="180">
            <el-table-column prop="data4" label="H(m)"> </el-table-column>
            <el-table-column prop="data5" label="D1.3(cm)"> </el-table-column
          ></el-table-column>
          <el-table-column label="修枝1/2" width="180">
            <el-table-column prop="data6" label="H(m)"> </el-table-column>
            <el-table-column prop="data7" label="D1.3(cm)"> </el-table-column
          ></el-table-column>
          <el-table-column label="CK" width="180">
            <el-table-column prop="data8" label="H(m)"> </el-table-column>
            <el-table-column prop="data9" label="D1.3(cm)"> </el-table-column
          ></el-table-column>
        </el-table>
        <h5>
          <el-tooltip
            class="item"
            effect="dark"
            content="修枝1/4的最好，修枝1/2最差，但修枝1/4、1/3和ck无显著差异，3者与修枝1/2的差异达极显著水平，说明修枝1/2的强度过大，影响树木生长，1/4强度修枝仅在胸径增量上效果稍好，仅比对照胸径生长量高0.4 %。"
            placement="top-start"
            ><el-button type="danger" size="medium">表1 </el-button></el-tooltip
          >不同处理下黑青杨树高和胸径均值
        </h5>
      </div>
      <div v-show="2 === number">
        <el-table
          :data="tableData2"
          height="200"
          border
          style="width: 100%"
          :header-cell-style="{ textAlign: 'center', color: '#000' }"
          :cell-style="{ textAlign: 'center' }"
        >
          <el-table-column prop="data1" label="变异来源" width="180">
          </el-table-column>

          <el-table-column prop="data2" label="df"> </el-table-column>
          <el-table-column prop="data3" label="均方"> </el-table-column>

          <el-table-column prop="data4" label="F"> </el-table-column>
          <el-table-column prop="data5" label="Sig."> </el-table-column>
        </el-table>
        <h5>
          <el-button type="danger" size="medium" @click="to_img">表2 </el-button
          >不同处理下黑青杨树高方差分析
        </h5>
      </div>
      <div v-show="3 === number">
        <el-table
          :data="tableData3"
          height="200"
          border
          style="width: 100%"
          :header-cell-style="{ textAlign: 'center', color: '#000' }"
          :cell-style="{ textAlign: 'center' }"
        >
          <el-table-column prop="data1" label="变异来源" width="180">
          </el-table-column>

          <el-table-column prop="data2" label="df"> </el-table-column>
          <el-table-column prop="data3" label="均方"> </el-table-column>

          <el-table-column prop="data4" label="F"> </el-table-column>
          <el-table-column prop="data5" label="Sig."> </el-table-column>
        </el-table>
        <h5>表3 不同处理下黑青杨胸径方差分析</h5>
      </div>
      <div v-show="4 === number">
        <el-table
          :data="tableData4"
          height="200"
          border
          style="width: 100%"
          :header-cell-style="{ textAlign: 'center', color: '#000' }"
          :cell-style="{ textAlign: 'center' }"
        >
          <el-table-column prop="data1" label="变异来源" width="180">
          </el-table-column>

          <el-table-column prop="data2" label="df"> </el-table-column>
          <el-table-column prop="data3" label="均方"> </el-table-column>

          <el-table-column prop="data4" label="F"> </el-table-column>
          <el-table-column prop="data5" label="Sig."> </el-table-column>
        </el-table>
        <h5>表4 不同处理下黑青杨材积方差分析</h5>
      </div>
    </div>
  </div>
</template>
  
  <script>
export default {
  name: "FrontendDiameterDq",

  data() {
    return {
      tableData4: [
        { data1: "区组", data2: 3, data3: 0.017, data4: 7.929, data5: 0 },
        {
          data1: "修枝强度",
          data2: 3,
          data3: 0.011,
          data4: 4.997,
          data5: 0.002,
        },
        { data1: "区组×系号", data2: 9, data3: 0.024, data4: 11.381, data5: 0 },
      ],
      tableData3: [
        { data1: "区组", data2: 3, data3: 57.546, data4: 6.51, data5: 0 },
        { data1: "处理", data2: 3, data3: 44.297, data4: 5.012, data5: 0.002 },
        { data1: "区组×处理", data2: 9, data3: 68.872, data4: 7.792, data5: 0 },
      ],
      tableData2: [
        { data1: "区组", data2: 3, data3: 13.526, data4: 10.303, data5: 0 },
        { data1: "处理", data2: 3, data3: 1.369, data4: 1.043, data5: 0.373 },
        { data1: "区组×处理", data2: 9, data3: 13.83, data4: 10.534, data5: 0 },
      ],
      tableData: [
        {
          data1: "Ⅰ区",
          data2: 10.8,
          data3: 14.4,
          data4: 11.3,
          data5: 14.5,
          data6: 11,
          data7: 13.4,
          data8: 12.6,
          data9: 17.3,
        },
        {
          data1: "Ⅱ区",
          data2: 11.5,
          data3: 15,
          data4: 11.7,
          data5: 16.1,
          data6: 11.9,
          data7: 15.4,
          data8: 11.4,
          data9: 15.9,
        },
        {
          data1: "Ⅲ区",
          data2: 12.3,
          data3: 15.9,
          data4: 12.4,
          data5: 17.8,
          data6: 11.7,
          data7: 15.6,
          data8: 11.7,
          data9: 15.6,
        },
        {
          data1: "Ⅳ区",
          data2: 12.2,
          data3: 17.6,
          data4: 11.2,
          data5: 13.9,
          data6: 10.7,
          data7: 12.8,
          data8: 10.6,
          data9: 13.5,
        },
        {
          data1: "均值",
          data2: 11.7,
          data3: 15.73,
          data4: 11.65,
          data5: 15.58,
          data6: 11.33,
          data7: 14.3,
          data8: 11.58,
          data9: 15.58,
        },
      ],
      src: null,
      number: 0,
    };
  },

  mounted() {
    console.log(555);
    this.$axios({
      method: "get",
      url: "http://127.0.0.1:8000/api/heat_hqy/",
    }).then((res) => {
      console.log(res.data);
      console.log(res.data.src);
      this.src = res.data.src;
    });
  },

  methods: {
    tz() {
      this.$router.push({ path: "/heat_yzy" });
    },
    to_img() {
      top.location.href = "/#/show_img_hqy";
    },
    change: function (index) {
      this.number = index; //重要处
    },
  },
};
</script>
  
  <style lang="less" scoped>
.btn_anniu {
  width: 15%;
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