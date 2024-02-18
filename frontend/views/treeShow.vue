<template>
  <div style="display: flex">
    <div v-if="this.$store.state.tab.treeName === '柳树'">
      <model-obj
        src="/files/obj/Baby_Head_Basemesh.obj"
        width="750"
        height="600"
      ></model-obj>
    </div>
    <div v-if="this.$store.state.tab.treeName === '红松'">
      <model-obj
        src="/files/obj/LeePerrySmith.obj"
        width="750"
        height="600"
      ></model-obj>
    </div>
    <div v-if="this.$store.state.tab.treeName === '榆树'">
      <model-obj
        src="/files/obj/LibertStatue.obj"
        width="750"
        height="600"
      ></model-obj>
    </div>
    <div v-if="this.$store.state.tab.treeName === '云杉'">
      <model-obj
        src="/files/obj/batman.obj"
        width="750"
        height="600"
      ></model-obj>
    </div>
    <div class="table">
      <el-descriptions title="树木信息">
        <el-descriptions-item label="树木种类">{{
          this.$store.state.tab.treeName
        }}</el-descriptions-item>
        <el-descriptions-item label="土壤">{{
          this.$store.state.tab.treeSoil
        }}</el-descriptions-item>
        <el-descriptions-item label="气候">{{
          this.$store.state.tab.treeClimate
        }}</el-descriptions-item>
      </el-descriptions>
    </div>
  </div>
</template>
<script>
import { ModelObj } from "vue-3d-model";
export default {
  components: { ModelObj },
  methods: {},
};
</script>
<style lang="less" scoped>
.table {
  margin-left: 20px;
}
</style>
