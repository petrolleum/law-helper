<script >
import HelloWorld from './components/HelloWorld.vue'
import Head from './components/Head.vue'
import HeadSecond from './components/HeadSecond.vue'
import ProductFunction from './components/ProductFunction.vue'
import CoreTech from './components/CoreTech.vue'
import { RouterLink,RouterView } from 'vue-router'
import axios from 'axios'
import { requestUrl } from './globalVar'
export default{
  components: {
    HelloWorld,
    Head,
    HeadSecond,
    ProductFunction,
    CoreTech
  },
  methods:{
    pt(){
      axios.post(requestUrl+"/images/getText").then(response => {
        // 获取响应的数据
        const responseData = response.data;
        // 格式化显示大段文字
        this.formattedTextBlocks = this.formatText(responseData.body);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
    }
  }
}

</script>
<template>
  <button @click="pt"></button>
  <div class="contained-app">
    <Head/>
    <HeadSecond/>
    <RouterView>
    </RouterView>
  </div>
</template>
