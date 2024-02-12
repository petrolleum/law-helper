<template>
    <div class="all">
        <div class="title-style">{{this.title}}</div>
        <div class="content-style">{{this.content}}</div>
    </div>
</template>
<script>
export default{
    props:{
        title:{
            type:String,
            required:true
        },
        content:{
            type:String,
            required:true
        }
    },
    data(){
        return{
    
        }
    }
}
</script>
<style scoped>
.all{
    display: flex;
    justify-content: flex-end;
    flex-direction: column;
}
.title-style{
    font-size: 30px;
    font-weight: bold;
    padding-top: 20px;
    padding-bottom: 20px;
}
.content-style{
    font-size: 15px;
    padding-bottom: 20px;
}
</style>