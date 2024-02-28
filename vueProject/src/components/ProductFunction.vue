
<template>
    <div class="all">
        <div class="line">
            产品功能
        </div>
        <div class="block-container">
            <div>
                <Pfcomponent name="法条预测" description="法条预测是本系统的核心功能，利用自然语言处理和人工智能等现代科学技术搭建推荐模型，
                采用多模型融合的思想，实现法条预测" path="/lp" :img_url="this.logoUrl1"/>
                <Pfcomponent name="法条栏目" description="法条栏目是本系统的辅助功能之一，用于辅助本系统核心功能法条预测，通过文本处理等技术
                对数据进行刑法法条文本数据进行处理" path="/lc" :img_url="this.logoUrl2"/>
            </div>
            <div>
                <Pfcomponent name="案件查询" description="案件查询是本系统的辅助功能，使用BM25算法实现案件的检索，通过关键字检索案件" 
                path="/cv" :img_url="this.logoUrl2"/>
                <Pfcomponent name="统计分析" description="对裁判文书进行数据分析，统计不同的法条在案件中的引用情况，以条形图的形式展现"
                :img_url="this.logoUrl1"/>
            </div>
        </div>
    </div>
</template>
<script>
import { requestUrl } from '@/globalVar';
import Pfcomponent from './Pfcomponent.vue'
export default{
  components: {
    Pfcomponent
  },
  data(){
    return{
        logoUrl1:requestUrl+"/image/2.jpg",
        logoUrl2:requestUrl+"/image/3.jpg"
    }
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
}
.block-container>div{
    text-align: center;
}

</style>
