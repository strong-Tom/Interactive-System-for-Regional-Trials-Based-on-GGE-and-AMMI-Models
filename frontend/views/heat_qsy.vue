<template>
  <div>
    <div class="btn_switch">
      <button
        class="btn_anniu"
        @click="change(0)"
        :class="{ newStyle: 0 === number }"
      >
      青山杨气象因子相关性分析热力图
      </button>

      <button
        class="btn_anniu"
        @click="change(1)"
        :class="{ newStyle: 1 === number }"
      >
        17年生青山杨疏伐试验林生长量
      </button>

      <button
        class="btn_anniu"
        @click="change(2)"
        :class="{ newStyle: 2 === number }"
      >
        17年生青山杨疏伐试验林材积生长量方差分析
      </button>
      <button
        class="btn_anniu"
        @click="change(3)"
        :class="{ newStyle: 3 === number }"
      >
        间伐试验设计
      </button>
      <button
        class="btn_anniu"
        @click="change(4)"
        :class="{ newStyle: 4 === number }"
      >
       施肥处理下错海林场14年生青山杨树高方差分析
      </button>
      <button
        class="btn_anniu"
        @click="change(5)"
        :class="{ newStyle: 5 === number }"
      >
        施肥处理下错海林场青山杨胸径方差分析
      </button>
      <button
        class="btn_anniu"
        @click="change(6)"
        :class="{ newStyle: 6 === number }"
      >
        L9（34）正交试验表
      </button>
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
          <el-table-column prop="data1" label="处理" width="180">
          </el-table-column>
          <el-table-column label="Ⅰ" width="180">
            <el-table-column prop="data2" label="H"> </el-table-column>
            <el-table-column prop="data3" label="D1.3"> </el-table-column>
          </el-table-column>
          <el-table-column label="Ⅱ" width="180">
            <el-table-column prop="data4" label="H"> </el-table-column>
            <el-table-column prop="data5" label="D1.3"> </el-table-column
          ></el-table-column>
          <el-table-column label="Ⅲ" width="180">
            <el-table-column prop="data6" label="H"> </el-table-column>
            <el-table-column prop="data7" label="D1.3"> </el-table-column
          ></el-table-column>
          <el-table-column label="Ⅳ" width="180">
            <el-table-column prop="data8" label="H"> </el-table-column>
            <el-table-column prop="data9" label="D1.3"> </el-table-column
          ></el-table-column>
          <el-table-column label="平均值" width="180">
            <el-table-column prop="data10" label="H"> </el-table-column>
            <el-table-column prop="data11" label="D1.3"> </el-table-column
          ></el-table-column>
        </el-table>
        <h5>
          <el-tooltip
            class="item"
            effect="dark"
            content="疏伐后营养空间较大的处理C（4 m × 6 m）、B（6 m × 3 m）和A（4 m × 3 m）树高、胸径和单株材积生长均高于对照初植林D（2 m × 3 m），其中单株材积生长量分别比对照高62.2 %、51.1 %和36.7 %。"
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
          <el-tooltip
            class="item"
            effect="dark"
            content="初植株行距越小，单位蓄积量越高，越利于杨树纤维用材林培育，株行距2 m × 3 m较适合；对于培育杨树刨花板等大径材用材林，需要定植6 m × 3 m、4 m × 6 m等大株行距的用材林较为合适。"
            placement="top-start"
          >
            <el-button type="danger" size="medium">表2 </el-button>
          </el-tooltip>
          17年生青山杨疏伐试验林材积生长量方差分析
        </h5>
      </div>
      <div v-show="3 === number">
        <el-table
          :data="tableData3"
          height="250"
          border
          style="width: 100%"
          :header-cell-style="{ textAlign: 'center', color: '#000' }"
          :cell-style="{ textAlign: 'center' }"
        >
          <el-table-column prop="data1" label="处理" width="180">
          </el-table-column>

          <el-table-column prop="data2" label="原始株行距"> </el-table-column>
          <el-table-column prop="data3" label="原始林分密度"> </el-table-column>

          <el-table-column prop="data4" label="目标株行距"> </el-table-column>
          <el-table-column prop="data5" label="目标林分密度"> </el-table-column>
        </el-table>
        <h5>
          <el-button type="danger" size="medium" @click="to_img">表3 </el-button
          >间伐试验设计
        </h5>
      </div>
      <div v-show="4 === number">
        <el-table
          :data="tableData4"
          height="250"
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
          <el-tooltip
            class="item"
            effect="dark"
            content="在土地较瘠薄的龙江县错海林场，对14年生青山杨林分进行施肥效果较好，林木材积生长可提高15.6 %，5月中旬施肥最好，施肥种类以磷肥为好，施肥量200 g/株为宜，灌水对林木生长影响不大。"
            placement="top-start"
            ><el-button type="danger" size="medium">表4 </el-button></el-tooltip
          >不同处理下错海林场14年生青山杨树高方差分析
        </h5>
      </div>
      <div v-show="5 === number">
        <el-table
          :data="tableData5"
          height="250"
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
        <h5>表5 不同处理下错海林场青山杨胸径方差分析</h5>
      </div>
      <div v-show="6 === number">
        <el-table
          :data="tableData6"
          height="500"
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
          <el-button type="danger" size="medium" @click="to_img1"
            >表6 </el-button
          >L9（34）正交试验表
        </h5>
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
        { data1: "施肥时间", data2: 2, data3: 28.746, data4: 22.555, data5: 0 },
        {
          data1: "施肥种类",
          data2: 2,
          data3: 3.972,
          data4: 3.117,
          data5: 0.045,
        },
        { data1: "施肥量", data2: 2, data3: 4.076, data4: 3.198, data5: 0.042 },
        { data1: "灌水", data2: 2, data3: 10.083, data4: 7.911, data5: 0 },
      ],
      tableData5: [
        { data1: "施肥时间", data2: 2, data3: 10.213, data4: 11.038, data5: 0 },
        {
          data1: "施肥种类",
          data2: 2,
          data3: 6.352,
          data4: 6.865,
          data5: 0.001,
        },
        { data1: "施肥量", data2: 2, data3: 8.534, data4: 9.223, data5: 0 },
        { data1: "灌水", data2: 2, data3: 9.133, data4: 9.871, data5: 0 },
      ],
      tableData6: [
        {
          data1: 1,
          data2: "1（5月中旬）",
          data3: "1（N肥）",
          data4: "1（0 g）",
          data5: "1（0 kg）",
        },
        {
          data1: 2,
          data2: "1（5月中旬）",
          data3: "2（P肥）",
          data4: "2（100 g）",
          data5: "2（15 kg）",
        },
        {
          data1: 3,
          data2: "1（5月中旬）",
          data3: "3（复合肥）",
          data4: "3（200 g）",
          data5: "3（30 kg）",
        },
        {
          data1: 4,
          data2: "2（6月中旬）",
          data3: "1（N肥）",
          data4: "2（100 g）",
          data5: "3（30 kg）",
        },
        {
          data1: 5,
          data2: "2（6月中旬）",
          data3: "2（P肥）",
          data4: "3（200 g）",
          data5: "1（0 kg）",
        },
        {
          data1: 6,
          data2: "2（6月中旬）",
          data3: "3（复合肥）",
          data4: "1（0 g）",
          data5: "2（15 kg）",
        },
        {
          data1: 7,
          data2: "3（7月中旬）",
          data3: "1（N肥）",
          data4: "3（200 g）",
          data5: "2（15 kg）",
        },
        {
          data1: 8,
          data2: "3（7月中旬）",
          data3: "2（P肥）",
          data4: "1（0 g）",
          data5: "3（30 kg）",
        },
        {
          data1: 9,
          data2: "3（7月中旬）",
          data3: "3（复合肥）",
          data4: "2（100 g）",
          data5: "1（0 kg）",
        },
      ],
      tableData3: [
        {
          data1: "A",
          data2: "2m×3m",
          data3: "1667株/公顷",
          data4: "4m×3m",
          data5: "833株/公顷",
        },
        {
          data1: "B",
          data2: "2m×3m",
          data3: "1667株/公顷",
          data4: "6m×3m",
          data5: "556株/公顷",
        },
        {
          data1: "C",
          data2: "2m×3m",
          data3: "1667株/公顷",
          data4: "4m×6m",
          data5: "417株/公顷",
        },
        {
          data1: "D（CK）",
          data2: "2m×3m",
          data3: "1667株/公顷",
          data4: "2m×3m",
          data5: "1667株/公顷",
        },
      ],
      tableData2: [
        { data1: "区组", data2: 3, data3: 0.028, data4: 3.981, data5: 0.008 },
        { data1: "处理", data2: 3, data3: 0.225, data4: 31.42, data5: 0 },
        {
          data1: "区组×处理",
          data2: 9,
          data3: 0.024,
          data4: 3.337,
          data5: 0.001,
        },
      ],
      tableData: [
        {
          data1: "A（4m×3m）",
          data2: 15.87,
          data3: 17.44,
          data4: 16.71,
          data5: 16.61,
          data6: 17.16,
          data7: 18.5,
          data8: 16.91,
          data9: 20.29,
          data10: 18.2,
          data11: 16.66,
        },
        {
          data1: "B（6m×3m）",
          data2: 17.8,
          data3: 19.42,
          data4: 17.16,
          data5: 18.32,
          data6: 17.72,
          data7: 19.42,
          data8: 15.97,
          data9: 19.32,
          data10: 19.12,
          data11: 17.16,
        },
        {
          data1: "C（4m×6m）",
          data2: 17.64,
          data3: 19.7,
          data4: 18.62,
          data5: 19.85,
          data6: 16.91,
          data7: 20.5,
          data8: 15.67,
          data9: 19.2,
          data10: 19.81,
          data11: 17.21,
        },
        {
          data1: "D（2m×3m）（ck）",
          data2: 17.41,
          data3: 16.36,
          data4: 15.73,
          data5: 13.97,
          data6: 16.59,
          data7: 17.25,
          data8: 14.23,
          data9: 16.04,
          data10: 15.91,
          data11: 15.99,
        },
        {
          data1: "平均值",
          data2: 17.18,
          data3: 18.23,
          data4: 17.06,
          data5: 17.19,
          data6: 17.1,
          data7: 18.92,
          data8: 15.7,
          data9: 18.71,
          data10: 18.26,
          data11: 16.76,
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
      url: "http://127.0.0.1:8000/api/heat_qsy/",
    }).then((res) => {
      console.log(res.data);
      console.log(res.data.src);
      this.src = res.data.src;
    });
  },

  methods: {
    to_img() {
      top.location.href = "/#/show_img_qsy";
    },
    to_img1() {
      top.location.href = "/#/show_img_qsy1";
    },
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
  padding-left: 10px;
  padding-right: 10px;
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