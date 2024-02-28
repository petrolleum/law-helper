<template>
  <div class="all">
    <div>{{caseTitle}}</div>
    <div>
      <div>{{caseId}}</div>
      <div>{{court}}</div>
      <div>{{religion}}</div>
      <div>{{caseType}}</div>
      <div>{{proceeding}}</div>
    </div>
    <div>
      <div>案由：</div>
      <div>{{reason}}</div>
    </div>
    <div>法条依据：</div>
  </div>
</template>
<script>
export default {
  props: {
    id:{
      type:Number
    },
    caseTitle:{
      type:String
    },
    caseId:{
      type:String
    },
    court:{
      type:String
    },
    religion:{
      type:String
    },
    caseType:{
      type:Number
    },
    proceeding:{
      type:String
    },
    reason:{
      type:String
    },
    reference:{
      type:String
    }
  }
};
</script>
<style scoped>
.all{
    padding-top: 20px;
}
.title-inline{
    display: inline-block;
    font-size: 20px;
    font-weight: bold;
}
.inline{
    display: inline-block;
}
.item-inline{
    display: inline-block;
}
</style>
