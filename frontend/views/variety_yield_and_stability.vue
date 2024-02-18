<template>
  <div style="display: flex; justify-content: space-between; margin-top: 10px">
    <!-- variety_yield_and_stability图 -->
    <div class="ammi">
      <div class="title">WorkPlace</div>
      <div class="name" v-if="src == null">variety_yield_and_stability</div>
      <el-card class="box-card" v-if="src == null">
        <div slot="header" class="clearfix">
          <span class="info_span">Info</span>
        </div>
        <div class="text">
          <strong>No data loaded. </strong><br />
          <div class="card_span">
            You should upload data first. Use toolkit panel on the right side.
          </div>
        </div>
      </el-card>
      <el-image
        class="image_null"
        :src="require('../src/assets/images/loadding4.gif')"
        fit="fill"
        :lazy="true"
        v-if="src == null"
      ></el-image>

      <el-image :src="src" :fit="fit" class="image" v-if="src != null">
        <!-- <div slot="error" class="image-slot"> -->
        <!-- <i class="el-icon-picture-outline"></i> -->
        <!-- :src="require('../src/assets/images/fail.jpeg')" -->
        <!-- <el-image
              style="width: 700px; height: 700px"
              fit="fill"
            ></el-image></div> -->
      </el-image>
    </div>
    <!-- 右侧工具栏 -->
    <div class="tool_box">
      <!-- 按钮组 -->
      <div class="button_club">
        <!-- 上传按钮 -->
        <el-upload
          style="margin-top: 10px; margin-bottom: 10px"
          ref="uploadFile"
          class="upload-demo"
          :before-upload="beforeFileUpload"
          :on-success="onUploadSuccess"
          :http-request="uploadVideo"
          multiple
          accept=".xlsx, .xls,.csv"
          :show-file-list="false"
        >
          <el-button size="primary" type="success">Upload(.csv)</el-button>
        </el-upload>
        <!-- 下载按钮 -->

        <el-button type="warning" size="default" @click="download"
          >Download(.png)</el-button
        >
      </div>

      <!-- 表单 -->
      <div class="form">
        <div class="title">tool box</div>
        <el-form ref="form" :model="form" label-width="80px">
          <!-- 第一行 -->
          <el-row :gutter="20">
            <el-col :span="12"
              ><div class="grid-content bg-purple">
                <el-form-item label="clone scatter color" label-width="10vw">
                  <el-color-picker
                    v-model="form.clone_scatter_color"
                  ></el-color-picker>
                </el-form-item></div
            ></el-col>
            <el-col :span="12"
              ><div class="grid-content bg-purple">
                <el-form-item label="vertical line color" label-width="10vw">
                  <el-color-picker
                    v-model="form.vertical_line_color"
                  ></el-color-picker>
                </el-form-item></div
            ></el-col>
          </el-row>
          <!-- 第二行 -->
          <el-row :gutter="20">
            <el-col :span="12"
              ><div class="grid-content bg-purple">
                <el-form-item label="clone text color" label-width="10vw">
                  <el-color-picker
                    v-model="form.clone_text_color"
                  ></el-color-picker>
                </el-form-item></div
            ></el-col>
            <el-col :span="12"
              ><div class="grid-content bg-purple">
                <el-form-item label="place scatter color" label-width="10vw">
                  <el-color-picker
                    v-model="form.place_scatter_color"
                  ></el-color-picker>
                </el-form-item></div
            ></el-col>
          </el-row>
          <!-- 第三行 -->
          <el-row :gutter="20">
            <el-col :span="12"
              ><div class="grid-content bg-purple">
                <el-form-item label="place text color" label-width="10vw">
                  <el-color-picker
                    v-model="form.place_text_color"
                  ></el-color-picker>
                </el-form-item></div
            ></el-col>
            <el-col :span="12"
              ><div class="grid-content bg-purple">
                <el-form-item label="mean line color" label-width="10vw">
                  <el-color-picker
                    v-model="form.mean_line_color"
                  ></el-color-picker>
                </el-form-item></div
            ></el-col>
          </el-row>
          <!-- 第四行 -->
          <el-row :gutter="20">
            <el-col :span="12"
              ><div class="grid-content bg-purple">
                <el-form-item label="clone scatter size" label-width="10vw">
                  <el-select
                    v-model="form.clone_scatter_size"
                    placeholder="select size"
                  >
                    <el-option
                      v-for="item in scatter_size_list"
                      :label="item"
                      :key="item.id"
                      :value="item"
                    ></el-option>
                  </el-select>
                </el-form-item></div
            ></el-col>
            <el-col :span="12"
              ><div class="grid-content bg-purple">
                <el-form-item label="vertical line size" label-width="10vw">
                  <el-select
                    v-model="form.vertical_line_size"
                    placeholder="select size"
                  >
                    <el-option
                      v-for="item in line_size_list"
                      :label="item"
                      :key="item.id"
                      :value="item"
                    ></el-option>
                  </el-select>
                </el-form-item></div
            ></el-col>
          </el-row>
          <!-- 第五行 -->
          <el-row :gutter="20">
            <el-col :span="12"
              ><div class="grid-content bg-purple">
                <el-form-item label="clone scatter mark" label-width="10vw">
                  <el-select
                    v-model="form.clone_scatter_mark"
                    placeholder="select mark"
                  >
                    <el-option
                      v-for="item in mark_list"
                      :label="item"
                      :key="item.id"
                      :value="item"
                    ></el-option>
                  </el-select>
                </el-form-item></div
            ></el-col>
            <el-col :span="12"
              ><div class="grid-content bg-purple">
                <el-form-item label="clone text size" label-width="10vw">
                  <el-select
                    v-model="form.clone_text_size"
                    placeholder="select size"
                  >
                    <el-option
                      v-for="item in line_size_list"
                      :label="item"
                      :key="item.id"
                      :value="item"
                    ></el-option>
                  </el-select>
                </el-form-item></div
            ></el-col>
          </el-row>
          <!-- 第六行 -->
          <el-row :gutter="20">
            <el-col :span="12"
              ><div class="grid-content bg-purple">
                <el-form-item label="place scatter size" label-width="10vw">
                  <el-select
                    v-model="form.place_scatter_size"
                    placeholder="select size"
                  >
                    <el-option
                      v-for="item in scatter_size_list"
                      :label="item"
                      :key="item.id"
                      :value="item"
                    ></el-option>
                  </el-select>
                </el-form-item></div
            ></el-col>
            <el-col :span="12"
              ><div class="grid-content bg-purple">
                <el-form-item label="place text size" label-width="10vw">
                  <el-select
                    v-model="form.place_text_size"
                    placeholder="select size"
                  >
                    <el-option
                      v-for="item in line_size_list"
                      :label="item"
                      :key="item.id"
                      :value="item"
                    ></el-option>
                  </el-select>
                </el-form-item></div
            ></el-col>
          </el-row>
          <!-- 第七行 -->
          <el-row :gutter="20">
            <el-col :span="12"
              ><div class="grid-content bg-purple">
                <el-form-item label="place scatter mark" label-width="10vw">
                  <el-select
                    v-model="form.place_scatter_mark"
                    placeholder="select size"
                  >
                    <el-option
                      v-for="item in mark_list"
                      :label="item"
                      :key="item.id"
                      :value="item"
                    ></el-option>
                  </el-select>
                </el-form-item></div
            ></el-col>
            <el-col :span="12"
              ><div class="grid-content bg-purple">
                <el-form-item label="mean line size" label-width="10vw">
                  <el-select
                    v-model="form.mean_line_size"
                    placeholder="select size"
                  >
                    <el-option
                      v-for="item in line_size_list"
                      :label="item"
                      :key="item.id"
                      :value="item"
                    ></el-option>
                  </el-select>
                </el-form-item></div
            ></el-col>
          </el-row>
          <!-- 提交按钮 -->
          <el-form-item>
            <el-button type="primary" @click="onSubmit" class="confirm"
              >Confirm</el-button
            >
          </el-form-item>
        </el-form>
      </div>
    </div>
  </div>
</template>
  <script>
import Cookies from "js-cookie";
export default {
  data() {
    return {
      query: {
        key: this.$route.query.key,
      },
      line_size_list: null,
      scatter_size_list: null,
      mark_list: [
        "o",
        "<",
        ">",
        "^",
        ",",
        ".",
        "v",
        "1",
        "2",
        "3",
        "4",
        "8",
        "s",
        "p",
        "P",
        "*",
        "h",
        "H",
        "+",
        "x",
        " X",
        "d",
        "D",
        "|",
        "_",
      ],
      src: null,
      file: null,
      form: {
        clone_text_size: 9,
        clone_text_color: "#121214", //black

        place_text_size: 10,
        place_text_color: "#F20909", //red

        vertical_line_color: "#4716E7", //purple
        vertical_line_size: 1,
        mean_line_color: "#121214", //black
        mean_line_size: 1,

        clone_scatter_size: 30,
        clone_scatter_color: "#15F209", //green
        clone_scatter_mark: "o",

        place_scatter_size: 50,
        place_scatter_color: "#0D5CEF", //blue
        place_scatter_mark: "^",
      },
    };
  },
  mounted() {
    this.src = this.query.key;
    this.get_scatter_size_list();
    this.get_line_size_list();
    this.$axios({
      method: "get",
      url: "http://127.0.0.1:8000/api/SaveFile/",
      // data: { place:3,clone:1 },
    }).then((res) => {
      // console.log(res.data);
      this.file = res.data;
    });
  },
  methods: {
    download() {
      let base64 = this.src;
      let byteCharacters = atob(
        base64.replace(/^data:image\/(png|jpeg|jpg);base64,/, "")
      );
      let byteNumbers = new Array(byteCharacters.length);
      for (let i = 0; i < byteCharacters.length; i++) {
        byteNumbers[i] = byteCharacters.charCodeAt(i);
      }
      let byteArray = new Uint8Array(byteNumbers);
      let blob = new Blob([byteArray], {
        type: undefined,
      });
      let aLink = document.createElement("a");
      aLink.download = "scatter.png"; //这里写保存时的图片名称
      aLink.href = URL.createObjectURL(blob);
      aLink.click();
    },
    get_scatter_size_list() {
      var arr = new Array(100);
      for (var i = 0; i < 100; i++) {
        arr[i] = (i + 1) * 10;
      }

      this.scatter_size_list = arr;
    },
    get_line_size_list() {
      var arr = new Array(100);
      for (var i = 0; i < 100; i++) {
        arr[i] = i + 1;
      }

      this.line_size_list = arr;
    },
    //上传文件前判断文件类型
    beforeFileUpload(file, fileList) {
      let fileName = file.name;
      let uid = file.uid;
      let pos = fileName.lastIndexOf(".");
      let lastName = fileName.substring(pos, fileName.length);
      // console.log(lastName, lastName.toLowerCase());
      if (
        lastName.toLowerCase() !== ".csv" &&
        lastName.toLowerCase() !== ".xls" &&
        lastName.toLowerCase() !== ".xlsx"
      ) {
        this.$message.error("文件必须为.csv .xls .xlsx 类型");
        this.$refs.uploadFile.clearFiles();
        return false;
      }
    },
    uploadVideo(fileObj) {
      var csrftoken = Cookies.get("csrftoken");
      // console.log(csrftoken);
      let formData = new FormData();
      formData.set("file", fileObj.file);
      // console.log(fileObj.file);
      this.$axios
        .post(
          "http://127.0.0.1:8000/api/upload_for_variety_yield_and_stability/",
          formData,
          {
            headers: {
              "Content-type": "multipart/form-data",
              "X-CSRFTOKEN": csrftoken,
            },
          }
        )
        .then((res) => {
          this.src = res.data.src;
        });
    },
    onSubmit() {
      this.$axios({
        method: "post",
        url: "http://127.0.0.1:8000/api/draw_variety_yield_and_stability/",
        data: { file: this.form },
      }).then((res) => {
        // console.log(res.data.src);
        this.src = res.data.src;
      });
    },
  },
};
</script>
  
  <style lang="less" scoped>
@import "../src/assets/less/variety_yield_and_stability.less";
</style>