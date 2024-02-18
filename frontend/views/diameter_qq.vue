<template>
    <div style="display:flex; align-items: center; justify-content: center;">
        <el-image :src="src" :fit="fit" class="image" v-if="src != null">

      </el-image>
    </div>
</template>

<script>
export default {
    name: 'FrontendDiameterDq',

    data() {
        return {
            src:null,
        };
    },

    mounted() {
        console.log(555);
        this.$axios({
        method: "get",
        url: "http://127.0.0.1:8000/api/draw_box_plot_qq/",
      }).then((res) => {
        console.log(res.data);
        console.log(res.data.src);
        this.src = res.data.src;
      });
    },

    methods: {
        
    },
};
</script>

<style lang="less" scoped>

</style>