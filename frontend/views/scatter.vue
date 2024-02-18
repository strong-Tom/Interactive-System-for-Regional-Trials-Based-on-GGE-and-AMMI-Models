<template>
  <div style="display: flex; justify-content: space-between; margin-top: 10px">
    <!-- 散点图 -->
    <div id="scatter" >
      <span class="title">WorkPlace</span>
      <div class="name" v-if="src == null">scatter</div>
      <el-card class="box-card">
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
        class="image"
        :src="require('../src/assets/images/loadding4.gif')"
        fit="fill"
        :lazy="true"
      ></el-image>
    </div>
    <!-- 右侧工具栏 -->
    <div class="item9">
      <span class="title">tool box</span>
      <!-- 提示 -->
      <div class="tip">
        <strong
          >Function:Used to individually display a certain clone belonging to a
          place</strong
        >
      </div>
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
          accept=".xlsx, .xls,.csv,.npy,.txt"
          :show-file-list="false"
        >
          <el-button size="primary" type="success" 
            >Upload(.xlsx)</el-button
          >
        </el-upload>
        <!-- 下载按钮 -->

        <el-button
          type="warning"
          size="default"
          @click="download"
          
          >Download(.png)</el-button
        >
      </div>
      <!-- 表单 -->
      <div class="form">
        <el-form ref="form" :model="sizeForm" label-width="80px" size="mini">
          <el-form-item label="place">
            <el-select
              v-model="sizeForm.place"
              placeholder="please input place"
            >
              <el-option
                v-for="v in place_list"
                :key="v"
                :label="'place' + v"
                :value="v"
              >
              </el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="clone">
            <el-select
              v-model="sizeForm.clone"
              placeholder="please input clone  "
            >
              <el-option
                v-for="v in clone_list"
                :key="v"
                :label="'clone' + v"
                :value="v"
              >
              </el-option>
            </el-select>
          </el-form-item>
          <el-form-item size="large">
            <el-button type="primary" @click="onSubmit">Confirm</el-button>
          </el-form-item>
        </el-form>
      </div>

      <!-- 颜色选择器 -->
      <div class="include">
        <div
          class="color_picker"
          v-for="(v, i) in label_list"
          :key="v"
          :value="v"
        >
          <el-color-picker
            @change="changeColor"
            v-model="color_list[i]"
          ></el-color-picker>
          <span class="demonstration" style="display: flex">{{ v }}</span>
        </div>
      </div>
    </div>
  </div>
</template>
      <script>
import * as echarts from "echarts";
import Cookies from "js-cookie";
import html2canvas from "html2canvas";
export default {
  props: ["v"],
  data() {
    return {
      query: {
        key: "",
        vimps_dict: "",
      },
      scatter: {},
      color_list: null,
      size: 20,
      color: "#409EFF",
      series: null,
      count_place: null,
      clone_list: null,
      place_list: null,
      data: null,
      isdata: null,
      work: null,
      multipleSelection: null,
      file: {},
      sizeForm: {
        cl_list: null,
        cl_judge: null,
        place: "",
        clone: "",
        delivery: false,
      },
      // height: null,
      // diameter: null,
      data_list: null,
      label_list: null,
      test: null,
    };
  },
  methods: {
    download() {
      var picInfo = this.scatter.getDataURL();
      // console.log(picInfo);
      let base64 = picInfo;
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
    changeColor() {
      this.getSeries();
      this.drawChart();
    },
    getSeries() {
      var serie = [];
      for (var i = 0; i < this.label_list.length; i++) {
        // console.log("zzzzzzzzzzz", this.label_list.length, serie);
        var item = {
          // name: "1",
          name: this.label_list[i],

          data: this.data_list[i], ////////////////////
          type: "scatter",
          symbolSize: function () {
            return 20;
          },
          emphasis: {
            focus: "series",
            label: {
              show: true,
              formatter: function (param) {
                return param.data;
              },
              position: "top",
            },
          },
          itemStyle: {
            shadowBlur: 10,
            // shadowColor: "black",
            shadowOffsetY: 5,
            color: new echarts.graphic.RadialGradient(0.4, 0.3, 1, [
              {
                offset: 0,
                color: this.color_list[i],
              },
              // {
              //   offset: 1,
              //   // color: "rgb(204, 46, 72)",
              //   color: "black",
              // },
            ]),
          },
        };
        serie.push(item);
      }

      this.series = serie;
    },
    //上传文件前判断文件类型
    beforeFileUpload(file, fileList) {
      let fileName = file.name;
      let uid = file.uid;
      let pos = fileName.lastIndexOf(".");
      let lastName = fileName.substring(pos, fileName.length);
      console.log(lastName, lastName.toLowerCase());
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
      console.log(csrftoken);
      let formData = new FormData();
      formData.set("file", fileObj.file);
      // console.log(fileObj.file);
      this.$axios
        .post("http://127.0.0.1:8000/api/upload_for_scatter/", formData, {
          headers: {
            "Content-type": "multipart/form-data",
            "X-CSRFTOKEN": csrftoken,
          },
        })
        .then((res) => {
          this.color_list = res.data.color_list;
          // 将第一次随机生成的颜色列表保存下来发给后端，保证后面多显示一条数据后前面的颜色顺序保持不变
          this.sizeForm.cl_list = this.color_list;
          this.count_place = res.data.count_place;
          this.data_list = res.data.data_list;
          this.label_list = res.data.label_list;
          this.place_list = res.data.place_list;
          this.clone_list = res.data.clone_list;
          // console.log(this.data_list,this.label_list);
          this.getSeries();
          this.drawChart();

          //   console.log("place_list is", this.place_list);
          if (res.data.code == 0) {
            this.$message.success("Upload succeeded");
          }
          if (res.data.code == -2) {
            this.$message.error("上传失败，此文件已存在");
          }
        });
    },
    onSubmit() {
      this.$axios({
        method: "post",
        url: "http://127.0.0.1:8000/api/draw_2d_scatter/",
        data: this.sizeForm,
      }).then((res) => {
        this.data_list = res.data.data_list;
        this.label_list = res.data.label_list;
        this.color_list = res.data.color_add_list;
        this.sizeForm.cl_judge = res.data.color_add_list;
        
        this.getSeries();
        this.drawChart();
        // console.log(this.label_list, this.data_list);
      });
    },
    drawChart() {
      var chartDom = document.getElementById("scatter");
      var scatter = echarts.init(chartDom);
      var option;
      var label = this.label_list;
      option = {
        backgroundColor: new echarts.graphic.RadialGradient(0.3, 0.3, 0.8, [
          {
            offset: 0,
            // color: "#f7f8fa",
            color: "white",
          },
          {
            offset: 1,
            // color: "#cdd0d5",
            color: "white",
          },
        ]),
        title: {
          // text: "scatter for suitable tree in plantation",
          left: "5%",
          top: "3%",
        },
        legend: {
          right: "10%",
          top: "3%",
          // data: ['1', "2", "3","4"], //////////图例
          data: this.label_list, //////////图例
        },
        grid: {
          left: "8%",
          top: "10%",
        },
        xAxis: {
          name: "height(cm)",
          nameLocation: "middle", 
          // padding:[20,20,20,20,20] ,
          nameGap: 30,
          splitLine: {
            lineStyle: {
              type: "dashed",
            },
          },
        },
        yAxis: {
          name: "diameter(mm)",
          nameLocation: "middle", 
          // padding:[0,0,0,0,0] ,
          nameGap: 30,
          splitLine: {
            lineStyle: {
              type: "dashed",
            },
          },
          scale: true,
        },
        series: this.series,
      };

      option && scatter.setOption(option, true);
      this.scatter = echarts.init(document.getElementById("scatter"));
    },
  },
  mounted() {
    this.color_list = JSON.parse(localStorage.getItem("color_list"));
          // 将第一次随机生成的颜色列表保存下来发给后端，保证后面多显示一条数据后前面的颜色顺序保持不变
          this.sizeForm.cl_list = this.color_list;
          this.count_place = JSON.parse(localStorage.getItem("count_place"));
          this.data_list = JSON.parse(localStorage.getItem("data_list"));
          this.label_list = JSON.parse(localStorage.getItem("label_list"));
          this.place_list = JSON.parse(localStorage.getItem("place_list"));
          this.clone_list = JSON.parse(localStorage.getItem("clone_list"));
          // console.log(this.data_list,this.label_list);
          this.getSeries();
          this.drawChart();
          localStorage.removeItem("color_list")
          localStorage.removeItem("count_place")
          localStorage.removeItem("data_list")
          localStorage.removeItem("label_list")
          localStorage.removeItem("place_list")
          localStorage.removeItem("clone_list")
  },
  created() {},
};
</script>
<style lang="less" scoped>
@import "../src/assets/less/scatter.less";
</style>