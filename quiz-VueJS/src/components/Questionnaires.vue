<template>
  <div>
    <h2>Liste des questionnaires</h2>
    <ul>
      <li v-for="questionnaire in questionnaires" :key="questionnaire.id">
        {{ questionnaire.name }}
        <button @click="deleteQuestionnaire(questionnaire.id)">Supprimer</button>
      </li>
    </ul>
    <form @submit.prevent="createQuestionnaire">
      <input type="text" v-model="newQuestionnaireName" placeholder="Nom du questionnaire" required>
      <button type="submit">Ajouter</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      questionnaires: [],
      newQuestionnaireName: ''
    };
  },
  mounted() {
    this.fetchQuestionnaires();
  },
  methods: {
    async fetchQuestionnaires() {
      try {
        const response = await axios.get('/quiz/api/v1.0/quiz');
        this.questionnaires = response.data;
      } catch (error) {
        console.error('Erreur lors de la récupération des questionnaires', error);
      }
    },
    async createQuestionnaire() {
      try {
        await axios.post('/quiz/api/v1.0/quiz', { name: this.newQuestionnaireName });
        this.newQuestionnaireName = '';
        this.fetchQuestionnaires();
      } catch (error) {
        console.error('Erreur lors de la création du questionnaire', error);
      }
    },
    async deleteQuestionnaire(questionnaireId) {
      try {
        await axios.delete(`/quiz/api/v1.0/quiz/${questionnaireId}`);
        this.fetchQuestionnaires();
      } catch (error) {
        console.error('Erreur lors de la suppression du questionnaire', error);
      }
    }
  }
}
</script>
