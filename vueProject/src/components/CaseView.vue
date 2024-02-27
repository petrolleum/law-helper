<template>
  <div class="all">
    <div>
      <CaseSearch @searchEvent="searchEvent" />
    </div>
    <div class="view">
      <div class="column">
        <div class="inline-column" @click="changeType(1)">刑事案件</div>
        <div class="inline-column" @click="changeType(2)">民事案件</div>
        <div class="inline-column" @click="changeType(3)">行政案件</div>
        <div class="inline-column" @click="changeType(4)">执行案件</div>
      </div>
      <CaseSelect
        :caseType="this.caseType"
        :searchContent="this.searchContent"
        :curPage="this.curPage"
      />
      <div class="pagination">
    <!-- 渲染分页按钮 -->
    <button @click="gotoPage(1)" class="page-btn">首页</button>
    <button @click="prevPage" class="page-btn">上一页</button>
    <span>{{curPage}}页</span>
    <button @click="nextPage" class="page-btn">下一页</button>
    <button @click="gotoPage(totalPages)" class="page-btn">尾页</button>
    <span>共{{totalPage}}页</span>
  </div>
    </div>
  </div>
</template>
<script scoped>
import axios from "axios";
import CaseViewComponent from "./CaseViewComponent.vue";
import { requestUrl } from "@/globalVar";
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
      caseType: 1,
      searchContent: "",
      curPage: 1,
      totalPage: 0,
    };
  },
  methods: {
    searchEvent(param) {
      if (param != "") {
        this.searchContent = param;
        this.caseType = 0;
      }
    },
    changeType(num) {
      this.caseType = num;
    },
  },
};
</script>
<style scoped>
.all {
  text-align: center;
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
