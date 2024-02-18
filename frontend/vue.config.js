//此文件解决了报错：
//1 error and 0 warnings potentially fixable with the `--fix` option.
//eslint是语法检查工具，但限制太过于严格,以下代码跳过它
module.exports = {
  assetsDir: "static", // 静态资源打包输出目录 (js, css, img, fonts)，相应的url路径也会改变
  lintOnSave: false,
  devServer: {
    disableHostCheck: true,
  },
};
