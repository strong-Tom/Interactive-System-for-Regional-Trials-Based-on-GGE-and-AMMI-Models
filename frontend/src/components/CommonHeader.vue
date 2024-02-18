<template>
  <header>
    <div class="l-content">
      <!-- 控制是否展开的按钮 -->
      <el-button
        @click="
          () => {
            this.$store.commit('collapseMenu');
          }
        "
        icon="el-icon-menu"
        size="mini"
      >
      </el-button>
      <h2>Expert system for poplar-site matching in Songnen Plain</h2>
    </div>
    <div class="r-content">
      <el-dropdown
        szie="mini"
        trigger="click"
        slot="dropdown"
        @command="handleCommand"
      >
        <div style="display: flex">
          <div><img :src="userImage" alt="" class="user" /></div>
          <div
            class="name"
            style="
              margin-top: 5px;
              margin-left: 5px;
              font-size: 20px;
              color: black;
            "
          >
            {{ username }}
          </div>
        </div>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item command="userCenter">User Center</el-dropdown-item>
          <el-dropdown-item command="loginout">Quit</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
    </div>
  </header>
</template>
<script>
import axios from "axios";
export default {
  name: "CommonHeader",
  data() {
    return {
      userImage: require("../assets/images/user.jpeg"),
      username: null,
      password: null,
      email: null,
    };
  },
  methods: {
    handleMenu() {
      this.$store.commit("collapseMenu");
    },
    handleCommand(command) {
      if (command == "loginout") {
        sessionStorage.removeItem("ms_useremail");
        sessionStorage.removeItem("ms_userpassword");
        let flag = false;
        this.$store.commit("login", flag);
        this.$router.push("/");
      } else if (command == "userCenter") {
        this.$router.push("/userCenter");
      }
    },
  },
  created() {
    this.breadNews = this.$route.meta;
  },
  mounted() {
    axios({
      method: "post",
      url: "http://127.0.0.1:8000/api/login/",
      data: {
        email: sessionStorage.getItem("ms_useremail"),
        password: sessionStorage.getItem("ms_userpassword"),
      },
    }).then((res) => {
      this.username = res.data.user[0].username;
      this.email = res.data.user[0].email;
      this.password = res.data.user[0].password;
    });
  },
};
</script>
<style lang="less" scoped>
header {
  display: flex;
  height: 100%;
  justify-content: space-between;
  align-items: center;
}
.l-content {
  display: flex;
  align-items: center;
  .el-button {
    margin-right: 20px;
  }
}
.r-content {
  margin-right: 35px;
  .user {
    width: 40px;
    height: 40px;
    //使头像变成圆形
    border-radius: 50%;
  }
}
</style>
