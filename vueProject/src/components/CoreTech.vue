<template>
    <div class="component">
        <div class="line">核心技术</div>
        <div class="block-container">
            <Ctcomponent/>
            <Ctcomponent/>
            <Ctcomponent/>
        </div>

    </div>
</template>
<script>
import Ctcomponent from './Ctcomponent.vue'
export default{
  components: {
    Ctcomponent
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
    width: 100%;
}
.block-container{
    display: flex;
    justify-content: space-between;
}
</style>
