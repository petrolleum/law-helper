<template>
  <div class="all" @click="toDetail()">
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
      <div class="reason-inline" v-for="item in reason">{{item}}</div>
    </div>
    <div class="reference" v-for="item in reference">
      <div class="reference-inline">法条依据：</div>
          <div class="reference-inline">{{ item }}</div>
    </div>
  </div>
</template>
<script scoped>
export default {
  props: {
    id: {
      type: Number,
    },
    caseTitle: {
      type: String,
    },
    caseId: {
      type: String,
    },
    court: {
      type: String,
    },
    religion: {
      type: String,
    },
    caseType: {
      type: String,
    },
    proceeding: {
      type: String,
    },
    reason: {
      type: Array,
    },
    reference: {
      type: Array,
    },
    judgementTime:{
      type:String
    },

  },
  methods:{
    toDetail(){
      this.$router.push('/detail/'+this.id.toString());
    }
  }
};
</script>
<style scoped>
.all {
  display: flex;
  flex-direction: column;
  gap: 10px;
  align-items: flex-start;
  border: 1px black;
  padding-top: 30px;
  padding-bottom: 30px;
  background-color: white;
  border-radius: 30px;
  cursor: pointer;
}
.title {
  font-weight: bold;
}
/* .detail{
  display: flex;
} */
.detail-inline {
  display: inline-block;
  padding-left: 20px;
  padding-right: 20px;
  border-right: 1px solid black;
}
.reason {
  display: flex;
  justify-content: flex-start;
  gap: 20px;
}
.reason-inline {
  display: inline-block;
  background-color: lightblue;
}
.reference {

}
.reference-inline {
  display: inline-block;
  background-color: lightblue;
}
</style>
