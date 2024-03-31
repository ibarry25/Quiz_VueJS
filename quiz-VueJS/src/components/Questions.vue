<template>
  <div>
    <h2>Liste des questions</h2>
    <ul>
      <li v-for="question in questions" :key="question.id">
        {{ question.title }}
        <button @click="deleteQuestion(question.id)">Supprimer</button>
      </li>
    </ul>
    <form @submit.prevent="createQuestion">
      <input type="text" v-model="newQuestionTitle" placeholder="Titre de la question" required>
      <button type="submit">Ajouter</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      questions: [],
      newQuestionTitle: ''
    };
  },
  mounted() {
    this.fetchQuestions();
  },
  methods: {
    async fetchQuestions() {
      try {
        const response = await axios.get('/quiz/api/v1.0/question');
        this.questions = response.data;
      } catch (error) {
        console.error('Erreur lors de la récupération des questions', error);
      }
    },
    async createQuestion() {
      try {
        await axios.post('/quiz/api/v1.0/question', { title: this.newQuestionTitle });
        this.newQuestionTitle = '';
        this.fetchQuestions();
      } catch (error) {
        console.error('Erreur lors de la création de la question', error);
      }
    },
    async deleteQuestion(questionId) {
      try {
        await axios.delete(`/quiz/api/v1.0/question/${questionId}`);
        this.fetchQuestions();
      } catch (error) {
        console.error('Erreur lors de la suppression de la question', error);
      }
    }
  }
}
</script>
