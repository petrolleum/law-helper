<template>
    <div class="all">
        <div class="title">法条预测</div>
        <div class="search-box">
            <div class="tip">
              <span>输入案情描述部分</span>
              <span style="color: deepskyblue;">换一段案情描述</span>
            </div>
            <textarea rows="20" cols="100" v-model="description"></textarea>
            <br/>
            <div><button>开始预测</button></div>
        </div>
    </div>
</template>
<script>
export default {
  data () {
    return {
      description: ''
    }
  }
}
</script>
<style scoped>

.all{
  text-align: center;
}
.title{
  font-size: 20px;
  font-weight: bold;
}
.search-box{
}
.search-box>textarea{
  padding-bottom: 20px;
}
.tip{
  padding-bottom: 20px;
}
.search-box>div{
  padding-top: 30px;
}
.search-box>div>button{
  background-color: deepskyblue;
  border-radius: 10px;
  border: 10px lightgray;
  font-weight: bold;
  color: white;
  height: 50px;
  width: 100px;
}
</style>
