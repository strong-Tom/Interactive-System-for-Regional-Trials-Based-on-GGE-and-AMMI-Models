<template>
  <div>
    <div
      class="big"
      style="display: flex; justify-content: space-between; margin-top: 10px"
    >
      <div class="r" style="display: flex">
        <el-button type="primary" @click="training" size="small"
          >提取特征</el-button
        >
      </div>
    </div>
    <p>
      提示:提取特征需要上传一个csv文件，如果格式不符合请在文件管理页面进行格式转换
    </p>
    <el-table
      :data="tableData"
      border
      style="width: 100%"
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

      <el-table-column prop="name" label="文件名"> </el-table-column>

    </el-table>

    <div style="display: flex; justify-content: center; align-items: center">
      <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="index"
        :page-size="pageSize"
        background
        layout="total,prev, pager, next, jumper"
        :total="totalSize"
        next-text="下一页"
        prev-text="上一页"
      ></el-pagination>
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
  created() {

  },
  methods: {
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
        console.log(res.data.vimps_json)
        localStorage.setItem('vimps_json',res.data.vimps_json)

        if (res.data.code == -1) {
          this.$message.error("请上传一个csv文件");
        }
        if (res.data.code == -2) {
          this.$message.error("文件内容有错误，请上传正确的文件内容");
        }
        if (res.data.code == 0) {


          this.query.key = res.data.img_url;
          // console.log(res.data.img_url);
  
            this.$router.push({ path: "/trainingResults", query: this.query });

        }
      });
    },
    //复选框状态改变
    changeFun(val) {
      this.multipleSelection = val;
      if (this.multipleSelection.length > 2) {
        // this.$message.warning('请按规定上传一个数据文件和训练标签,否则无法完成训练');
        // alert("请按规定上传一个数据文件和训练标签,否则无法完成训练");
      }
      // console.log("val is", this.multipleSelection);
    },
    index(index) {
      return index + 1 + (this.currentPage - 1) * this.pageSize;
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
