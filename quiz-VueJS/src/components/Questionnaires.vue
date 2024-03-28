<script>
import QuestionItem from './Questions.vue'
// import HelloWorld from './components/HelloWorld.vue'
let data = {
  name: "",  
  questions: [],
}

export default {
    props: {
    quest: Object,
    key: Number
  },
  data() {
    return data;
  },
  methods: {
    add: function () {
      if (this.tmpLOL != "" && this.questions.length < 10) {
        this.questions.push({ text: this.tmpLOL, checked: false });
        this.tmpLOL = "";
      }
    },
    remove($event){
        console.log();
      this.questions.splice(this.questions.indexOf($event.question),1)
    }
  },
  components: {
    QuestionItem
  },
  mounted(){
    fetch('http://127.0.0.1:5000/quiz/api/v1.0/quiz/1')
      .then(response => response.json())
      .then(json => {
        this.name = json.name
        this.questions = json.questions;
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
      <h3>{{ this.name }}</h3>
    <ol>
      <QuestionItem v-for="item in this.questions" :question="item" :key="item.id" @sup="remove"></QuestionItem>
    </ol>
  </div>
    <span class="input-group-btn">
      <input type="text" v-model="tmpLOL" @keyup.enter="add">
      <button @click="add" class="btn btn-success" type="button">Ajouter</button>
    </span>
</template>