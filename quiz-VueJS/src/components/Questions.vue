<template>
  <div>
    <h4>{{ questionnaire.name }}</h4>
    <ol>
      <li v-for="(question, index) in questionnaire.questions" :key="index">
        {{ question.title }}
        <button @click="deleteQuestion(question.id)">Supprimer</button>
      </li>
    </ol>
    <div>
      <input type="text" v-model="newQuestionTitle">
      <button @click="createQuestion">Ajouter question</button>
    </div>
  </div>
</template>

<script>
export default {
  props: ['quest'],
  data() {
    return {
      questionnaire: this.quest,
      newQuestionTitle: ''
    }
  },
  methods: {
    createQuestion() {
  if (this.newQuestionTitle.trim() !== '') {
    fetch('http://127.0.0.1:5000/quiz/api/v1.0/question', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ title: this.newQuestionTitle, quiz_id: this.questionnaire.id }) // Utilisation de quiz_id au lieu de quizId
    })
    .then(response => response.json())
    .then(data => {
      this.questionnaire.questions.push(data);
      this.newQuestionTitle = '';
    });
  }
},
    deleteQuestion(question_id) {
      fetch(`http://127.0.0.1:5000/quiz/api/v1.0/question/${question_id}`, {
        method: 'DELETE'
      })
      .then(response => response.json())
      .then(() => {
        this.questionnaire.questions = this.questionnaire.questions.filter(item => item.id !== questionId);
      });
    }
  }
}
</script>
