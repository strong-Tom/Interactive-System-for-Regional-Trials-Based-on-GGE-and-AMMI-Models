<template>
  <div>
    <div class="head" style="display: flex;justify-content:space-around;">
      <h5>(Ⅲ) 西部半干旱平原区</h5>
    </div>
    <!-- 首先写几个button按钮 -->
    <div class="btn_switch">
      <button class="btn_anniu" @click="change(0)" :class="{ newStyle: 0 === number }">
        重要树种叶片图
      </button>
      <button class="btn_anniu" @click="change(1)" :class="{ newStyle: 1 === number }">
        齐齐哈尔地区杨树品种造林综合评价
      </button>
      <button class="btn_anniu" @click="change(2)" :class="{ newStyle: 2 === number }">
        各地青山杨生长调查汇总表
      </button>
      <button class="btn_anniu" @click="change(3)" :class="{ newStyle: 3 === number }">
        银中杨在松嫩平原速生丰产用材林生长指标
      </button>
      <el-button type="primary" size="default" @click="tz">
        跳转到下一个生态区页面</el-button>
    </div>
    <!-- 写上我们想要它切换显示的内容 -->
    <div>
      <!-- 显示图片 -->
      <div v-show="0 === number">
        <div style="padding-top: 30px">
          <!-- 第一行 -->
          <el-row :gutter="20">
            <el-col :span="4">
              <div class="grid-content bg-purple">
                <div style="text-align: center;  line-height">小黑杨叶片</div>
                <img src="@/assets/images/tree/小黑杨叶片.png" alt="" style="
                        background: no-repeat center center;
                        width: 80%;
                        height: 80%;
                        margin: 20px;
                      " />
              </div>
            </el-col>
            <el-col :span="4">
              <div class="grid-content bg-purple">
                <div style="text-align: center;  line-height">黑青杨叶片</div>
                <img src="@/assets/images/tree/黑青杨叶片.png" alt="" style="
                        background: no-repeat center center;
                        width: 100%;
                        height: 100%;
                        margin: 20px;
                      " />
              </div>
            </el-col>
            <el-col :span="4">
              <div class="grid-content bg-purple">
                <div style="text-align: center;  line-height">银中杨叶片</div>
                <img src="@/assets/images/tree/银中杨叶片.png" alt="" style="
                        background: no-repeat center center;
                        width: 80%;
                        height: 80%;
                        margin: 20px;
                      " />
              </div>
            </el-col>
            <el-col :span="4">
              <div class="grid-content bg-purple">
                <div style="text-align: center;  line-height">青山杨叶片</div>
                <img src="@/assets/images/tree/青山杨叶片.png" alt="" style="
                        background: no-repeat center center;
                        width: 90%;
                        height: 90%;
                        margin: 20px;
                      " />
              </div>
            </el-col>
            <el-col :span="4">
              <div class="grid-content bg-purple">
                <div style="text-align: center;  line-height">
                  龙丰1号杨叶片
                </div>
                <img src="@/assets/images/tree/龙丰1号杨叶片.png" alt="" style="
                        background: no-repeat center center;
                        width: 60%;
                        height: 60%;
                        margin: 20px;
                      " />
              </div>
            </el-col>
            <el-col :span="4">
              <div class="grid-content bg-purple">
                <div style="text-align: center;  line-height">中雄4号杨</div>
                <img src="@/assets/images/tree/中雄4号杨.png" alt="" style="
                        background: no-repeat center center;
                        width: 70%;
                        height: 70%;
                        margin: 20px;
                      " />
              </div>
            </el-col>
          </el-row>
          <!-- 第二行 -->
          <el-row :gutter="20">
            <el-col :span="6">
              <div class="grid-content bg-purple"></div>
              <div style="text-align: center;  line-height;margin-top:30px;"></div>
              <img src="@/assets/images/forest.jpg" alt="" style="
                      background: no-repeat center center;
                      width: 110%;
                      height: 120%;
                      margin: 20px;
                      background-size: contain;
                    " />
            </el-col>

            <el-col :span="8">
              <div style="margin-left: 100px; margin-top: 100px; width: 100%">
                <div style="text-align: center;  line-height;margin-top:-50px;margin-bottom: 20px;">
                  视频
                </div>
                <video-player class="video-player vjs-custom-skin" ref="videoPlayer" :playsline="false"
                  :options="playerOptions"></video-player>
              </div>
            </el-col>
            <el-col :span="8">
              <div style="margin-left: 100px; margin-top: 100px; width: 100%">
                <div style="text-align: center;  line-height;margin-top:-50px;margin-bottom: 20px;">
                  视频
                </div>
                <video-player class="video-player vjs-custom-skin" ref="videoPlayer" :playsline="false"
                  :options="playerOptions1"></video-player>
              </div>
            </el-col>
          </el-row>
        </div>
      </div>
      <!-- 显示表格，齐齐哈尔地区杨树品种造林综合评价 -->
      <div v-show="1 === number">
        <el-table :data="tableData" height="1100" border style="width: 100%"
          :header-cell-style="{ textAlign: 'center', color: '#000' }" :cell-style="{ textAlign: 'center' }">
          <el-table-column type="index" label="序号" width="50">
          </el-table-column>
          <el-table-column prop="data1" label="品种名称" width="150">
          </el-table-column>
          <el-table-column prop="data2" label="树径分级" width="180">
          </el-table-column>
          <el-table-column prop="data3" label="冻害分级"> </el-table-column>
          <el-table-column prop="data4" label="虫害分级"> </el-table-column>
          <el-table-column prop="data5" label="病害分级"> </el-table-column>
          <el-table-column prop="data6" label="干型分级"> </el-table-column>
          <el-table-column prop="data7" label="造林保存率"> </el-table-column>
          <el-table-column prop="data8" label="综合指数值"> </el-table-column>
          <el-table-column prop="data9" label="综合评价分级"> </el-table-column>
        </el-table>
        <!-- 说明表 -->
        <h4 style="padding: 20px; text-align: center">
          杨树无性系造林综合评价量化值
        </h4>
        <el-table :data="tableData0" height="500" border style="width: 100%"
          :header-cell-style="{ textAlign: 'center', color: '#000' }" :cell-style="{ textAlign: 'center' }">
          <el-table-column prop="data1" label="因     素
    " width="180">
          </el-table-column>
          <el-table-column prop="data2" label="范    围
    " width="180">
          </el-table-column>
          <el-table-column prop="data3" label="A级

    ">
          </el-table-column>
          <el-table-column prop="data4" label="B级

    ">
          </el-table-column>
          <el-table-column prop="data5" label="C级

    ">
          </el-table-column>
          <el-table-column prop="data6" label="权重值
    ">
          </el-table-column>
        </el-table>
      </div>
      <!-- 显示表格，各地青山杨生长调查汇总表-->
      <div v-show="2 === number">
        <el-table :data="tableData1" height="1400" border style="width: 100%"
          :header-cell-style="{ textAlign: 'center', color: '#000' }" :cell-style="{ textAlign: 'center' }">
          <el-table-column prop="data1" label="地点" width="180">
          </el-table-column>
          <el-table-column prop="data2" label="年龄"> </el-table-column>
          <el-table-column prop="data3" label="品种"> </el-table-column>
          <el-table-column prop="data4" label="H（m）"> </el-table-column>
          <el-table-column prop="data5" label="H/对照(%)"> </el-table-column>
          <el-table-column prop="data6" label="D（cm）"> </el-table-column>
          <el-table-column prop="data7" label="D/对照(%)"> </el-table-column>
          <el-table-column prop="data8" label="V（m3）"> </el-table-column>
          <el-table-column prop="data9" label="V/对照(%)"> </el-table-column>
        </el-table>
      </div>
      <!-- 显示表格，银中杨在松嫩平原速生丰产用材林生长指标-->
      <div v-show="3 === number">
        <el-table :data="tableData2" height="800" border style="width: 100%;font-size:1px;"
          :header-cell-style="{ textAlign: 'center', color: '#000' }" :cell-style="{ textAlign: 'center' }">
          <el-table-column label="栽培区">
            <el-table-column prop="data1" label="年龄（a）">
            </el-table-column>
          </el-table-column>
          <el-table-column label="松嫩平原东部栽培区">
            <el-table-column prop="data5" label="平均胸径（cm）">
            </el-table-column>
            <el-table-column prop="data6" label="平均树高（m）">
            </el-table-column>
            <el-table-column prop="data7" label="年均蓄积生长量(m³/(hm²·a))">
            </el-table-column>
          </el-table-column>
          <el-table-column label="三江平原栽培区" width="180">
            <el-table-column prop="data2" label="平均胸径（cm）">
            </el-table-column>
            <el-table-column prop="data3" label="平均树高（m）">
            </el-table-column>
            <el-table-column prop="data4" label="年均蓄积生长量(m³/(hm²·a))">
            </el-table-column>
          </el-table-column>

          <el-table-column label="松嫩平原西部栽培区">
            <el-table-column prop="data8" label="平均胸径（cm）">
            </el-table-column>
            <el-table-column prop="data9" label="平均树高（m）">
            </el-table-column>
            <el-table-column prop="data10" label="年均蓄积生长量(m³/(hm²·a))">
            </el-table-column>
          </el-table-column>
        </el-table>
      </div>
    </div>
  </div>
</template>

<script>
import "video.js/dist/video-js.css";
import { videoPlayer } from "vue-video-player";
import axios from "axios";

export default {
  components: {
    videoPlayer,
  },
  name: "FrontendTest",

  data() {
    return {
      playerOptions: {
        height: "36",
        playbackRates: [0.7, 1.0, 1.5, 2.0], // 播放速度
        autoplay: false, // 如果true,浏览器准备好时开始回放。
        muted: false, // 默认情况下将会消除任何音频。
        loop: false, // 导致视频一结束就重新开始。
        preload: "auto", // 建议浏览器在<video>加载元素后是否应该开始下载视频数据。auto浏览器选择最佳行为,立即开始加载视频（如果浏览器支持）
        language: "zh-CN",
        aspectRatio: "16:9", // 将播放器置于流畅模式，并在计算播放器的动态大小时使用该值。值应该代表一个比例 - 用冒号分隔的两个数字（例如"16:9"或"4:3"）
        fluid: true, // 当true时，Video.js player将拥有流体大小。换句话说，它将按比例缩放以适应其容器。
        sources: [
          {
            type: "video/mp4", // 这里的种类支持很多种：基本视频格式、直播、流媒体等，具体可以参看git网址项目
            src: null, // url地址
          },
          {
            type: "video/mp4", // 这里的种类支持很多种：基本视频格式、直播、流媒体等，具体可以参看git网址项目
            src: null, // url地址
          },
        ],
        // poster: "../../../../static/full_res.jpg", // 你的封面地址

        width: document.documentElement.clientWidth, // 播放器宽度
        notSupportedMessage: "此视频暂无法播放，请稍后再试", // 允许覆盖Video.js无法播放媒体源时显示的默认信息。
        controlBar: {
          timeDivider: true,
          durationDisplay: true,
          remainingTimeDisplay: false,
          fullscreenToggle: true, // 全屏按钮
        },
      },
      playerOptions1: {
        height: "36",
        playbackRates: [0.7, 1.0, 1.5, 2.0], // 播放速度
        autoplay: false, // 如果true,浏览器准备好时开始回放。
        muted: false, // 默认情况下将会消除任何音频。
        loop: false, // 导致视频一结束就重新开始。
        preload: "auto", // 建议浏览器在<video>加载元素后是否应该开始下载视频数据。auto浏览器选择最佳行为,立即开始加载视频（如果浏览器支持）
        language: "zh-CN",
        aspectRatio: "16:9", // 将播放器置于流畅模式，并在计算播放器的动态大小时使用该值。值应该代表一个比例 - 用冒号分隔的两个数字（例如"16:9"或"4:3"）
        fluid: true, // 当true时，Video.js player将拥有流体大小。换句话说，它将按比例缩放以适应其容器。
        sources: [
          {
            type: "video/mp4", // 这里的种类支持很多种：基本视频格式、直播、流媒体等，具体可以参看git网址项目
            src: null, // url地址
          },
          {
            type: "video/mp4", // 这里的种类支持很多种：基本视频格式、直播、流媒体等，具体可以参看git网址项目
            src: null, // url地址
          },
        ],
        // poster: "../../../../static/full_res.jpg", // 你的封面地址

        width: document.documentElement.clientWidth, // 播放器宽度
        notSupportedMessage: "此视频暂无法播放，请稍后再试", // 允许覆盖Video.js无法播放媒体源时显示的默认信息。
        controlBar: {
          timeDivider: true,
          durationDisplay: true,
          remainingTimeDisplay: false,
          fullscreenToggle: true, // 全屏按钮
        },
      },
      number: 0,
      tableData2: [
        {
          data1: 3,
          data2: 4.5,
          data3: 5,
          data4: "－",
          data5: 4.5,
          data6: 4.5,
          data7: "－",
          data8: 4,
          data9: 4,
          data10: "－",
        },
        {
          data1: 4,
          data2: 7.5,
          data3: 7,
          data4: 2.2,
          data5: 6.5,
          data6: 6.5,
          data7: 1.6,
          data8: 6.5,
          data9: 6,
          data10: 1.3,
        },
        {
          data1: 5,
          data2: 10.5,
          data3: 9,
          data4: 4,
          data5: 9.5,
          data6: 8.5,
          data7: 3.2,
          data8: 8.5,
          data9: 8,
          data10: 2.5,
        },
        {
          data1: 6,
          data2: 13.5,
          data3: 11,
          data4: 6.4,
          data5: 12.5,
          data6: 10.5,
          data7: 5.3,
          data8: 11,
          data9: 10,
          data10: 4.1,
        },
        {
          data1: 7,
          data2: 16,
          data3: 12.5,
          data4: 9.2,
          data5: 15,
          data6: 12,
          data7: 7.5,
          data8: 13.5,
          data9: 11.5,
          data10: 5.9,
        },
        {
          data1: 8,
          data2: 18.5,
          data3: 14.5,
          data4: 12,
          data5: 17,
          data6: 13.5,
          data7: 9.6,
          data8: 15.5,
          data9: 13.5,
          data10: 7.8,
        },
        {
          data1: 9,
          data2: 20.5,
          data3: 16,
          data4: 14.3,
          data5: 19,
          data6: 15,
          data7: 11.5,
          data8: 17,
          data9: 15,
          data10: 9.5,
        },
        {
          data1: 10,
          data2: 22,
          data3: 17,
          data4: 16.1,
          data5: 20.5,
          data6: 16.5,
          data7: 13.1,
          data8: 18.5,
          data9: 16,
          data10: 10.9,
        },
        {
          data1: 11,
          data2: 23.5,
          data3: 18.5,
          data4: 17.3,
          data5: 21.5,
          data6: 17.5,
          data7: 14.2,
          data8: 19.5,
          data9: 17.5,
          data10: 11.8,
        },
        {
          data1: 12,
          data2: 24.5,
          data3: 19.5,
          data4: 18.2,
          data5: 22.5,
          data6: 19,
          data7: 15.1,
          data8: 20.5,
          data9: 18.5,
          data10: 12.5,
        },
        {
          data1: 13,
          data2: 25,
          data3: 20.5,
          data4: 18.8,
          data5: 23.5,
          data6: 19.5,
          data7: 15.7,
          data8: 21.5,
          data9: 19.5,
          data10: 12.9,
        },
        {
          data1: 14,
          data2: 26,
          data3: 21.5,
          data4: 19.4,
          data5: 24,
          data6: 20.5,
          data7: 16.1,
          data8: 22,
          data9: 20,
          data10: 13.2,
        },
        {
          data1: 15,
          data2: 26.5,
          data3: 22,
          data4: 19.8,
          data5: 25,
          data6: 21,
          data7: 16.4,
          data8: 22.5,
          data9: 20.5,
          data10: 13.3,
        },
      ],
      tableData: [
        {
          data1: "小青黑",
          data2: 3,
          data3: 3,
          data4: 3,
          data5: 3,
          data6: 3,
          data7: 3,
          data8: 3,
          data9: 1,
        },
        {
          data1: "小黑14",
          data2: 2,
          data3: 3,
          data4: 3,
          data5: 3,
          data6: 3,
          data7: 3,
          data8: 2.75,
          data9: 1,
        },
        {
          data1: "小黑杨",
          data2: 2,
          data3: 3,
          data4: 3,
          data5: 3,
          data6: 3,
          data7: 3,
          data8: 2.75,
          data9: 1,
        },
        {
          data1: "青山杨",
          data2: 3,
          data3: 3,
          data4: 3,
          data5: 3,
          data6: 2,
          data7: 3,
          data8: 2.85,
          data9: 1,
        },
        {
          data1: "银中杨",
          data2: 3,
          data3: 3,
          data4: 2,
          data5: 3,
          data6: 3,
          data7: 3,
          data8: 2.85,
          data9: 1,
        },
        {
          data1: "北京605",
          data2: 3,
          data3: 2,
          data4: 2,
          data5: 2,
          data6: 3,
          data7: 2,
          data8: 2.4,
          data9: 2,
        },
        {
          data1: "DN113",
          data2: 3,
          data3: 1,
          data4: 2,
          data5: 2,
          data6: 3,
          data7: 1,
          data8: 2.1,
          data9: 2,
        },
        {
          data1: "白林3",
          data2: 3,
          data3: 2,
          data4: 2,
          data5: 2,
          data6: 2,
          data7: 2,
          data8: 2.25,
          data9: 2,
        },
        {
          data1: "中黑防",
          data2: 2,
          data3: 2,
          data4: 3,
          data5: 3,
          data6: 3,
          data7: 3,
          data8: 2.55,
          data9: 2,
        },
        {
          data1: "白林1",
          data2: 2,
          data3: 2,
          data4: 2,
          data5: 2,
          data6: 2,
          data7: 2,
          data8: 2,
          data9: 2,
        },
        {
          data1: "白城2",
          data2: 1,
          data3: 2,
          data4: 2,
          data5: 2,
          data6: 2,
          data7: 2,
          data8: 1.75,
          data9: 2,
        },
        {
          data1: "B6",
          data2: 1,
          data3: 3,
          data4: 2,
          data5: 2,
          data6: 2,
          data7: 2,
          data8: 1.95,
          data9: 2,
        },
        {
          data1: "北京3",
          data2: 3,
          data3: 2,
          data4: 2,
          data5: 1,
          data6: 2,
          data7: 3,
          data8: 2.2,
          data9: 2,
        },
        {
          data1: "黑林1",
          data2: 3,
          data3: 2,
          data4: 1,
          data5: 1,
          data6: 3,
          data7: 2,
          data8: 2.1,
          data9: 2,
        },
        {
          data1: "群众杨",
          data2: 1,
          data3: 1,
          data4: 2,
          data5: 1,
          data6: 1,
          data7: 1,
          data8: 1.15,
          data9: 3,
        },
        {
          data1: "大青杨",
          data2: 2,
          data3: 2,
          data4: 1,
          data5: 1,
          data6: 2,
          data7: 1,
          data8: 1.6,
          data9: 3,
        },
        {
          data1: "昭林6",
          data2: 1,
          data3: 1,
          data4: 1,
          data5: 1,
          data6: 2,
          data7: 1,
          data8: 1.15,
          data9: 3,
        },
        {
          data1: "赤峰杨",
          data2: 2,
          data3: 1,
          data4: 1,
          data5: 1,
          data6: 1,
          data7: 1,
          data8: 1.25,
          data9: 3,
        },
        {
          data1: "小钻杨",
          data2: 1,
          data3: 1,
          data4: 1,
          data5: 1,
          data6: 1,
          data7: 1,
          data8: 1,
          data9: 3,
        },
        {
          data1: "健杨",
          data2: 2,
          data3: 1,
          data4: 1,
          data5: 1,
          data6: 1,
          data7: 1,
          data8: 1.25,
          data9: 3,
        },
        {
          data1: "I-45/51",
          data2: 1,
          data3: 1,
          data4: 1,
          data5: 1,
          data6: 1,
          data7: 1,
          data8: 1,
          data9: 3,
        },
      ],
      tableData0: [
        {
          data1: "径生长（胸径）",
          data2: "",
          data3: "大于对照1.5cm以上",
          data4: "平均在A、C之间",
          data5: "小于对照1.0cm 以下",
          data6: 0.25,
        },
        {
          data1: "冻     害",
          data2: "主干",
          data3: "无",
          data4: "微冻裂冻害率低于20%",
          data5: "干冻裂严重,冻害率大于20%",
          data6: 0.2,
        },
        {
          data1: "虫     害",
          data2: "蛀干害虫",
          data3: "无",
          data4: "主干无,侧枝有,虫害率低于40%",
          data5: "主干和侧枝均有,虫害率大于40%",
          data6: 0.15,
        },
        {
          data1: "病     害",
          data2: "溃疡,腐烂病",
          data3: "无",
          data4: "有,病害率低于20%,不影响生长",
          data5: "严重,病害率大于20%",
          data6: 0.15,
        },
        {
          data1: "干    型",
          data2: "主干",
          data3: "通直",
          data4: "小于1/3弯曲",
          data5: "大于1/3弯曲",
          data6: 0.15,
        },
        {
          data1: "造林保存率（%）",
          data2: "",
          data3: "大于85%",
          data4: "40%～85%之间",
          data5: "40%以下",
          data6: 0.1,
        },
        { data1: "得分值", data2: "", data3: 3, data4: 2, data5: 1, data6: "" },
      ],
      tableData1: [
        {
          data1: "大庆红旗林场",
          data2: 18,
          data3: "青山杨",
          data4: 18.7,
          data5: 123,
          data6: 18,
          data7: 116.1,
          data8: 0.2208,
          data9: 160.8,
        },
        {
          data1: "",
          data2: 18,
          data3: "小黑杨(ck)",
          data4: 15.2,
          data5: 100,
          data6: 15.5,
          data7: 100,
          data8: 0.1373,
          data9: 100,
        },
        {
          data1: "龙江县错海林场",
          data2: 10,
          data3: "青山杨",
          data4: 18.2,
          data5: 141.1,
          data6: 14.9,
          data7: 106.4,
          data8: 0.1478,
          data9: 151,
        },
        {
          data1: "",
          data2: 10,
          data3: "小黑杨(ck)",
          data4: 12.9,
          data5: 100,
          data6: 14,
          data7: 100,
          data8: 0.0979,
          data9: 100,
        },
        {
          data1: "甘南县甘南林场",
          data2: 4,
          data3: "青山杨",
          data4: 8,
          data5: 133.3,
          data6: 6.3,
          data7: 165.8,
          data8: 0.0137,
          data9: 334.1,
        },
        {
          data1: "",
          data2: 4,
          data3: "小黑杨(ck)",
          data4: 6,
          data5: 100,
          data6: 3.8,
          data7: 100,
          data8: 0.0041,
          data9: 100,
        },
        {
          data1: "拜泉县兴国乡",
          data2: 12,
          data3: "青山杨",
          data4: 17.5,
          data5: 102.9,
          data6: 23.9,
          data7: 109.1,
          data8: 0.3677,
          data9: 122.1,
        },
        {
          data1: "",
          data2: 12,
          data3: "小黑杨(ck)",
          data4: 17,
          data5: 100,
          data6: 21.9,
          data7: 100,
          data8: 0.3012,
          data9: 100,
        },
        {
          data1: "克山县北联林场",
          data2: 5,
          data3: "青山杨",
          data4: 3.6,
          data5: 120,
          data6: 4.2,
          data7: 155.6,
          data8: 0.0037,
          data9: 264.3,
        },
        {
          data1: "",
          data2: 5,
          data3: "小黑杨(ck)",
          data4: 3,
          data5: 100,
          data6: 2.7,
          data7: 100,
          data8: 0.0014,
          data9: 100,
        },
        {
          data1: "富裕县富裕林场",
          data2: 8,
          data3: "青山杨",
          data4: 11.6,
          data5: 119.6,
          data6: 12.1,
          data7: 114.2,
          data8: 0.0671,
          data9: 149.8,
        },
        {
          data1: "",
          data2: 8,
          data3: "小黑杨(ck)",
          data4: 9.7,
          data5: 100,
          data6: 10.6,
          data7: 100,
          data8: 0.0448,
          data9: 100,
        },
        {
          data1: "望奎县",
          data2: 5,
          data3: "青山杨",
          data4: 8.1,
          data5: 152.8,
          data6: 7.6,
          data7: 152,
          data8: 0.0201,
          data9: 309.2,
        },
        {
          data1: "",
          data2: 5,
          data3: "小黑杨(ck)",
          data4: 5.3,
          data5: 100,
          data6: 5,
          data7: 100,
          data8: 0.0065,
          data9: 100,
        },
        {
          data1: "新江实验林场",
          data2: 5,
          data3: "青山杨",
          data4: 7.6,
          data5: 172.7,
          data6: 7.8,
          data7: 195,
          data8: 0.0204,
          data9: 551.4,
        },
        {
          data1: "",
          data2: 5,
          data3: "小黑杨(ck)",
          data4: 4.4,
          data5: 100,
          data6: 4,
          data7: 100,
          data8: 0.0037,
          data9: 100,
        },
        {
          data1: "齐齐哈尔市全合台",
          data2: 10,
          data3: "青山杨",
          data4: 10.7,
          data5: 130.5,
          data6: 14.2,
          data7: 146.4,
          data8: 0.0867,
          data9: 261.9,
        },
        {
          data1: "",
          data2: 10,
          data3: "小黑杨(ck)",
          data4: 8.2,
          data5: 100,
          data6: 9.7,
          data7: 100,
          data8: 0.0331,
          data9: 100,
        },
        {
          data1: "巴彦县龙泉林场",
          data2: 4,
          data3: "青山杨",
          data4: 7.4,
          data5: 132.1,
          data6: 7.1,
          data7: 122.4,
          data8: 0.0165,
          data9: 181.3,
        },
        {
          data1: "",
          data2: 4,
          data3: "小黑杨(ck)",
          data4: 5.6,
          data5: 100,
          data6: 5.8,
          data7: 100,
          data8: 0.0091,
          data9: 100,
        },
        {
          data1: "富锦东风岗林场",
          data2: 5,
          data3: "青山杨",
          data4: 8.9,
          data5: 130.9,
          data6: 9.4,
          data7: 120.5,
          data8: 0.033,
          data9: 176.5,
        },
        {
          data1: "",
          data2: 5,
          data3: "小黑杨(ck)",
          data4: 6.8,
          data5: 100,
          data6: 7.8,
          data7: 100,
          data8: 0.0187,
          data9: 100,
        },
        {
          data1: "宁安市三灵林场",
          data2: 4,
          data3: "青山杨",
          data4: 7.2,
          data5: 120,
          data6: 8.3,
          data7: 120.3,
          data8: 0.0221,
          data9: 163.7,
        },
        {
          data1: "",
          data2: 4,
          data3: "小黑杨(ck)",
          data4: 6,
          data5: 100,
          data6: 6.9,
          data7: 100,
          data8: 0.0135,
          data9: 100,
        },
        {
          data1: "五大连池二龙山林场",
          data2: 7,
          data3: "青山杨",
          data4: 10.2,
          data5: 127.5,
          data6: 11.8,
          data7: 126.9,
          data8: 0.0577,
          data9: 193,
        },
        {
          data1: "",
          data2: 7,
          data3: "小黑杨(ck)",
          data4: 8,
          data5: 100,
          data6: 9.3,
          data7: 100,
          data8: 0.0299,
          data9: 100,
        },
        {
          data1: "五大连池二龙山林场",
          data2: 7,
          data3: "青山杨",
          data4: 10.2,
          data5: 127.5,
          data6: 11.8,
          data7: 126.9,
          data8: 0.0577,
          data9: 193,
        },
        {
          data1: "",
          data2: 7,
          data3: "小黑杨(ck)",
          data4: 8,
          data5: 100,
          data6: 9.3,
          data7: 100,
          data8: 0.0299,
          data9: 100,
        },
      ],
      currentRow: null,
    };
  },

  mounted() {
    this.$axios.get("http://127.0.0.1:8000/api/video/6").then((res) => {
      // this.tableDataALL = res.data;
      // this.getList();
      // console.log(res.data.video);
      this.playerOptions.sources[0].src = res.data.video;
      console.log("----------", res.data.video);
    });
    this.$axios.get("http://127.0.0.1:8000/api/video/5").then((res) => {
      // this.tableDataALL = res.data;
      // this.getList();
      // console.log(res.data.video);
      this.playerOptions1.sources[0].src = res.data.video;
      console.log("----------", res.data.video);
    });
  },

  methods: {
    tz() {
      this.$router.push({ path: "/region15" });
    },
    change: function (index) {
      this.number = index; //重要处
    },
  },
};
</script>

<style lang="less" scoped>
.btn_anniu {
  width: 20%;
  padding: 20px;
  font-size: 15px;
  font-weight: bold;
  border: 0 solid #fff;
  color: #000;
  outline: none;
  background: #fff;
}

.newStyle {
  border-bottom: 2px solid #f0892e;
  color: #f0892e;
  font-size: 15px;
  font-weight: bold;
}

.el-row {
  margin-bottom: 20px;

  &:last-child {
    margin-bottom: 0;
  }
}

.el-col {
  border-radius: 4px;
}

.bg-purple-dark {
  //   background: #99a9bf;
}

.bg-purple {
  //   background: #d3dce6;
}

.bg-purple-light {
  background: #e5e9f2;
}

.grid-content {
  border-radius: 4px;
  min-height: 36px;
}

.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
</style>
