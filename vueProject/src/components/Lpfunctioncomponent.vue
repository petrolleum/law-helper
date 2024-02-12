<template>
    <div class="component-lp">
        <span>
            <img :src="['img-url']" alt="">
        </span>
        <span>
            <div class="name-div">{{name}}</div>
            <div class="des-div">{{description}}</div>
        </span>
    </div>
    </template>
<script>
export default{
  props: ['name', 'description', 'img-url']
}
</script>
    <style>
    .component-lp{
        display: inline-block;
        padding-right: 20px;
        padding-bottom: 50px;
        width: 200px;
        cursor: pointer;
        padding-left: 20px;
    }
    .name-div{
        font-size: 20px;
        font-weight: bold;
        text-align: left;
    }
    .des-div{
        font-size: 15px;
    }
    </style>
