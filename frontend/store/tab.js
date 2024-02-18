export default {
  state: {
    // 用法:
    // 定义：zyq:'朱义奇无敌',
    // 使用：xx属性='this.$store.state.tab.zyq'

    // 控制是否展开，默认是一个展开的状态,被控制的文件是CommonAaide
    isCollapse: false,
    treeIndex:null,
    treeName:null,
    treeSoil:null,
    treeClimate:null,
    currentMenu: null,

  },
  mutations: {
    collapseMenu(state) {
      state.isCollapse = !state.isCollapse;
    },
  },
};
