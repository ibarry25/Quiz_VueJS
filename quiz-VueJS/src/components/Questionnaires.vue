<template>
  <div>
    <h3>{{ title }}</h3>
    <ol>
      <li v-for="(questionnaire, index) in questionnaires" :key="index">
        {{ questionnaire.name }}
        <button @click="deleteQuestionnaire(questionnaire.id)">Supprimer</button>
      </li>
    </ol>
    <div>
      <input type="text" v-model="newQuestionnaireName">
      <button @click="createQuestionnaire">Ajouter questionnaire</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      title: "Questionnaires",
      questionnaires: [],
      newQuestionnaireName: ''
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
    }
  }
}
</script>
