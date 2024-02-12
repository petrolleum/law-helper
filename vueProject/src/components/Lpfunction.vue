<template>
  <div>
    <div class="line">功能介绍</div>
    <div class="block-container">
        <Lpfunctioncomponent name="法条预测" description="通过输入案情文本描述和事实部分，点击预测按钮，实现法条预测"/>
        <Lpfunctioncomponent name="法条查询" description="通过法条预测成功以后，返回预测成功的法条，点击对应的法条可以查询对应法条的信息"/>
        <Lpfunctioncomponent name="相似案件筛选" description="以预测成功的法条为关键字，筛选出引用这些法条的案例"/>
    </div>
  </div>
</template>
<script>
import Lpfunctioncomponent from './Lpfunctioncomponent.vue'
export default{
  components: {
    Lpfunctioncomponent
  }
}
</script>
<style>
.line{
    text-align: center;
    font-size: 20px;
    color: black;
    background-color: white;
    height: 60px;
    font-weight: bold;
}
.block-container{
  text-align: center;
}

</style>
