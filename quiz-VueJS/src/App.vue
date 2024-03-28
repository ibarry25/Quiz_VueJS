<script>
import QuestionnaireItem from './components/Questionnaires.vue'
//import HelloWorld from './components/HelloWorld.vue'
let data = {
  questionnaire: [
    {
      id: 1,
      text: "Question 1",
      checked: false,
    },
    {
      id: 2,
      text: "Question 2",
      checked: false,
    },
    {
      id: 3,
      text: "Question 3",
      checked: false,
    }
    
  ],
  title: "Quiz 1",
}

export default {
  data() {
    return data;
  },
  methods: {
    add: function () {
      if (this.tmpLOL != "" && this.questionnaire.length < 10) {
        this.questionnaire.push({ text: this.tmpLOL, checked: false });
        this.tmpLOL = "";
      }
    },
    remove($event){
      this.questionnaire.splice(this.questionnaire.indexOf($event.todo),1)
    }
  },
  components: {
    QuestionnaireItem
  },
  mounted(){
    fetch('http://127.0.0.1:5000/quiz/api/v1.0/quiz')
      .then(response => response.json())
      .then(json => {
        this.questionnaire = json.questionnaires; console.log(this.questionnaire);
      });
  }
}
</script>

<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png" />
    <HelloWorld msg="Hello Vue 3 + Vite" /> -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css"
    integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
  <div id="app" class="container">
    <h2>Quiz</h2>
    <div>
      <QuestionnaireItem v-for="item in questionnaire" :quest="item"  @sup="remove"></QuestionnaireItem>
  </div>
  </div>
</template>