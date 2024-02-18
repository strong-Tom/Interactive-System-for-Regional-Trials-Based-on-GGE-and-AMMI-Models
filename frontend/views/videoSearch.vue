<template>
  <div>
    <div
      class="big"
      style="display: flex; justify-content: space-between; margin-top: 10px"
    >
      <div class="l">
        <el-upload
          class="upload-demo"
          :before-upload="onBeforeUpload"
          :on-success="onUploadSuccess"
          action="http://127.0.0.1:8000/api/evaluatefileupload/"
          multiple
        >
          <el-button size="small" type="primary">点击上传</el-button>
        </el-upload>
      </div>
      <div class="r" style="display: flex">
        <el-input
          v-model="query.key"
          placeholder="请输入关键字"
          @input="search"
          clearable
          @clear="handleClear"
        ></el-input>
        <el-button type="primary" @click="search">搜索</el-button>
      </div>
    </div>
    <div class="row">
      <div
        v-for="video in tableData"
        :key="video.id"
        class="col-6 col-md-3 col-lg-3"
      >
        <router-link :to="{ path: '/videoInfo', query: { id: video.id } }">
          <b-card
            :id="video.id"
            title=""
            img-src="https://img0.baidu.com/it/u=321763348,3350526900&fm=253&fmt=auto&app=138&f=PNG?w=888&h=500"
            img-alt="Image"
            img-top
            tag="article"
            style="max-width: 20rem"
            class="m-2"
          >
            <b-card-text>
              {{ video.name }}
            </b-card-text>
            <b-card-text style="color: red">
              <!-- {{course.price !=0 ? '￥'+course.price : '免费'}} -->
            </b-card-text>
            <!--        <div slot="footer"><small class="text-muted"></small></div>-->
          </b-card>
        </router-link>
      </div>
    </div>
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
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      query: {
        key: this.$route.query.key,
      },
      data: null,
      isdata: null,
      work: null,
      // hotlist: [], //2 热门
      pageSize: 12,
      totalSize: null,
      index: 1,
      tableData: [], //el-table  绑定的数据
      tableDataALL: [], //所有返回的数据  处理后赋值到tableData
    };
  },
  created() {},
  mounted() {
    axios
      .get("http://127.0.0.1:8000/api/videoSearch/", {
        // work是搜索框中绑定的值,发送给后端的参数名为work
        params: { work: this.query.key },
      })
      .then((res) => {
        this.tableDataALL = res.data;
        this.getList();
      });
  },
  methods: {
    // 搜索
    search(key) {
      axios
        .get("http://127.0.0.1:8000/api/videoSearch/", {
          params: { work: this.query.key },
        })
        .then((res) => {
          this.tableDataALL = res.data;
          this.getList();
        });
      if (key !== "") {
        this.$router.push({ path: "/videoSearch", query: this.query });
        this.reload();
      } else {
        this.$router.push("/uploadVideo");
      }
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
    // 分页,获取符合index和pagesize的数据
    getList() {
      this.tableData = this.tableDataALL.filter(
        (item, index) =>
          index < this.index * this.pageSize &&
          index >= this.pageSize * (this.index - 1)
      );
      this.totalSize = this.tableDataALL.length;
    },
    onBeforeUpload(file) {
      // 上传文件之前，进行文件大小、类型的判断
      console.log(file);
    },

    onUploadSuccess(res, file) {
      // 上传文件成功之后
      console.log(res);
      console.log(file);
    },
  },
};
</script>
