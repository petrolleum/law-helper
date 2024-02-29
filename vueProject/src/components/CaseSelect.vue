<template>
  <div class="container">
    
    <div v-if="this.haveData">
      <div v-for="item in caseData" class="subContainer">
        <CaseViewComponent
          :id="item.id"
          :caseTitle="item.caseTitle"
          :caseId="item.caseId"
          :court="item.court"
          :religion="item.religion"
          :caseType="item.caseType"
          :proceeding="item.proceding"
          :reason="item.caseReason"
          :reference="item.reference"
          :judgementTime="item.judgementTime"
        />
        <div style="height: 30px;"></div>
      </div>
    </div>
  </div>
</template>
<script scoped>
import axios from "axios";
import CaseViewComponent from "./CaseViewComponent.vue";
import { number_max, requestUrl } from "@/globalVar";
import CaseSearch from "./CaseSearch.vue";

export default {
  components: {
    CaseViewComponent,
    CaseSearch,
  },
  props: {
    searchContent: {
      type: String,
    },
    curPage: {
      type: String,
    },
  },
  mounted() {
    
    this.requestCase(this.type1,1);
  },
  watch: {
  
    searchContent(newValue, oldValue) {
      this.requestCase('bySearch',this.page1,this.searchContent)
    },
    curPage(newValue, oldValue) {   
    this.type1=this.curPage.split(';')[0];
    this.page1=Number(this.curPage.split(';')[1]);
    console.log(this.page1);
    this.requestCase(this.type1,this.page1,'');
    },
    
  },
  data() {
    return {
      caseData: [],
      haveData:0,
      type1:"刑事案件",//这里的type1是type，上面的curPage是type+page
      page1:1//这里的page1是page，上面的curPage是type+page
    };
  },
  methods: {
  requestCase(type, page,searchContent) {
    var requestParam = { caseType: type, page: page ,searchContent:searchContent};
    axios
      .post(requestUrl + "/getJudgements/", requestParam)
      .then((response) => {
        this.caseData=[];
        this.haveData=1;
        const responseData = response.data.judgements;
        const totalData=response.data.total;

        this.$emit('totalPageEvent',totalData);
        const jsonArray = JSON.parse(responseData);
        for (var i = 0; i < jsonArray.length; i++) {
          jsonArray[i].deAccusation = [];
          jsonArray[i].reference = JSON.parse(jsonArray[i].reference);
          jsonArray[i].caseReason = JSON.parse(jsonArray[i].caseReason);
          this.caseData.push(jsonArray[i]);
        }
      })
      .catch((error) => {
        console.log(error);
      });
  },
  requestCaseByContent(content,page){
    var requestParam = { contentToSearch: content, page: page };
    axios
      .post(requestUrl + "/getJudgementsByContent/", requestParam)
      .then((response) => {
        this.caseData=[];
        this.haveData=1;
        const responseData = response.data.judgements;
        const totalData=response.data.total;

        this.$emit('totalPageEvent',totalData);
        const jsonArray = JSON.parse(responseData);
        for (var i = 0; i < jsonArray.length; i++) {
          jsonArray[i].deAccusation = [];
          jsonArray[i].reference = JSON.parse(jsonArray[i].reference);
          jsonArray[i].caseReason = JSON.parse(jsonArray[i].caseReason);
          this.caseData.push(jsonArray[i]);
        }
      })
      .catch((error) => {
        console.log(error);
      });
  },
  requestNum(type) {

  },
}
}
</script>
<style scoped>
.container {
  background-color: #f2f2f2;
}

</style>
