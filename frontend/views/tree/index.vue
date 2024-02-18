<template>
  <div>
    <div class="c">
      <div class="l">
        <el-button type="success" plain @click="handleAddClick">增加</el-button>
        <el-button type="primary" plain @click="exportExcle"
          >文件导出</el-button
        >
      </div>
      <div class="r">
        <el-input
          placeholder="请输入搜索内容"
          v-model="inputVal"
          @keyup.enter.native="Search_table"
          clearable
        >
        </el-input>
        <el-button type="search" @click="Search_table">搜索</el-button>
      </div>
    </div>
    <br />

    <el-table :data="trees" border style="width: 100%">
      <el-table-column type="index" :index="index" label="索引"> </el-table-column>
      <el-table-column prop="place" label="地点" width="180"> </el-table-column>
      <el-table-column prop="block" label="区块" width="180"> </el-table-column>
      <el-table-column prop="clone" label="无性系"> </el-table-column>
      <el-table-column prop="rep" label="重复"> </el-table-column>
      <el-table-column prop="height" label="苗高"> </el-table-column>
      <el-table-column prop="diameter" label="地径"> </el-table-column>

      <el-table-column label="操作" width="210">
        <template slot-scope="scope">
          <el-button
            type="primary"
            @click="handleEditClick(scope.$index, scope.row)"
            size="mini"
            >编辑</el-button
          >
          <el-button
            type="danger"
            size="mini"
            @click="handleDelClick(scope.$index, scope.row)"
            >删除</el-button
          >
          <!-- <el-button
            type="danger"
            size="mini"
            @click="detail(scope.$index, scope.row)"
            >详情</el-button
          > -->
        </template>
      </el-table-column>
    </el-table>
    <div
      style="display: flex; justify-content: center; align-items: center"
      v-if="length <= pageSize"
    >
      <el-pagination
        background
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="currentPage"
        :page-sizes="[10, 20, 30, 50]"
        :page-size="pageSize"
        layout="total, sizes, prev, pager, next, jumper"
        :total="total"
      >
      </el-pagination>
    </div>
    <!-- 修改树木 -->
    <el-dialog
      title="修改树木"
      :visible.sync="editBox"
      width="50%"
      :before-close="handleClose"
    >
      <el-form ref="form" label-width="100px" v-model="tree">
        <el-form-item label="地点">
          <el-input
            placeholder="请输入地点"
            maxlength="50"
            v-model="tree.place"
          ></el-input>
        </el-form-item>
        <el-form-item label="区组">
          <el-input
            placeholder="请输入区组"
            maxlength="50"
            v-model="tree.block"
          ></el-input>
        </el-form-item>
        <el-form-item label="无性系">
          <el-input
            placeholder="请输入无性系"
            maxlength="50"
            v-model="tree.clone"
          ></el-input>
        </el-form-item>
        <el-form-item label="重复">
          <el-input
            placeholder="请输入重复"
            maxlength="50"
            v-model="tree.rep"
          ></el-input>
        </el-form-item>
        <el-form-item label="苗高">
          <el-input
            placeholder="请输入苗高"
            maxlength="50"
            v-model="tree.height"
          ></el-input>
        </el-form-item>
        <el-form-item label="地径">
          <el-input
            placeholder="请输入地径"
            maxlength="50"
            v-model="tree.diameter"
          ></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button type="primary" @click="handleEditUser">确 定</el-button>
      </span>
    </el-dialog>
    <!-- 添加树种 -->
    <el-dialog
      title="添加树种"
      :visible.sync="addBox"
      width="50%"
      :before-close="handleClose"
    >
      <el-form ref="form" label-width="100px" v-model="addUserData">
        <el-form-item label="地点">
          <el-input
            placeholder="请输入地点"
            maxlength="50"
            v-model="addTreeData.place"
          ></el-input>
        </el-form-item>
        <el-form-item label="区组">
          <el-input
            placeholder="请输入区组"
            maxlength="50"
            v-model="addTreeData.block"
          ></el-input>
        </el-form-item>
        <el-form-item label="无性系">
          <el-input
            placeholder="请输入无性系"
            maxlength="50"
            v-model="addTreeData.clone"
          ></el-input>
        </el-form-item>
        <el-form-item label="重复">
          <el-input
            placeholder="请输入重复"
            maxlength="50"
            v-model="addTreeData.rep"
          ></el-input>
        </el-form-item>
        <el-form-item label="苗高">
          <el-input
            placeholder="请输入苗高"
            maxlength="50"
            v-model="addTreeData.height"
          ></el-input>
        </el-form-item>
        <el-form-item label="地径">
          <el-input
            placeholder="请输入地径"
            maxlength="50"
            v-model="addTreeData.diameter"
          ></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button type="primary" @click="handleAddUser">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
import * as XLSX from "xlsx"; // 数据导出导入所需要的依赖
import axios from "axios";
export default {
  name: "TableData",
  data() {
    return {
      count: 0,
      firstId: 0,
      length: 0,
      pageSize: 10,
      currentPage: 1,
      total: null,
      baseUrl: "http://127.0.0.1:8000/api/poplar/",
      trees: null,
      treeAll: null,
      addBox: false,
      editBox: false,
      editIndex: "",
      tree: {},
      inputVal: "",
      addTreeData: {
        place: "",
        block: "",
        clone: "",
        rep: "",
        height: "",
        diameter: "",

        // tableData: [],
      },
      showTable: [],
    };
  },

  methods: {
    exportExcle() {
      // axios.get("http://127.0.0.1:8000/api/tree1/").then((res) => {
      //   this.treeAll = res.data;
      // });
      var data1 = this.treeAll;
      //1. 新建一个工作簿
      let workbook = XLSX.utils.book_new();
      //2. 生成一个工作表，
      //2.1 aoa_to_sheet 把数组转换为工作表
      // let sheet1 = XLSX.utils.aoa_to_sheet(data1);
      //2.2 把json对象转成工作表
      let sheet1 = XLSX.utils.json_to_sheet(data1);
      //3.在工作簿中添加工作表
      XLSX.utils.book_append_sheet(workbook, sheet1, "sheetName1"); //工作簿名称
      // XLSX.utils.book_append_sheet(workbook, sheet2, "sheetName2"); //工作簿名称
      // XLSX.utils.sheet_add_json(sheet1,data2);//把已存在的sheet中数据替换成json数据
      //4.输出工作表,由文件名决定的输出格式
      XLSX.writeFile(workbook, "workBook1.xlsx"); // 保存的文件名
    },
    // detail(index, row) {
    //   var index1 = index + (this.currentPage - 1) * this.pageSize;
    //   this.$store.state.tab.treeIndex = index1;
    //   this.$store.state.tab.treeName = row.name;
    //   this.$store.state.tab.treeSoil = row.soil;
    //   this.$store.state.tab.treeClimate = row.climate;
    //   // alert(index1)
    //   this.$router.push("treeShow");
    // },
    index(index) {
      return index + 1 + (this.currentPage - 1) * this.pageSize;
    },
    handleSizeChange(val) {
      axios
        .get(this.baseUrl + "?size=" + val + "&page=" + this.currentPage)
        .then((res) => {
          this.trees = res.data.results;
          this.pageSize = val;
          // alert(this.baseUrl+'?size='+val+'&page='+this.currentPage)
        });
    },
    handleCurrentChange(val) {
      axios
        .get(this.baseUrl + "?size=" + this.pageSize + "&page=" + val)
        .then((res) => {
          this.trees = res.data.results;
          this.currentPage = val;
          // alert(this.baseUrl+'?size='+this.pageSize+'&page='+val)
        });
    },
    //搜索框强制刷新@input='change($event)'
    // change(e) {
    //   this.$forceUpdate();
    // },
    //编辑按钮
    handleEditClick(index, row) {
      this.editBox = true;
      // this.user = row;
      this.tree = row;
      this.editIndex = index;
      this.$message(index);
    },

    // eslint-disable-next-line no-unused-vars
    handleDelClick(index, row) {
      this.tree = row;
      this.$confirm("此操作将删除该数据, 是否继续?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      }).then(() => {
        // this.trees.splice(index, 1);
        axios.delete(this.tree.url).then(() => {
          this.getAll();
        });
        this.$message({
          showClose: true,
          message: "删除成功",
          type: "success",
        });
      });
    },
    handleClose(done) {
      done();
    },
    //修改对话框确定按钮
    handleEditUser() {
      // this.trees.splice(this.editIndex, 1, this.tree);

      axios
        .put(this.tree.url, {
          place: this.tree.place,
          block: this.tree.block,
          clone: this.tree.clone,
          rep: this.tree.rep,
          height: this.tree.height,
          diameter: this.tree.diameter,
        })
        .then(() => {
          this.getAll();
          this.$message({
            showClose: true,
            message: "修改成功",
            type: "success",
          });
          this.editBox = false;
        });
    },
    //增加按钮
    handleAddClick() {
      this.addBox = true;
    },
    //添加树木对话框的确认按钮
    handleAddUser() {
      axios
        .post(this.baseUrl, {
          place: this.addTreeData.place,
          block: this.addTreeData.block,
          clone: this.addTreeData.clone,
          rep: this.addTreeData.rep,
          height: this.addTreeData.height,
          diameter: this.addTreeData.diameter,
        })
        .then(() => {
          this.$message({
            showClose: true,
            message: "添加成功",
            type: "success",
          });
          this.addBox = false;
        });
    },
    getAll() {
      axios.get(this.baseUrl).then((res) => {
        this.trees = res.data.results;
      });
    },
    Search_table() {
      if (this.inputVal) {
        const Search_List = [];
        let res1 = this.inputVal;
        const res = res1.replace(/\s/gi, "");
        let searchArr = this.treeAll;
        searchArr.forEach((e) => {
          let place = e.place;
          let block = e.block;
          let clone = e.clone;
          let rep = e.rep;
          let height = e.height;
          let diameter = e.diameter;
          if (block.includes(res)) {
            if (Search_List.indexOf(e) == "-1") {
              Search_List.push(e);
              axios.post("http://127.0.0.1:8000/api/treeTmp/", {
                place: e.place,
                block: e.block,
                clone: e.clone,
                rep: e.rep,
                height: e.height,
                diameter: e.diameter,
              });
            }
          }
          if (place.includes(res)) {
            if (Search_List.indexOf(e) == "-1") {
              Search_List.push(e);
              axios.post("http://127.0.0.1:8000/api/treeTmp/", {
                place: e.place,
                block: e.block,
                clone: e.clone,
                rep: e.rep,
                height: e.height,
                diameter: e.diameter,
              });
            }
          }
          if (clone.includes(res)) {
            if (Search_List.indexOf(e) == "-1") {
              Search_List.push(e);
              axios.post("http://127.0.0.1:8000/api/treeTmp/", {
                place: e.place,
                block: e.block,
                clone: e.clone,
                rep: e.rep,
                height: e.height,
                diameter: e.diameter,
              });
            }
          }
          if (rep.includes(res)) {
            if (Search_List.indexOf(e) == "-1") {
              Search_List.push(e);
              axios.post("http://127.0.0.1:8000/api/treeTmp/", {
                place: e.place,
                block: e.block,
                clone: e.clone,
                rep: e.rep,
                height: e.height,
                diameter: e.diameter,
              });
            }
          }
          if (height.includes(res)) {
            if (Search_List.indexOf(e) == "-1") {
              Search_List.push(e);
              axios.post("http://127.0.0.1:8000/api/treeTmp/", {
                place: e.place,
                block: e.block,
                clone: e.clone,
                rep: e.rep,
                height: e.height,
                diameter: e.diameter,
              });
            }
          }
          if (diameter.includes(res)) {
            if (Search_List.indexOf(e) == "-1") {
              Search_List.push(e);
              axios.post("http://127.0.0.1:8000/api/treeTmp/", {
                place: e.place,
                block: e.block,
                clone: e.clone,
                rep: e.rep,
                height: e.height,
                diameter: e.diameter,
              });
            }
          }
        });

        this.trees = Search_List;
        this.length = Search_List.length;
        axios.get("http://127.0.0.1:8000/api/treeTmp/").then((res) => {
          this.firstId = res.data.results[0].id;
          this.count = res.data.count;
          // console.log("count=" + this.count, this.firstId);
        });
      }
    },
  },
  watch: {
    inputVal(item1, item2) {
      if (item1 == "" || item2 == "") {
        this.length = 1;
        // this.trees = this.showTable;
        axios.get(this.baseUrl + "?size=10&page=1").then((res) => {
          this.trees = res.data.results;
        });
      }
    },
  },
  computed: {},
  mounted() {
    //在这发起后端请求，拿回数据
    axios.get(this.baseUrl).then((res) => {
      this.showTable = res.data.results;
      this.trees = res.data.results;
      this.total = res.data.count;
    });
    axios.get("http://127.0.0.1:8000/api/tree1/").then((res) => {
      this.treeAll = res.data;
      // console.log(this.treeAll);
    });
  },
};
</script>

<style lang="less" scoped>
.c {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
  .r {
    display: flex;
  }
}
</style>
