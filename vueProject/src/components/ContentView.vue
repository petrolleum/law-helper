<template>
  <div class="content" @scroll="handleScroll">
    <div v-if="this.haveData">
      <div v-for="(content, num) in lawData" :key="num">
        <div>
          <div class="content-title">{{this.getCharacter(content.num)}}</div>
          <div class="content-content">{{content.content}}</div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { requestUrl, lawToRequestPerUpdate } from "@/globalVar";
import axios from "axios";
import Cvcomponent from "./Cvcomponent.vue";

export default {
  props: {
    selectedLaw: {
      type: String,
      required: true,
    },
    selectedContent:{
      type:String,
      required:true
    }
  },
  data() {
    return {
      lawData: [],
      isLoading: false,
      haveData:false,//确保得到数据后
      selectedLawLoc:1,
      position:0,//用于标识当前的位置
      dataType:'byNum'
    };
  },
  mounted() {
    if(this.selectedLawLoc==1){
      this.selectedLawLoc=Number(this.selectedLaw);
      this.getLawDown(this.selectedLaw);
    }
    
  },
  updated(){
    const container = this.$el;
    container.scrollTop=this.position;
  },
  watch:{
    selectedLaw(newValue,oldValue){
      this.dataType='byNum';
      this.selectedLawLoc=Number(this.selectedLaw);
      this.getLawSelect(this.selectedLaw,0);
    },
    selectedContent(newValue,oldValue){
      if(this.selectedContent!=''){
        this.dataType='byContent';
        this.getLawByContent(this.selectedContent,0);
      }else{
        this.selectedLawLoc=Number(this.selectedLaw,0);
      this.getLawDown(this.selectedLaw);
      this.dataType='byNum';
      }
    }
  },
  methods: {
    handleScroll() {
      const container = this.$el;
      if (
        container.scrollHeight - container.scrollTop <=
        container.clientHeight+10&&this.isLoading==false&&this.dataType=='byNum'
      ) {
        this.selectedLawLoc = lawToRequestPerUpdate+this.selectedLawLoc;
        this.getLawDown(this.selectedLawLoc,container.scrollTop);
        
      } else if (container.scrollTop < 0) {
        this.getLawUp(selectedLaw);
        selectedLaw -= lawToRequestPerUpdate;
      }
    },
    getLawDown(num,position) {
      var requestParam = { lawNum: num };
      this.isLoading = true;//暂未用到
      this.haveData=false;
      axios
        .post(requestUrl + "/getLawByNum/", requestParam)
        .then((response) => {
          const responseData = response.data.law;
          const jsonArray = JSON.parse(responseData);
          for (var i = 0; i < jsonArray.length; i++) {
            this.lawData.push(jsonArray[i]);
          }
          this.isLoading = false;
          this.haveData = true;
          this.position=position;
          
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getLawUp(num,position) {
      var requestParam = { num: num };
      this.isLoading = true;
      axios
        .post(requestUrl + "/getLaw", requestParam)
        .then((response) => {
          const responseData = response.data;
          lawData = responseData + lawData;
          this.isLoading = false;
        })
        .catch((error) => {});
    },
    getLawSelect(num,position) {
      this.lawData = [];
      console.log(this.lawData.length);
      var requestParam = { lawNum: num };
      this.isLoading = true;
      axios
        .post(requestUrl + "/getLawByNum/", requestParam)
        .then((response) => {
          const responseData = response.data.law;
          const jsonArray = JSON.parse(responseData);
          for (var i = 0; i < jsonArray.length; i++) {
            this.lawData.push(jsonArray[i]);
          }
          this.isLoading = false;
          this.haveData = true;
          this.position=position;
        
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getLawByContent(lawContent,position){
      this.lawData = [];
      console.log(this.lawData.length);
      var requestParam = { lawContent: lawContent };
      this.isLoading = true;
      axios
        .post(requestUrl + "/getLawByContent/", requestParam)
        .then((response) => {
          const responseData = response.data.law;
          const jsonArray = JSON.parse(responseData);
          for (var i = 0; i < jsonArray.length; i++) {
            this.lawData.push(jsonArray[i]);
          }
          this.isLoading = false;
          this.haveData = true;
          this.position=position;
        
        })
        .catch((error) => {
          console.log(error);
        });
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
        return "第"+res + "条";
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
        return "第"+ res + "条";
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
  
  components: { Cvcomponent },
};
</script>
<style scoped>
.content {
  overflow-y: scroll;
  border: 1px solid black;
  height: 1200px;
  background-color: white;
}
.content-title{
  font-size: 30px;
    font-weight: bold;
    padding-top: 20px;
    padding-bottom: 20px;
    text-align: center;
}
.content-content{
  font-size: 15px;
    padding-bottom: 20px;
}
html {
  overflow-x: hidden;
  overflow-y: scroll;
}
.content::-webkit-scrollbar {
  width: 12px; /* 设置滚动条宽度 */
}
.content::-webkit-scrollbar-thumb {
  border-radius: 10px;
  -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
  border-radius: 10px;
  transition: 0.3s ease-in-out;
}
.content::-webkit-scrollbar-track {
  border-radius: 10px;
  -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
  background-color: #f5f5f5;
}
</style>
