<template>
  <div class="all-lc">
    <div class="container-dir">
      <div class="law-title">
        <div
          class="dir-title"
          style="font-size: 20px; font-weight: bold; padding-bottom: 30px"
        >
          基本信息
        </div>
        <div class="dir-title">效力级别：法律</div>
        <div class="dir-title">发布日期：2017-11-04</div>
        <div class="dir-title">实施日期：2017-11-04</div>
        <div class="dir-title">发布部门：全国人民代表大会</div>
      </div>
      <div style="background-color: white;">
        <div>
        <div style="font-size: 20px;font-weight: bold;padding-bottom: 10px;">通过法条内容查找法条</div>
        <input type="text" v-model="selectedContent">
      </div>
      </div>
      <div>
        <div class="law-dir" ref="lawDir">
          <div style="font-size: 20px; font-weight: bold; padding-bottom: 30px">
            目录
          </div>
          <div
            class="dir-item"
            v-for="(value, index) in dirArr"
            :key="index"
            @click="this.selectLaw(index)"
          >
            {{ value }}
          </div>
        </div>
      </div>
    </div>

    <div class="container-content">
      <ContentView :selectedLaw="this.selectedLaw" :selectedContent="this.selectedContent"/>
    </div>
  </div>
</template>

<script scoped>
import axios from "axios";
import ContentView from "./ContentView.vue";
import { requestUrl } from "@/globalVar";
export default {
  components: {
    ContentView,
    ContentView,
  },
  data() {
    return {
      pageMax: 400,
      dirArr: [],
      selectedLaw: "1",
      selectedContent:"",
    };
  },
  beforeMount() {
    this.getDir();
  },
  methods: {
    selectLaw(num) {
      this.selectedLaw = String(num+1);
      console.log(this.selectedLaw);
    },
    getDir() {
      for (let i = 1; i < this.pageMax; i++) {
        this.dirArr.push(this.getCharacter(i));
      }
    },
    getCharacter(num) {
      var res = "";
      if (num < 100) {
        let cnt = 0;
        while (num != 0) {
          if (cnt == 1) {
            res = this.change(num % 10) + "十" + res;
          } else {
            if (num % 10 != 0) {
              res = this.change(num % 10) + res;
            }
          }
          num = Math.floor(num / 10);
          cnt++;
        }
        return res + "条";
      } else {
        let cnt = 0;
        while (num != 0) {
          if (cnt == 1) {
            res = this.change(num % 10) + "十" + res;
          } else if (cnt == 2) {
            res = this.change(num % 10) + "百" + res;
          } else {
            if (num % 10 != 0) {
              res = this.change(num % 10) + res;
            }
          }
          num = Math.floor(num / 10);
          cnt++;
        }
        return res + "条";
      }
    },
    change(num) {
      switch (num) {
        case 0:
          return "零";
        case 1:
          return "一";
        case 2:
          return "二";
        case 3:
          return "三";
        case 4:
          return "四";
        case 5:
          return "五";
        case 6:
          return "六";
        case 7:
          return "七";
        case 8:
          return "八";
        case 9:
          return "九";
      }
    },
  },
};
</script>

<style>
html {
  overflow-x: hidden;
  overflow-y: scroll;
}
.all-lc {
  display: flex;
  flex-direction: row;
  background-color: rgb(204, 204, 204);
  width: 100%;
  gap: 50px;
  /* background-color:grey; */
}
.container-dir {
  width: 30%;
  display: flex;
  flex-direction: column;
  gap: 100px;
}
.law-title {
  background-color: white;
  padding-top: 50px;
}
.dir-title {
  padding-left: 30px;
  padding-bottom: 20px;
}
.container-room {
  width: 100px;
  background-color: aqua;
  display: flexbox;
}
.container-content {
  flex: 0 0 auto;
  box-sizing: content-box;
  display: flex;
  width: 60%;
  background-color: white;
}

.law-dir {
  overflow-y: scroll;
  border: 1px solid black;
  height: 600px;
  background-color: white;
}
.dir-item {
  cursor: pointer;
  border-bottom: 1px dashed black;
}
/* 定制滚动条样式 */
.law-dir::-webkit-scrollbar {
  width: 12px; /* 设置滚动条宽度 */
}
.law-dir::-webkit-scrollbar-thumb {
  border-radius: 10px;
  -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
  border-radius: 10px;
  transition: 0.3s ease-in-out;
}
.law-dir::-webkit-scrollbar-track {
  border-radius: 10px;
  -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
  background-color: #f5f5f5;
}
</style>
