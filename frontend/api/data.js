//接口请求都写在这个类
import axios from "./axios";
export const getMenu = (param) => {
  return axios.request({
    url: "/permission/getMenu",
    method: "post",
    data: param,
  });
};
//箭头函数写法
// export const getData = () => {
    
//     return axios.request({
//     url: "/home/getData",
//     //默认是get
//   });


//原始人写法
  export  function getData() {
      
    
    return axios.request({
    url: "/home/getData",
    //默认是get
  });

};

export function getTrees() {
  return axios.request({
    url: "http://127.0.0.1:8000/api/tree1/",
    method: 'get',
    // data: formData
  })
}

// 连后台接口部分
// 上传 UploadFiles
export function UploadFiles(formData) {
  return request({
    url: '/auditufileinfo/uploadPlanBatchTemplate',
    method: 'post',
    data: formData
  })
}