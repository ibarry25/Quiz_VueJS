<script>
import RepItem from './Reponses.vue'

export default {
  props: {
    question: Object
  },
  data(){
    return {
      modif: false,
      reponses: [],
    }
  },
  methods: {
    supprimer(){
      this.$emit("sup", {question: this.question})
    },
    modifier(){
      this.modif = true;
    },
    sauvegarder(){
      this.modif = false
    },
    supprimerRep($event){
      var cle = Object.keys(this.reponses).find(val => this.reponses[val] === $event.reponse);
      console.log(String(cle));
if (cle) {
  delete this.reponses[cle];
}

    }
  },
  components: {
    RepItem,
  },
  emits : ['sup'],
  mounted(){
    fetch(this.question.url)
      .then(response => response.json())
      .then(json => {
        this.reponses = json.question;
      });
  }
}

</script>

<template>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css"
    integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
  <div class="checkbox">
    <label>
      <input v-if="modif" v-model="question.title" type="text">
      <p v-else>{{ question.title }}</p>
      <button @click="supprimer" class="btn btn-danger">Supprimer</button>
      <button v-if="modif" @click="sauvegarder" class="btn btn-primary">Sauvegarder</button>
      <button v-else @click="modifier" class="btn btn-warning">Modifier</button>
      <RepItem v-for="rep in reponses" :reponse="rep" @sup="supprimerRep"></RepItem>
    </label>
  </div>
</template>


