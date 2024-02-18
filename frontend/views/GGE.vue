<template>
  <div style="display: flex; justify-content: space-between; margin-top: 10px">
    <div class="btn_switch">
      <button
        class="btn_anniu"
        @click="change(0)"
        :class="{ newStyle: 0 === number }"
      >
      Variety Yield and Stability Chart
      </button>
      <button
        class="btn_anniu"
        @click="change(1)"
        :class="{ newStyle: 1 === number }"
      >
      Which won Where
      </button>
    </div>
    <div v-show="0 === number">
      <el-image style="width: 1000px; height: 700px" :src="GGE_1" :fit="fit">
        <div slot="error" class="image-slot">
          <!-- <i class="el-icon-picture-outline"></i> -->
          <!-- :src="require('../src/assets/images/fail.jpeg')" -->
          <el-image
            style="width: 700px; height: 700px"
            fit="fill"
          ></el-image></div
      ></el-image>
    </div>
    <div v-show="1 === number">
      <el-image style="width: 1000px; height: 700px" :src="GGE_2" :fit="fit">
        <div slot="error" class="image-slot">
          <!-- <i class="el-icon-picture-outline"></i> -->
          <el-image
            style="width: 700px; height: 700px"
            
            fit="fill"
          ></el-image></div
      ></el-image>
    </div>
    <el-form ref="form" :model="form" label-width="80px">
      <el-form-item label="Select file">
        <el-select v-model="form.region" placeholder="please select the file">
          <el-option
            v-for="item in file"
            :label="item.name"
            :key="item.id"
            :value="item.name"
          ></el-option>
        </el-select>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">Confirm</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
  <script>
export default {
  data() {
    return {
      number: 0,
      GGE_1: null,
      GGE_2: null,
      file: null,
      form: {
        region: "",
      },
    };
  },
  mounted() {
    this.$axios({
      method: "get",
      url: "http://127.0.0.1:8000/api/SaveFile/",
      // data: { place:3,clone:1 },
    }).then((res) => {
      console.log(res.data);
      this.file = res.data;
    });
  },
  methods: {
    change: function (index) {
      this.number = index; //重要处
    },
    onSubmit() {
      this.$axios({
        method: "post",
        url: "http://127.0.0.1:8000/api/GGE_1/",
        data: { file: this.form.region },
      }).then((res) => {
        if (res.data.code == -2) {
          this.$message.error("文件内容有错误，请选择正确的文件");
        }
        // console.log("src is", res.data.GGE_1, "src1 is", res.data.GGE_2);
        this.GGE_1 = res.data.GGE_1;
        this.GGE_2 = res.data.GGE_2;
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