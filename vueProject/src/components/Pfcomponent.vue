<template>
<div class="component-pf" @click="changeUrl">
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
  props: ['name', 'description', 'img-url', 'path'],
  methods: {
    changeUrl () {
      this.$router.push(this.path)
      console.log(1)
    }
  }
}

</script>
<style>
.component-pf{
    cursor: pointer;
    display: inline-block;
    padding-right: 100px;
    padding-bottom: 50px;
    width: 500px;
}
.name-div{
    font-size: 20px;
    font-weight: bold;
}
.des-div{
    font-size: 15px;
}
</style>
