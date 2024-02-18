<template>
  <div class="main">
    <div class="crumbs">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item
          ><i class="el-icon-edit"></i> Change Password</el-breadcrumb-item
        >
      </el-breadcrumb>
    </div>
    <div class="userContent">
      <el-form ref="ruleForm" :model="form" :rules="rules" label-width="280px">
        <el-form-item prop="pass" label="Password">
          <el-input
            v-model="form.pass"
            type="password"
            placeholder="Please input a password"
          ></el-input>
        </el-form-item>
        <el-form-item prop="checkPass" label="Confirm Password">
          <el-input
            v-model="form.checkPass"
            type="password"
            placeholder="Please enter the password again"
          ></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmit('ruleForm')">Confirm</el-button>
          <el-button @click="onCancle()">Cancel</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    var validatePass = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("Please input a password"));
      } else {
        if (this.form.checkPass !== "") {
          this.$refs.ruleForm.validateField("checkPass");
        }
        callback();
      }
    };
    var validatePass2 = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("Please enter the password again"));
      } else if (value !== this.form.pass) {
        callback(new Error("The passwords entered twice are inconsistent"));
      } else {
        callback();
      }
    };
    return {
      form: {
        pass: "",
        checkPass: "",
      },
      rules: {
        pass: [{ validator: validatePass, trigger: "blur" }],
        checkPass: [{ validator: validatePass2, trigger: "blur" }],
      },
    };
  },
  methods: {
    onSubmit(ruleForm) {
      const self = this;
      let formData = {
        email:sessionStorage.getItem("ms_useremail"),
        pass: self.form.pass,
        checkPass: self.form.checkPass,
      };
      self.$refs.ruleForm.validate((valid) => {
        if (valid) {
          axios({
            method: "post",
            url: "http://127.0.0.1:8000/api/modifyPassword/",
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
                message: "Modification failed. The passwords entered twice are inconsistent",
                type: "error",
              });
        }
      });
    },
    onCancle() {
      this.$router.push("/userCenter");
    },
  },
};
</script>

<style scoped>
.el-icon-edit {
  margin-top: 20px;
  font-size: 30px;
}
.userContent {
  width: 400px;
  margin: 80px auto;
}
.el-form-item{
  width:40vw;
}
</style>
