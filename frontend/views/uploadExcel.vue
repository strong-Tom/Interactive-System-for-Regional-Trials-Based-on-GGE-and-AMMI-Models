<template>
  <div class="main">
    <!-- 上面一行被隐藏的按钮 -->
    <!-- <div
      class="big"
      style="display: flex; justify-content: space-between; margin-top: 10px"
    >
      <div class="l">
        <el-upload
          style="margin-top: 10px; margin-bottom: 10px"
          ref="uploadFile"
          class="upload-demo"
          :before-upload="beforeFileUpload"
          :on-success="onUploadSuccess"
          :http-request="uploadVideo"
          multiple
          accept=".xlsx, .xls,.csv,.npy,.txt"
          :show-file-list="true"
        >
          <el-button size="small" type="primary">点击上传</el-button> 
        </el-upload>
      </div>
      <div class="r" style="display: flex">
        <el-button type="primary" @click="batch_deletion" size="small"
          >批量删除</el-button
        > 
        <el-button type="primary" @click="excel_to_csv" size="small"
          >excel转csv</el-button
        >
        <el-button type="primary" @click="excel_to_npy" size="small"
          >excel转npy</el-button
        > 
        <el-button type="primary" @click="training" size="small"
          >开始训练</el-button
        >
      </div>
    </div> -->
    <div class="tip">
      <strong
        >Here are some sample data, and you can view the effect directly or download them.Please select the data corresponding to the corresponding button from the right panel. Click "preview Variety Yield and Stability data" or "preview
        Which won Where data" when gge data is checked, click "preview ammi"
        when ammi data is checked, and click "preview_scatter" when scatter plot
        data is checked.</strong
      >
    </div>
    <div class="table">
      <el-table
        :row-style="{ height: '80px' }"
        :cell-style="{ padding: '0px' }"
        :data="tableData"
        border
        style="width: 42%"
        ref="multipleTable"
        @selection-change="changeFun"
        :row-key="getRowKeys"
      >
        <el-table-column
          type="selection"
          width="55"
          @selection-change="changeFun"
          :reserve-selection="true"
        >
        </el-table-column>
       <!-- <el-table-column type="index" :index="index"> </el-table-column>  -->
        <el-table-column prop="name" label="file name" width="300px;">
        </el-table-column>
        <!-- <el-table-column prop="file_url" label="url" width="780">
      </el-table-column> -->
      <!-- <el-table-column prop="create_time" label="upload time" width="180">
      </el-table-column>  -->
        <el-table-column label="menu" width="210">
          <template slot-scope="scope">
            <el-button
              type="danger"
              size="medium"
              @click="download(scope.$index, scope.row)"
              >download data</el-button
            >
          </template>
        </el-table-column>
      </el-table>
    </div>
    <!-- 被隐藏的分页栏 -->
    <div style="display: flex; justify-content: center; align-items: center">
      <!-- <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="index"
        :page-size="pageSize"
        background
        layout="total,prev, pager, next, jumper"
        :total="totalSize"
        next-text="下一页"
        prev-text="上一页"
      ></el-pagination> -->
    </div>
    <br />
    <div class="button_group">
      <el-button type="primary" size="default" @click="preview_ammi"
        >preview AMMI data</el-button
      >
      <el-button type="primary" size="default" @click="preview_stab"
        >preview Variety Yield and Stability data</el-button
      >
      <el-button type="primary" size="default" @click="preview_where"
        >preview Which won Where data</el-button
      >
      <el-button type="primary" size="default" @click="preview_scatter"
        >preview scatter data</el-button
      >
    </div>
  </div>
</template>
<script>
import axios from "axios";
import Cookies from "js-cookie";
export default {
  components: {
    // pdfjs
    // htmlpdf,
    // 'iframe-pdf':IframePdf,
    // baseWord
    // baseExcel,
  },
  data() {
    return {
      baseUrl: "http://127.0.0.1:8000/api/SaveFile/",
      tableData: null,
      query: {
        key: "",
        vimps_dict: "",
      },
      data: null,
      isdata: null,
      work: null,
      // hotlist: [], //2 热门
      pageSize: 10,
      totalSize: null,
      index: 1,
      currentPage: 1,
      tableData: [], //el-table  绑定的数据
      tableDataALL: [], //所有返回的数据  处理后赋值到tableData
      multipleSelection: null,
      file: {},
      src: null,
      query: {
        key: "",
      },
    };
  },
  mounted() {
    //在这发起后端请求，拿回数据
    axios.get("http://127.0.0.1:8000/api/SaveFile/").then((res) => {
      this.tableDataALL = res.data;
      this.getList();
    });
  },
  created() {},
  methods: {
    preview_scatter() {
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/api/select_for_scatter/",
        data: this.multipleSelection,
      }).then((res) => {
        if (res.data.code == -1) {
          this.$message.error("please choose right data");
        } else {
          // console.log(res.data);
          localStorage.setItem("data_list", JSON.stringify(res.data.data_list));
          localStorage.setItem(
            "label_list",
            JSON.stringify(res.data.label_list)
          );
          localStorage.setItem(
            "place_list",
            JSON.stringify(res.data.place_list)
          );
          localStorage.setItem(
            "clone_list",
            JSON.stringify(res.data.clone_list)
          );
          localStorage.setItem(
            "count_place",
            JSON.stringify(res.data.count_place)
          );
          localStorage.setItem(
            "color_list",
            JSON.stringify(res.data.color_list)
          );
          this.$router.push({ path: "/scatter", query: this.query });
        }
      });
    },
    preview_ammi() {
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/api/select_for_ammi/",
        data: this.multipleSelection,
      }).then((res) => {
        if (res.data.code == -1) {
          this.$message.error("please choose right data");
        } else {
          this.query.key = res.data.src;
          this.$router.push({ path: "/AMMI", query: this.query });
        }
      });
    },
    preview_stab() {
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/api/select_for_variety_yield_and_stability/",
        data: this.multipleSelection,
      }).then((res) => {
        if (res.data.code == -1) {
          this.$message.error("please choose right data");
        } else {
          this.query.key = res.data.src;
          this.$router.push({
            path: "/variety_yield_and_stability",
            query: this.query,
          });
        }
      });
    },
    preview_where() {
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/api/select_for_which_won_where/",
        data: this.multipleSelection,
      }).then((res) => {
        if (res.data.code == -1) {
          this.$message.error("please choose right data");
        } else {
          this.query.key = res.data.src;
          this.$router.push({ path: "/which_won_where", query: this.query });
        }
      });
    },
    download(index, row) {
      window.open(row.file_url, "_blank");
    },
    batch_deletion() {
      this.$confirm("此操作将删除该文件, 是否继续?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      }).then(() => {
        axios({
          method: "post",
          url: "http://127.0.0.1:8000/api/batch_deletion/",
          data: this.multipleSelection,
        }).then((res) => {
          console.log(res.data.code);
          if (res.data.code == 0) {
            this.$message.success("删除成功");
            // 此时已经删除了服务器中的数据，如果此时数据库中有两条索引，剩下一条打开会报错
            // 因此要将索引对应的名字的文件都删除
            axios.delete("http://127.0.0.1:8000/api/SaveFile/").then(() => {
              this.getAll();
            });
          }
        });
      });
    },
    excel_to_csv() {
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/api/excel_to_csv/",
        data: this.multipleSelection,
      }).then((res) => {
        console.log(res.data.code);
        if (res.data.code == -1) {
          this.$message.error("请选择excel文件");
        }
        if (res.data.code == 0) {
          this.$message.success("转换成功");
        }
        if (res.data.code == -2) {
          this.$message.warning("此文件列表中已存在");
        }
      });
    },
    excel_to_npy() {
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/api/excel_to_npy/",
        data: this.multipleSelection,
      }).then((res) => {
        console.log(res.data.code);
        if (res.data.code == -1) {
          this.$message.error("请选择excel文件");
        }
        if (res.data.code == 0) {
          this.$message.success("转换成功");
        }
        if (res.data.code == -2) {
          this.$message.warning("此文件列表中已存在");
        }
      });
    },
    getRowKeys(row) {
      // console.log(row.id);
      return row.id;
    },
    training() {
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/api/extract_feature/",
        data: this.multipleSelection,
      }).then((res) => {
        console.log(res.data.code, res.data);
        if (res.data.code == -1) {
          this.$message.error("请上传一个csv文件");
        }
        if (res.data.code == -2) {
          this.$message.error("文件内容有错误，请上传正确的文件内容");
        }
        if (res.data.code == 0) {
          // 调用后端保存图片到数据库的api
          axios.get("http://127.0.0.1:8000/api/saveLineChart/");

          this.query.key = res.data.img_url;
          this.query.vimps_dict = res.data.vimps_dict;
          this.$router.push({ path: "/trainingResults", query: this.query });
        }
      });
    },
    //复选框状态改变
    changeFun(val) {
      // 限制多选
      if (val.length > 1) {
        this.$refs.multipleTable.clearSelection();
        this.$refs.multipleTable.toggleRowSelection(val.pop());
      } else {
        this.multipleSelection = val;

        // console.log(this.multipleSelection);
      }
    },
    index(index) {
      return index + 1 + (this.currentPage - 1) * this.pageSize;
    },
    //上传文件前判断文件类型
    beforeFileUpload(file, fileList) {
      let fileName = file.name;
      let uid = file.uid;
      let pos = fileName.lastIndexOf(".");
      let lastName = fileName.substring(pos, fileName.length);
      console.log(lastName, lastName.toLowerCase());
      if (
        lastName.toLowerCase() !== ".npy" &&
        lastName.toLowerCase() !== ".csv" &&
        lastName.toLowerCase() !== ".xls" &&
        lastName.toLowerCase() !== ".xlsx" &&
        lastName.toLowerCase() !== ".txt"
      ) {
        this.$message.error("文件必须为.csv .npy .xls .xlsx .txt类型");
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
      axios
        .post("http://127.0.0.1:8000/api/uploadExcel/", formData, {
          headers: {
            "Content-type": "multipart/form-data",
            "X-CSRFTOKEN": csrftoken,
          },
        })
        .then((res) => {
          if (res.data.code == 0) {
            this.$message.success("上传成功");
          }
          if (res.data.code == -2) {
            this.$message.error("上传失败，此文件已存在");
          }
        });
    },
    handleClear() {
      this.$router.push("/uploadVideo");
    },
    handleSizeChange(val) {
      // console.log(`每页 ${val} 条`);
      this.pageSize = val;
      this.getList();
    },
    handleCurrentChange(val) {
      // console.log(`当前页: ${val}`);
      this.index = val;
      this.getList();
    },
    getList() {
      this.tableData = this.tableDataALL.filter(
        (item, index) =>
          index < this.index * this.pageSize &&
          index >= this.pageSize * (this.index - 1)
      );
      this.totalSize = this.tableDataALL.length;
    },
  },
};
</script>
<style lang="less" scoped>
@import "../src/assets/less/uploadExcel.less";
</style>