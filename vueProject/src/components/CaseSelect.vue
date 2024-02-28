<template>
  <div>
    <CaseViewComponent
    
    />
    <!-- <div v-if="this.haveData">
      <div v-for="item in caseData" :key="content">
        <CaseViewComponent
          :content="item.content"
          :relevant_articles="item.relevant_articles"
          :accusation="item.deAccusation"
          :punish_of_money="item.punish_of_money"
          :term_of_imprisonment="item.term_of_imprisonment"
        />
      </div>
    </div> -->
  </div>
</template>
<script>
import axios from "axios";
import CaseViewComponent from "./CaseViewComponent.vue";
import { requestUrl } from "@/globalVar";
import CaseSearch from "./CaseSearch.vue";

export default {
  components: {
    CaseViewComponent,
    CaseSearch,
},
  props: {
    caseType: {
      type: Number,
      required: true,
    },
    searchContent: {
      type: String,
    },
    curPage:{
        type:Number
    },
  },
  mounted(){
    // this.requestCase(1,1);
  },
  watch:{
    caseType(newValue,oldValue){
        this.requestCase(this.caseType,1);
    },
    searchContent(newValue,oldValue){
        this.search(this.searchContent,1);
    },
    curPage(newValue,oldValue){
        if(caseType==0){
            this.search(this.searchContent,this.curPage);
        }else{
            this.requestCase(this.caseType,this.curPage);
        }
    }
  },
  data() {
    return {
      caseData: [],
      haveData: false,
    };
  },
  methods: {
    search(factContent,page) {
      var requestParam = { fact_content: caseContent };
      axios
        .post(requestUrl + "/getFactByKeyWord/", requestParam)
        .then((response) => {
          const responseData = response.data.fact;
          const jsonArray = JSON.parse(responseData);
          for (var i = 0; i < jsonArray.length; i++) {
            jsonArray[i].deAccusation = [];
            jsonArray[i].accusation = JSON.parse(jsonArray[i].accusation);
            jsonArray[i].relevant_articles = JSON.parse(
              jsonArray[i].relevant_articles
            );
            for (let j = 0; j < jsonArray[i].accusation.length; j++) {
              console.log(jsonArray[i].accusation[j]);
              const decodedString = unescape(jsonArray[i].accusation[j]);
              console.log(decodedString);
              jsonArray[i].deAccusation.push(decodedString);
              console.log(jsonArray[i].deAccusation[j]);
            }
            this.factData.push(jsonArray[i]);
          }
          this.haveData = true;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  requestCase(type,page){

  },
  requestNum(type){

  }
};
</script>
<style></style>
