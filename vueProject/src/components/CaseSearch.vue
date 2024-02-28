<template>
  <div class="container">
    <div class="search-box">
      <input
        type="text"
        placeholder="在百度中搜索"
        v-model="searchQuery"
        @keyup.enter="search"
      />
    </div>
    
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchQuery: "",
    };
  },
  methods: {
    search() {
      // 在这里执行搜索操作，可以使用 this.searchQuery 来获取搜索关键词
      console.log("搜索：", this.searchQuery);
      const paramValue = this.searchQuery;
      this.$emit('searchEvent',this.searchQuery);
      this.$router.push({ path: '/caseView/'+paramValue });
    },
  },
};
</script>

<style scoped>
.container{
    display: flex;
    justify-content: center; /* 水平居中 */
  align-items: center; /* 垂直居中 */
  height: 100px; /* 使容器铺满整个视口高度 */
}
.search-box {
  width: 800px; /* 设定搜索框的宽度 */
  margin: 0 auto; /* 水平居中 */
  padding: 20px;
  background-color: #f2f2f2;
  border-radius: 30px; /* 圆角 */
}

.search-box input[type="text"] {
  width: 100%; /* 搜索框铺满整个容器 */
  padding: 10px;
  font-size: 16px;
  border: none;
  border-radius: 30px; /* 圆角 */
  outline: none;
}
</style>
