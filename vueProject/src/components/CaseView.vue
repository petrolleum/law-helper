<template>
  <div>
    <div v-if="this.haveData">
      <div v-for="item in factData" :key="content">
        <CaseViewComponent
          :content="item.content"
          :relevant_articles="item.relevant_articles"
          :accusation="item.deAccusation"
          :punish_of_money="item.punish_of_money"
          :term_of_imprisonment="item.term_of_imprisonment"
        />
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import CaseViewComponent from "./CaseViewComponent.vue";
import { requestUrl } from "@/globalVar";
export default {
  components: {
    CaseViewComponent,
  },
  mounted() {
    this.searchContent = this.$route.params.param;
    this.search(this.searchContent);
  },
  data() {
    return {
      searchContent: "",
      factData: [],
      haveData: false,
    };
  },
  methods: {
    search(factContent) {
      var requestParam = { fact_content: factContent };
      axios
        .post(requestUrl + "/getFactByKeyWord/", requestParam)
        .then((response) => {
          const responseData = response.data.fact;
          const jsonArray = JSON.parse(responseData);
          for (var i = 0; i < jsonArray.length; i++) {
            jsonArray[i].deAccusation=[];
            jsonArray[i].accusation = JSON.parse(jsonArray[i].accusation);
            jsonArray[i].relevant_articles=JSON.parse(jsonArray[i].relevant_articles);
            for (let j = 0; j < jsonArray[i].accusation.length; j++) {
              console.log(jsonArray[i].accusation[j]);
              const decodedString = unescape(jsonArray[i].accusation[j]);
              console.log(decodedString);
              jsonArray[i].deAccusation.push(decodedString);
              console.log(jsonArray[i].deAccusation[j]);
            }
            this.factData.push(jsonArray[i]);
          }
          this.haveData = true;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
<style></style>
