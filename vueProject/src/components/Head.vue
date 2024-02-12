
<template>
    <div>
        <div class="head-line1">
            <span class="img-span"></span>
            <span>
                <div>法条推荐智能分析</div>
                <div>Intelligent Legal Article Recommendation</div>
            </span>
            <span class="button-span">
                <span class="head-button">产品功能</span>
                <span class="head-button">个人中心</span>
                <span class="head-button" @click="toPf">首页</span>
            </span>
        </div>
    </div>
</template>
<script>
export default{
  methods: {
    toPf () {
      this.$router.push('/pf')
    }
  }
}
</script>
<style scoped>
.head-line1 {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px;
  background-color: black;
  color: #fff;
}

.head-line1 > span {
  margin: 0 10px;
  cursor: pointer;
}
.head-line1 > span > div {
  margin: 0;
  font-size: 14px;
}
.button-span{
    display: flex;
    justify-content: flex-end;
}
.head-button {
  padding: 5px 10px;
  border-radius: 5px;
  cursor: pointer;
  margin-left: auto; /* 将 .head-button 推到容器的右侧 */
}
</style>
