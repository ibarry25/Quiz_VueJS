<template>
  <div>
    <h3>Questions</h3>
    <ul id="lst-quest">
      <li v-for="question in questions" :key="question.id">
        {{ question.title }}
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
      request : 'http://127.0.0.1:5000/quiz/api/v1.0/question/'
    };
  },
  mounted() {
    this.getAllQuestion();
  },
  watch: {
    quizId(newQuizId) {

      this.getAllQuestion();
      this.afficherQuestions();
    }
  },
  methods: {
    afficherQuestions() {
      document.getElementById('lst-quest').innerHTML = '';
      this.lesQuestion.forEach(question => {
        document.getElementById('lst-quest').innerHTML += '<li>' + question.title + '</li>';
      });
    },
    createQuestion() {
      document.getElementById('new-quest').innerHTML = '\
        <input type="text" id="new-quest-text">\
        <button id="add-quest"  >Ajouter</button>';

      document.getElementById('add-quest').addEventListener('click', () => {
        const newQuestionText = document.getElementById('new-quest-text').value;
        if (!newQuestionText) {
          document.getElementById('error-quiz').innerHTML = 'Veuillez saisir une question';
          return;
        }
        
        fetch(this.request, {
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
            return response.json();
          } else {
            throw new Error('Request failed! : ', response.status);
          }
        }).then(data => {
          this.getAllQuestion();
          document.getElementById('new-quest').innerHTML = '';
          document.getElementById('error-quiz').innerHTML = '';
        }).catch(error => {
          document.getElementById('error-quiz').innerHTML = error;

      });

    }); 


    },
    getAllQuestion(){
      fetch(this.request)
      .then(response => {
        if (response.ok) return response.json();
        else throw new Error('Request failed! : ', response.status);
      }).then(data => {
        console.log(data);
        this.questions = data;
      }).catch(error => {
        document.getElementById('error-quiz').innerHTML = error;
      });

    }
  }
};
</script>