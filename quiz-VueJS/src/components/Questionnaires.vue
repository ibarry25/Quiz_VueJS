<template>
  <div class="rect titre">
    <h1>{{ title }}</h1>
  </div>
  <div class="questionnaire">
    <div class="rect quizz">
      <ol class="list-quiz">
        <h3>Vos Quizzes</h3>
        <li v-for="(questionnaire, index) in questionnaires" :key="index">
          <button :id="'quiz_' + questionnaire.quiz_id" @click="afficherQuestions(questionnaire.quiz_id)" :class="{ 'choose-quiz': true, 'selectionner': currentQuestionnaire.quiz_id === questionnaire.quiz_id }"><span>{{ questionnaire.name }}</span></button>
          <div>
            <button @click="modifierQuestionnaire(questionnaire.quiz_id)">Modifier</button>
            <button @click="deleteQuestionnaire(questionnaire.quiz_id)">Supprimer</button>
          </div>
        </li>
      </ol>
      <div id="new-quiz">
        <!-- <input type="text" v-model="newQuestionnaireName">
        <button @click="createQuestionnaire">Ajouter questionnaire</button> -->
      </div>
      <div id="error"></div>
      <button class="choose-quiz" @click="createQuiz">Ajouter Quiz</button>

    </div>
    <div class="rect question">
      <Questions :quizId="currentQuestionnaire.quiz_id " :lesQuestion="currentQuestionnaire.questions"></Questions>
    </div>
  </div>
</template>

<script>

import Questions from './Questions.vue';

const requete = "http://127.0.0.1:5000/quiz/api/v1.0/quiz";

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
    }
  },
  mounted() {
    this.getAllQuestionnaires();
  },
  methods: {
    createQuiz() {
      document.getElementById('new-quiz').innerHTML = `
        <input type="text" id="new-quiz-text">
        <button id="add-quiz">Ajouter</button>`;

      document.getElementById('add-quiz').addEventListener('click', () => {
        const newQuizText = document.getElementById('new-quiz-text').value;
        if (!newQuizText) {
          document.getElementById('error').innerHTML = 'Veuillez saisir un nom de questionnaire';
          return;
        }
        this.newQuestionnaireName = newQuizText;
        this.createQuestionnaire();
      });
    },
    async afficherQuestions(quizId) {
      this.currentQuestionnaire = this.questionnaires.find(questionnaire => questionnaire.quiz_id === quizId);
      console.log(this.currentQuestionnaire);
      // Ajouter en dessous des boutons pour supprimer, ou modifier le nom du questionnaire
      document.getElementById('error').innerHTML = '';
    },
    async getAllQuestionnaires() {
      await fetch(requete)
        .then(response => {
          if (response.ok) return response.json();
          else throw new Error('Request failed! : ', response.status);
        })
        .then(data => {
          this.questionnaires = data;
          if (this.questionnaires.length > 0) {
            this.currentQuestionnaire = this.questionnaires[0];
          }
      }).catch(this.onerror);
    },
    onerror(err) {
      document.getElementById('error').innerHTML = err;
    },
    async createQuestionnaire() {
      if (this.newQuestionnaireName.trim() !== '') {
        fetch(requete, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            name: this.newQuestionnaireName
          })
        })
        .then(response => {
          if (response.ok) {
            this.newQuestionnaireName = '';
            return this.getAllQuestionnaires();
          } else {
            throw new Error('Erreur lors de la création du questionnaire');
          }
        })
        .catch(error => {
          this.onerror(error.message);
        });
      }
    },
    async deleteQuestionnaire(questionnaireId) {
      fetch(`http://127.0.0.1:5000/quiz/api/v1.0/quiz/${questionnaireId}`, {
        method: 'DELETE'
      })
      .then(response => {
        if (response.ok) {
          this.newQuestionnaireName = '';
          return this.getAllQuestionnaires();
        } else {
          throw new Error('Erreur lors de la suppression du questionnaire');
        }
      }).catch(error => {
        this.onerror(error.message);
      });
    },
    modifierQuestionnaire(questionnaireId) {

      document.getElementById('new-quiz').innerHTML = `
        <input type="text" id="new-quiz-text">
        <button id="add-quiz">Modifier</button>`;
      document.getElementById('add-quiz').addEventListener('click', () => {
        const newQuizText = document.getElementById('new-quiz-text').value;
        if (!newQuizText) {
          document.getElementById('error').innerHTML = 'Veuillez saisir un nom de questionnaire';
          return;
        }
        fetch(requete + '/' + questionnaireId, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            name: newQuizText
          })
        })
        .then(response => {
          if (response.ok) {
            this.newQuestionnaireName = '';
            return this.getAllQuestionnaires();
          } else {
            throw new Error('Erreur lors de la modification du questionnaire');
          }
        });
      });
    }
  }
}
</script>
