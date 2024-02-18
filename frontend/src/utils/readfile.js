/* 读取文件 */
// export const readFile = (file) => {
//     return new Promise(resolve => {
//       let reader = new FileReader()
//       reader.readAsBinaryString(file)
//       reader.onload = ev => {
//         resolve(ev.target.result)
//       }
//     })
//   }
  // 上面存在的问题就是这种文件传递给后台，后端也不认识啊。人家是name,我们传过去一个姓名。这个是不可能解析的。如何实现一个可以传递给后台的文件数据呢。
  // 这个马上就可以在组件里面进行将对应的text文本转换了
  // 字段转换
export let character = {
  name: {
      text: "姓名",
      type: String
  },
  sex: {
      text: "性别",
      type: String
  },
  age: {
      text: "年龄",
      type: Number
  },
} 

export function upload(file){
  return new Promise(resolve=>{
      let reader = new FileReader()
      reader.readAsBinaryString(file);
      reader.onload = ev=>{
          resolve(ev.target.result)
      }
  })
}
