<template>
  <div class="rect titre">
    <h1>{{ title }}</h1>
  </div>
    <div class="questionnaire">
      <div class="rect quizz">
      <ol class="list-quiz">
        <h3>Vos Quizzes</h3>
        <li v-for="(questionnaire, index) in questionnaires" :key="index">
          <button :id=questionnaire.quiz_id  @click="afficherQuestions(questionnaire.quiz_id)" class="choose-quiz"><span>{{ questionnaire.name }}</span></button>
          <!-- <button @click="deleteQuestionnaire(questionnaire.id)">Supprimer</button> -->
        </li>
      </ol>
      <div>
        <input type="text" v-model="newQuestionnaireName">
        <button @click="createQuestionnaire">Ajouter questionnaire</button>
      </div>
      <div id="error"></div>
    </div>
    <div class="rect question">
      <Questions :quizId="currentQuestionnaire.quiz_id " :lesQuestion="currentQuestionnaire.questions"></Questions>
    </div>
  </div>
</template>

<script>

import Questions from './Questions.vue';


export default {
  components: {
    Questions
  },
  data() {
    return {
      title: "Questionnaires",
      questionnaires: [],
      newQuestionnaireName: '',
      currentQuestionnaire: { quiz_id: -1, questions: []},
      // espaceQuest : new Questions(-1, [])
    }
  },
  mounted() {
    this.getAllQuestionnaires();
  },
  methods: {
     getAllQuestionnaires() {
      const requete = "http://127.0.0.1:5000/quiz/api/v1.0/quiz";
        fetch(requete)
        .then(response => {
          if (response.ok) return response.json();
          else throw new Error('Request failed! : ', response.status);
        }).then(this.testS)
        .catch(this.onerror);
    },
    testS(data) {
      console.log(data)
      this.questionnaires = data;
      if (this.questionnaires.length > 0) {
        this.currentQuestionnaire = this.questionnaires[0];
      }
    },
    onerror(err) {
        // afficher l'erreur sur la div error
        document.getElementById('error').innerHTML = err;
    },
    createQuestionnaire() {
      if (this.newQuestionnaireName.trim() !== '') {
        fetch('http://127.0.0.1:5000/quiz/api/v1.0/quiz', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ name: this.newQuestionnaireName })
        })
        .then(response => response.json())
        .then(data => {
          this.questionnaires.push(data);
          this.newQuestionnaireName = '';
        });
      }
    },
    deleteQuestionnaire(questionnaireId) {
      fetch(`http://127.0.0.1:5000/quiz/api/v1.0/quiz/${questionnaireId}`, {
        method: 'DELETE'
      })
      .then(response => response.json())
      .then(() => {
        this.questionnaires = this.questionnaires.filter(item => item.id !== questionnaireId);
      });
    },
    afficherQuestions(questionnaireId) {


    this.currentQuestionnaire = this.questionnaires.find(questionnaire => questionnaire.quiz_id === questionnaireId);
    console.log('currentQuestionnaire:', this.currentQuestionnaire);
    
    for (let i = 0; i < this.questionnaires.length; i++) {
      document.getElementById(this.questionnaires[i].quiz_id).classList.remove('selectionner');
    }
    document.getElementById(this.currentQuestionnaire.quiz_id).classList.add('selectionner');



  }

  }
}
</script>
