<template>
<div class="component-pf" @click="changeUrl">
    <span class="inline">
        <img :src="this.img_url" alt="Image">
    </span>
    <span class="inline">
        <div class="name-div">{{this.name}}</div>
        <div class="des-div">{{this.description}}</div>
    </span>
</div>
</template>
<script>
export default{
  props: {
    name:{
      type:String,
      required:true
    },
    description:{
      type:String,
      required:true
    },
    path:{
      type:String,
      required:true
    },
    img_url:{
      type:String,
      
    }
  },
  methods: {
    changeUrl () {
      this.$router.push(this.path)
      console.log(1)
    }
  }
}

</script>
<style>
.inline{
  display: inline-block;
}
.component-pf{
    cursor: pointer;
    display: inline-flex;
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
