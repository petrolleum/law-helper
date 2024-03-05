<template>
  <div v-if="this.haveData == 1" style="text-align: center;background-color: #f2f2f2;">
    <div style="display: inline-block ;width: 50%;background-color: white;">
      <div class="title">{{ caseTitle }}</div>
      <div class="details">
        <div class="detail" style="padding-left: 0px">案号：{{ caseId }}</div>
        <div class="detail">法院：{{ court }}</div>
        <div class="detail">判决时间：{{ judgementTime }}</div>
        <div class="detail">案件类型：{{ caseType }}</div>
        <div class="detail">审理流程：{{ proceeding }}</div>
        <div class="detail">
          <div class="detail-inline">案由：</div>
          <div class="detail-inline" v-for="item in this.reason">
            {{ item }}
          </div>
        </div>
      </div>
      <div class="detail" style="padding-top: 20px">正文如下：</div>
      <p class="content">
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{ content }}
      </p>
      <div class="judge">审判长：{{judge}}</div>
      <div class="reference" v-for="item in this.reference">
        <div class="reference-inline">法条依据：</div>
        <div class="reference-inline">{{ item }}</div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import { requestUrl } from "@/globalVar";
export default {
  mounted() {
    this.id = Number(this.$route.params.id);
    console.log(this.id);
    this.getJudgement(this.id);
  },
  data() {
    return {
      id: 0,
      caseTitle: "",
      caseId: "",
      court: "",
      judgementTime: "",
      caseType: "",
      proceeding: "",
      reason: [],
      reference: [],
      content: "",
      judge:"",
      haveData: 0,
    };
  },
  methods: {
    getJudgement(id) {
      console.log(this.id);
      var requestParam = {
        id: this.id,
      };
      axios
        .post(requestUrl + "/getJudgement/", requestParam)
        .then((response) => {
          const responseData = response.data;
          console.log(responseData);
          this.id = responseData.id;
          this.caseTitle = responseData.caseTitle;
          this.caseId = responseData.caseId;
          this.court = responseData.court;
          this.judgementTime = responseData.judgementTime;
          this.caseType = responseData.caseType;
          this.proceeding = responseData.proceeding;
          this.reference = JSON.parse(responseData.reference);
          this.reason = JSON.parse(responseData.caseReason);
          this.content = responseData.content;
          this.judge=responseData.judge;
          this.haveData = 1;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
<style>
.title {
  text-align: center;
  font-size: 30px;
  font-weight: bold;
}
.details {
  display: flex;
  flex-direction: column;
  gap: 20px;
}
.detail {
  font-size: 20px;
}
.detail-inline {
  display: inline-block;
}
.content {
  font-size: 20px;
}
</style>
