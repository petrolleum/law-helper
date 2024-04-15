<template>
    <div style="">
        <div class="inline">
            <img :src="this.image_url" alt="Image">
        </div>
        <div class="inline">
            <div>{{this.content}}</div>
        </div>
    </div>
</template>
<script scoped>
export default{
props{
    image_url:{
        type:String,
    },
    content:{
        type:String,
    }
}

}
</script>
<style scoped>
.inline{
display: inline-block;

}
</style>