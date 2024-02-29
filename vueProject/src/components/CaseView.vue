<template>
  <div class="all">
    <div>
      <CaseSearch @searchEvent="searchEvent" />
    </div>
    <div class="view">
      <div class="column">
        <div class="inline-column" @click="changeType('刑事案件')">刑事案件</div>
        <div class="inline-column" @click="changeType('民事案件')">民事案件</div>
        <div class="inline-column" @click="changeType('执行案件')">执行案件</div>
        <div class="inline-column" @click="changeType('管辖案件')">管辖案件</div>
        <div class="inline-column" @click="changeType('强制清算与破产案件')">强制清算与破产案件</div>
      </div>
      <!-- 想不到好的办法了 -->
      <div style="background-color: #f2f2f2;;height: 20px;"></div>
      <div v-if="this.searchContent!=''">下面是{{searchContent}}的搜索结果。</div>
      <CaseSelect
        :searchContent="this.searchContent"
        :curPage="this.curPage"
        @totalPageEvent="totalPageEvent"
      />
      <div class="pagination">
    <!-- 渲染分页按钮 -->
    <button @click="gotoPage(1)" class="page-btn">首页</button>
    <button @click="prevPage()" class="page-btn">上一页</button>
    <span>{{curPage.split(';')[1]}}页</span>
    <button @click="nextPage()" class="page-btn">下一页</button>
    <button @click="gotoPage(this.totalPage)" class="page-btn">尾页</button>
    <span>共{{totalPage}}页</span>
  </div>
    </div>
  </div>
</template>
<script scoped>
import axios from "axios";
import CaseViewComponent from "./CaseViewComponent.vue";
import { pageSize, requestUrl,number_max } from "@/globalVar";
import CaseSearch from "./CaseSearch.vue";
import CaseSelect from "./CaseSelect.vue";
export default {
  components: {
    CaseViewComponent,
    CaseSearch,
    CaseSelect,
  },

  data() {
    return {
      caseType: "刑事案件",
      searchContent: "",
      curPage: "刑事案件;1",
      totalPage: 0,
    };
  },
  methods: {
    searchEvent(param) {
      if (param != "") {
        this.searchContent = param;
        this.caseType = "bySearch";
      }
    },
    changeType(num) {
      this.caseType = num;
      this.curPage=this.caseType+";"+this.curPage.split(';')[1];
      this.searchContent="";
    },
    prevPage(){
      if(Number(this.curPage.split(';')[1])>1){
        this.curPage=this.curPage.split(';')[0]+";"+(Number(this.curPage.split(';')[1])-1).toString();
      }
    },
    nextPage(){
      if(Number(this.curPage.split(';')[1])<this.totalPage){
        this.curPage=this.curPage.split(';')[0]+";"+(Number(this.curPage.split(';')[1])+1).toString();
      }
    },
    gotoPage(num){
      this.curPage=this.curPage.split(';')[0]+";"+num.toString();
    },
    totalPageEvent(data){
      this.totalPage=Math.floor(data/pageSize)-1;
    }
  },
};
</script>
<style scoped>
.all {
  text-align: center;
  background-color: #f2f2f2;
}
.view {
  text-align: center;
  display: inline-block;
  width: 50%;
}
.column {
  display: flex;
  justify-content: space-between;
}
.inline-column {
  margin: 0 -10px; /* 负的外边距值 */
  padding: 0 10px; /* 补偿的内边距值 */
  display: inline;
  text-align: center;
  font-size: 25px;
  cursor: pointer;
}
.pagination {
  text-align: center;
  margin-top: 20px;
}

.page-btn {
  padding: 8px 16px;
  margin: 0 5px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.page-btn:hover {
  background-color: #0056b3;
}
</style>
