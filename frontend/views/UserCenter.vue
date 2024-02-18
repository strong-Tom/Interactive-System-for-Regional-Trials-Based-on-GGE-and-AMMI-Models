<template>
  <div>
    <div class="crumbs">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item
          ><i class="el-icon-setting"></i>User Center</el-breadcrumb-item
        >
      </el-breadcrumb>
    </div>
    <div class="userContent">
      <el-form ref="form" :model="form" label-width="180px" disabled>
        <el-form-item label="User Name">
          <el-input v-model="form.username"></el-input>
        </el-form-item>
        <el-form-item label="Email">
          <el-input v-model="form.email"></el-input>
        </el-form-item>
        <el-form-item label="Phone">
          <el-input v-model="form.phone"></el-input>
        </el-form-item>
        <el-form-item label="Sex">
          <el-select
            class="select-sex"
            v-model="form.sex"
            placeholder="Please select gender"
          >
            <el-option label="male" value="man"></el-option>
            <el-option label="female" value="woman"></el-option>
          </el-select>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "userCenter",
  data() {
    return {
      form: {
        username: null,
        email: null,
        password: null,
        phone: null,
        sex: null,
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
        this.form.password = res.data.user[0].password;
        this.form.phone = res.data.user[0].phone;
        this.form.sex = res.data.user[0].sex;
        // console.log(this.form);
      });
    },
  },
  mounted() {
    this.getUserData();
  },
};
</script>

<style scoped>
.el-icon-setting {
  margin-top: 20px;
  font-size: 30px;
}
.userContent {
  margin: 80px auto;

  width: 400px;
  /* margin: 0 auto; */
}
.select-sex {
  width: 320px;
}
</style>
