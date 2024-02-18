<template>
  <div>
    <div class="crumbs">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item
          ><i class="el-icon-edit"></i> Modify User</el-breadcrumb-item
        >
      </el-breadcrumb>
    </div>
    <div class="userContent">
      <el-form ref="form" :model="form" :rules="rules" label-width="180px">
        <el-form-item prop="name" label="User Name">
          <el-input v-model="form.username"></el-input>
        </el-form-item>
        <el-form-item prop="email" label="Email">
          <el-input v-model="form.email" disabled></el-input>
        </el-form-item>
        <el-form-item prop="phone" label="Phone">
          <el-input
            v-model="form.phone"
            placeholder="Please enter your mobile number"
          ></el-input>
        </el-form-item>
        <el-form-item prop="sex" label="Sex">
          <el-select
            class="select-sex"
            v-model="form.sex"
            placeholder="Please select gender"
          >
            <el-option label="male" value="man"></el-option>
            <el-option label="female" value="woman"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="updateUserData('form')"
            >Confirm</el-button
          >
          <el-button @click="onCancle()">cancel</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Util from "@/utils/utils";
export default {
  data() {
    var validatePhone = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("Please enter your mobile number"));
      } else if (!Util.phoneReg.test(this.form.phone)) {
        callback(new Error("Please enter the correct mobile number"));
      } else {
        callback();
      }
    };
    return {
      form: {
        username: "",
        email: "",
        phone: "",
        sex: "",
      },
      rules: {
        name: [
          {
            required: true,
            message: "Please enter one user name",
            trigger: "blur",
          },
        ],
        phone: [{ validator: validatePhone, trigger: "blur" }],
        sex: [
          { required: true, message: "Please enter gender", trigger: "blur" },
        ],
      },
    };
  },
  methods: {
    getUserData() {
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/api/login/",
        data: {
          email: sessionStorage.getItem("ms_useremail"),
          password: sessionStorage.getItem("ms_userpassword"),
        },
      }).then((res) => {
        this.form.username = res.data.user[0].username;
        this.form.email = res.data.user[0].email;
        this.form.phone = res.data.user[0].phone;
        this.form.sex = res.data.user[0].sex;
        // console.log(this.form);
      });
    },
    updateUserData(formName) {
      const self = this;
      let formData = {
        email: self.form.email,
        phone: self.form.phone,
        sex: self.form.sex,
        username: self.form.username,
      };
      //   self.$refs[formName].validate((valid) => {
      if (Util.phoneReg.test(this.form.phone)) {
        axios({
          method: "post",
          url: "http://127.0.0.1:8000/api/modifyUser/",
          data: {
            formData,
          },
        }).then((res) => {
          if (res.status === 200) {
            // console.log(res);
            // console.log(res.data);
            this.$message({
              message: "Modification succeeded",
              type: "success",
            });
            this.$router.push("/userCenter");
          }
        });
      } else {
        this.$message({
          message:
            "Modification failed. Please enter the correct mobile number",
          type: "error",
        });
      }
      //   });
    },
    onCancle() {
      this.$router.push("/userCenter");
    },
  },
  //初始化
  mounted() {
    this.getUserData();
  },
};
</script>
<style lang="less" scoped>
.el-icon-edit {
  margin-top: 20px;
  font-size: 30px;
}
.userContent {
  width: 400px;
  margin: 80px auto;
}
.select-sex {
  width: 320px;
}
</style>
