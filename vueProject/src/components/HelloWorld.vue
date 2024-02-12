
<template>
<div v-bind:id="msg1">
    {{msg1}}
    <button>Button</button>
    <div>你好</div>
    <div>{{$globalVar}}</div>
</div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      msg1: this.$globalVar
    }
  }
}
</script>
