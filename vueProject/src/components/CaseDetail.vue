<template>
  <div v-if="this.haveData==1">
    <div class="title">{{ caseTitle }}</div>
    <div class="detail">
      <div class="detail-inline" style="padding-left: 0px">{{ caseId }}</div>
      <div class="detail-inline">{{ court }}</div>
      <div class="detail-inline">{{ judgementTime }}</div>
      <div class="detail-inline">{{ caseType }}</div>
      <div class="detail-inline">{{ proceeding }}</div>
    </div>
    <div class="reason">
      <div class="reason-inline">案由：</div>
      <div class="reason-inline" v-for="item in this.reason">{{ item }}</div>
    </div>
    <div class="content">{{content}}</div>
    <div class="reference" v-for="item in this.reference">
      <div class="reference-inline">法条依据：</div>
      <div class="reference-inline">{{ item }}</div>
    </div>
  </div>
</template>
<script>
import axios from 'axios';
import { requestUrl } from '@/globalVar';
export default {
  mounted() {
    this.id=Number(this.$route.params.id);
    console.log(this.id);
    this.getJudgement(this.id);
  },
  data() {
    return {
        id:0,
        caseTitle:"",
        caseId:"",
        court:"",
        judgementTime:"",
        caseType:"",
        proceeding:"",
        reason:[],
        reference:[],
        content:"",
        haveData:0
    };
  },
  methods: {
    getJudgement(id) {
      console.log(this.id);
      var requestParam = {
        id:this.id
      };
      axios
        .post(requestUrl + "/getJudgement/", requestParam)
        .then((response) => {
          
          const responseData=response.data;
          console.log(responseData);
          this.id=responseData.id;
          this.caseTitle=responseData.caseTitle;
          this.caseId=responseData.caseId;
          this.court=responseData.court;
          this.judgementTime=responseData.judgementTime;
          this.caseType=responseData.caseType;
          this.proceeding=responseData.proceeding;
          this.reference=JSON.parse(responseData.reference);
          this.reason=JSON.parse(responseData.caseReason);
          this.content=responseData.content
          this.haveData=1;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
<style></style>
