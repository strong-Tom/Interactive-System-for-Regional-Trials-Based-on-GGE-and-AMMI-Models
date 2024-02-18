<template>
  <div class="login-register">
    <div class="contain">
      <div class="big-box" :class="{ active: isLogin }">
        <div class="big-contain" v-if="isLogin">
          <div class="btitle">Account Login</div>
          <div class="bform">
            <!-- <input type="email" placeholder="邮箱" v-model="form.useremail" />
            <span class="errTips" v-if="emailError">* 邮箱填写错误 *</span>
            <input type="password" placeholder="密码" v-model="form.userpwd" />
            <span class="errTips" v-if="emailError">* 密码填写错误 *</span> -->
            <el-form
              ref="form"
              :model="form"
              status-icon
              :rules="rules"
              label-width="80px"
            >
              <el-form-item prop="useremail" label="Email">
                <el-input
                  v-model="form.useremail"
                  placeholder="Please enter your email address"
                ></el-input>
              </el-form-item>
              <el-form-item prop="userpwd" label="Password">
                <el-input
                  v-model="form.userpwd"
                  type="password"
                  placeholder="Please input a password"
                ></el-input>
              </el-form-item>
            </el-form>
          </div>
          <button class="bbutton" @click="login">Sign in</button>
        </div>
        <div class="big-contain" v-else>
          <div class="btitle" style="margin-bottom: 35px">Create Account</div>
          <div class="bform" style="margin-bottom: 20px">
            <el-form
              ref="form"
              :model="form"
              status-icon
              :rules="rules"
              label-width="120px"
            >
              <el-form-item prop="username" label="User Name" >
                <el-input
                  v-model="form.username"
                  placeholder="Please enter the user name"
                ></el-input>
              </el-form-item>
              <el-form-item prop="useremail" label="Email">
                <el-input
                  v-model="form.useremail"
                  placeholder="Please enter your email address"
                ></el-input>
              </el-form-item>
              <el-form-item prop="userpwd" label="password">
                <el-input
                  v-model="form.userpwd"
                  type="password"
                  placeholder="Please input a password"
                ></el-input>
              </el-form-item>
            </el-form>
          </div>
          <button class="bbutton" @click="register">Register</button>
        </div>
      </div>
      <div class="small-box" :class="{ active: isLogin }">
        <div class="small-contain" v-if="isLogin">
          <div class="stitle">Hello, friend!</div>
          <p class="scontent">Start to register and travel with us</p>
          <button class="sbutton" @click="changeType">Register</button>
        </div>
        <div class="small-contain" v-else>
          <div class="stitle">welcome back!</div>
          <p class="scontent">Please log in to your account to keep in touch with us</p>
          <button class="sbutton" @click="changeType">Sign in</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Util from "../src/utils/utils";
export default {
  name: "login-register",
  data() {
    var validateEmail = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("Please enter your email address"));
      } else if (!Util.emailReg.test(this.form.useremail)) {
        callback(new Error("Please enter the correct email"));
      } else {
        callback();
      }
    };
    var validatePass = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("Please input a password"));
      } else {
        if (this.form.userpwd !== "") {
          this.$refs.form.validateField("checkPass");
        }
        callback();
      }
    };
    return {
      isLogin: true,
      emailError: false,
      passwordError: false,
      existed: false,
      form: {
        username: "",
        useremail: "",
        userpwd: "",
      },
      rules: {
        username: [
          {
            required: true,
            message: "enter one user name",
            trigger: "blur",
          },
        ],
        userpwd: [{ validator: validatePass, trigger: "blur" }],
        useremail: [{ validator: validateEmail, trigger: "blur" }],
      },
    };
  },
  methods: {
    changeType() {
      this.isLogin = !this.isLogin;
      this.form.username = "";
      this.form.useremail = "";
      this.form.userpwd = "";
    },
    login() {
      const self = this;
      if (self.form.useremail != "" && self.form.userpwd != "") {
        // axios
        //   .post("http://127.0.0.1:8000/api/login/", {
        //     email: self.form.useremail,
        //     password: self.form.userpwd,
        //   })
        if (Util.emailReg.test(this.form.useremail)) {
          axios({
            method: "post",
            url: "http://127.0.0.1:8000/api/login/",
            data: {
              email: self.form.useremail,
              password: self.form.userpwd,
            },
          })
            .then((res) => {
              // console.log(res);
              // console.log(res.data);

              switch (res.data.code) {
                case 0:
                  // alert("登陆成功！");
                  let flag = true;
                  this.$store.commit("login", flag);

                  this.$router.push("/home");
                  this.$message({
                    message: "Login succeeded",
                    type: "success",
                  });
                  sessionStorage.setItem("ms_useremail", this.form.useremail);
                  sessionStorage.setItem("ms_userpassword", this.form.userpwd);
                  // console.log(sessionStorage.getItem('ms_useremail'));
                  sessionStorage.setItem("ms_user", JSON.stringify(this.form));
                  // console.log(JSON.stringify(this.form));
                  break;
                case -1:
                  this.$message({
                    message: "Incorrect email or password input",
                    type: "error",
                  });
                  break;
              }
            })
            .catch((err) => {
              console.log(err);
            });
        } else {
          this.$message({
            message: "Login failed, please enter the correct email",
            type: "error",
          });
        }
      } else {
        alert("Fill in cannot be blank!");
      }
    },
    register() {
      const self = this;
      if (
        self.form.username != "" &&
        self.form.useremail != "" &&
        self.form.userpwd != ""
      ) {
        if (Util.emailReg.test(this.form.useremail)) {
          axios({
            method: "post",
            url: "http://127.0.0.1:8000/api/register/",
            data: {
              username: self.form.username,
              email: self.form.useremail,
              password: self.form.userpwd,
            },
          })
            .then((res) => {
              switch (res.data) {
                case 0:
                  this.$message({
                    message: "login was successful",
                    type: "success",
                  });
                  this.$router.push("/");
                  this.changeType();
                  break;
                case -1:
                  this.$message({
                    message: "Registration failed. The mailbox has been used",
                    type: "error",
                  });
                  this.existed = true;
                  break;
              }
            })
            .catch((err) => {
              console.log(err);
            });
        } else {
          this.$message({
            message: "Registration failed, please enter correct email",
            type: "error",
          });
        }
      } else {
        alert("Fill in cannot be blank!");
      }
    },
  },
};
</script>

<style scoped="scoped">
.login-register {
  width: 100vw;
  height: 100vh;
  box-sizing: border-box;
  /* background-image: url(../src/assets/images/6.gif); */
}
.contain {
  width: 60%;
  height: 60%;
  position: relative;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: #fff;
  border-radius: 20px;
  box-shadow: 0 0 3px #f0f0f0, 0 0 6px #f0f0f0;
}
.big-box {
  width: 70%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 30%;
  transform: translateX(0%);
  transition: all 1s;
}
.big-contain {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.btitle {
  font-size: 1.5em;
  font-weight: bold;
  color: rgb(57, 167, 176);
  margin-bottom: 5px;
}
.bform {
  width: 100%;
  height: 40%;
  padding: 2em 0;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
}
.bform .errTips {
  display: block;
  width: 50%;
  text-align: left;
  color: red;
  font-size: 0.7em;
  margin-left: 1em;
}
.bform input {
  width: 50%;
  height: 30px;
  border: none;
  outline: none;
  border-radius: 10px;
  padding-left: 2em;
  background-color: #f0f0f0;
}
.bbutton {
  width: 20%;
  height: 40px;
  border-radius: 24px;
  border: none;
  outline: none;
  background-color: rgb(57, 167, 176);
  color: #fff;
  font-size: 0.9em;
  cursor: pointer;
}
.small-box {
  width: 30%;
  height: 100%;
  background: linear-gradient(135deg, rgb(57, 167, 176), rgb(56, 183, 145));
  position: absolute;
  top: 0;
  left: 0;
  transform: translateX(0%);
  transition: all 1s;
  border-top-left-radius: inherit;
  border-bottom-left-radius: inherit;
}
.small-contain {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.stitle {
  font-size: 1.5em;
  font-weight: bold;
  color: #fff;
}
.scontent {
  font-size: 0.8em;
  color: #fff;
  text-align: center;
  padding: 2em 4em;
  line-height: 1.7em;
}
.sbutton {
  width: 60%;
  height: 40px;
  border-radius: 24px;
  border: 1px solid #fff;
  outline: none;
  background-color: transparent;
  color: #fff;
  font-size: 0.9em;
  cursor: pointer;
}

.big-box.active {
  left: 0;
  transition: all 0.5s;
}
.small-box.active {
  left: 100%;
  border-top-left-radius: 0;
  border-bottom-left-radius: 0;
  border-top-right-radius: inherit;
  border-bottom-right-radius: inherit;
  transform: translateX(-100%);
  transition: all 1s;
}
</style>
