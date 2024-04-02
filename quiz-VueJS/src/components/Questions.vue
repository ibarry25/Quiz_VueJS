<template>
  <div>
    <h3>Questions</h3>
    <ul id="lst-quest">
      <li v-for="question in questions" :key="question.id">
        <span>{{ question.title }}</span>
        <div>
          <button @click="modifyQuestion(question.id)">Modifier</button>
          <button @click="deleteQuestion(question.id)">Supprimer</button>
        </div>
      </li>
    </ul>
    <div>
      <div id="new-quest"></div>
      <div class="error" id="error-quiz"></div>
      <button class="choose-quiz" @click="createQuestion">Ajouter question</button>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    quizId: {
      type: Number,
      required: true
    },
    lesQuestion: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      questions: [], // Placeholder for the questions data
      request : 'http://127.0.0.1:5000/quiz/api/v1.0/question'
    };
  },
  mounted() {
    this.getAllQuestion();
  },
  watch: {
    quizId(newQuizId) {
      console.log('New quiz id: ', newQuizId);
      this.getAllQuestion();
    }
  },
  methods: {
    createQuestion() {
      document.getElementById('new-quest').innerHTML = `
        <input type="text" id="new-quest-text">
        <button id="add-quest">Ajouter</button>`;

      document.getElementById('add-quest').addEventListener('click', () => {
        const newQuestionText = document.getElementById('new-quest-text').value;
        if (!newQuestionText) {
          document.getElementById('error-quiz').innerHTML = 'Veuillez saisir une question';
          return;
        }
        console.log('New question: ', this.quizId);
        
        fetch(this.request , {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            quiz_id: this.quizId,
            title: newQuestionText
          })
        }).then(response => {
          if (response.ok) {
            console.log('Question added');
            return this.getAllQuestion();
          } else {
            throw new Error('Request failed! : ', response.status);
          }
        }).catch(error => {
          document.getElementById('error-quiz').innerHTML = error;
        });
      }); 
    },
    async getAllQuestion(){
      const request = this.request + '?quiz_id=' + this.quizId;
      console.log('Request: ', request);
      await fetch(request)
      .then(response => {
        if (response.ok) return response.json();
        else throw new Error('Request failed! : ', response.status);
      }).then(data => {
        console.log(data);
        this.questions = data;
      }).catch(error => {
        document.getElementById('error-quiz').innerHTML = error;
      });
    },
    deleteQuestion(idQuestion) {
      fetch(this.request + '/' + idQuestion, {
        method: 'DELETE'
      }).then(response => {
        if (response.ok) {
          return this.getAllQuestion();
        } else {
          throw new Error('Request failed! : ', response.status);
        }
      }).catch(error => {
        document.getElementById('error-quiz').innerHTML = error;
      });
    },
    modifyQuestion(idQuestion) {
      const question = this.questions.find(question => question.id === idQuestion);
      document.getElementById('new-quest').innerHTML = `
        <input type="text" id="new-quest-text" value="${question.title}">
        <button id="modify-quest">Modifier</button>`;

      document.getElementById('modify-quest').addEventListener('click', () => {
        const newQuestionText = document.getElementById('new-quest-text').value;
        if (!newQuestionText) {
          document.getElementById('error-quiz').innerHTML = 'Veuillez saisir une question';
          return;
        }
        
        fetch(this.request + '/'+ idQuestion, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            title: newQuestionText
          })
        }).then(response => {
          if (response.ok) {
            console.log('Question modified');
            return this.getAllQuestion();
          } else {
            throw new Error('Request failed! : ', response.status);
          }
        }).catch(error => {
          document.getElementById('error-quiz').innerHTML = error;
        });
      });
    }
  }
};

</script>
