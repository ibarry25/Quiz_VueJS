<template>
  <div>
    <Questionnaires></Questionnaires>
    <Questions v-for="(questionnaire, index) in questionnaires" :key="index" :quest="questionnaire"></Questions>
  </div>
</template>

<script>
import Questionnaires from './components/Questionnaires.vue'
import Questions from './components/Questions.vue'

export default {
  components: {
    Questionnaires,
    Questions
  },
  data() {
    return {
      questionnaires: []
    }
  },
  mounted() {
    this.getAllQuestionnaires();
  },
  methods: {
    getAllQuestionnaires() {
      fetch('http://127.0.0.1:5000/quiz/api/v1.0/quiz')
        .then(response => response.json())
        .then(data => {
          this.questionnaires = data;
        });
    }
  }
}
</script>
