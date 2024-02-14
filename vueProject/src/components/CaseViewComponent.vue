<template>
  <div class="all">
    <div class="title-inline">
        案件详情：
    </div>
    <div>
        {{ content }}
    </div>
  </div>
  <div>
    <div>
      <div>
        <div class="title-inline">罪名：</div>
        <div v-for="item in accusation" class="item-inline">
          {{ item }}
        </div>
      </div>
      <div>
        <div class="inline">
          <div class="title-inline">罚款：</div>
          <div class="item-inline">
            {{ punish_of_money }}
          </div>
        </div>
        <div class="inline" style="padding-left: 30px;">
          <div class="title-inline">刑期：</div>
          <div class="item-inline">{{ term_of_imprisonment }}</div>
        </div>
      </div>
    </div>
    <div>
      <div class="title-inline">相关法条：</div>
      <div v-for="item in relevant_articles" class="item-inline">
        {{ item }}
      </div>
    </div>
  </div>
</template>
<script>
export default {
  props: {
    content: {
      type: String,
      required: true,
    },
    relevant_articles: {
      required: true,
    },
    accusation: {
      required: true,
    },
    punish_of_money: {
      type: String,
      required: true,
    },
    term_of_imprisonment: {},
  },
};
</script>
<style scoped>
.all{
    padding-top: 20px;
}
.title-inline{
    display: inline-block;
    font-size: 20px;
    font-weight: bold;
}
.inline{
    display: inline-block;
}
.item-inline{
    display: inline-block;
}
</style>
