<script>

export default {
  props: {
    reponse: Object
  },
  data(){
    return {
      modif: false,
      rep: this.reponse
    }
  },
  methods: {
    supprimer(){
      this.$emit("sup", {reponse: this.reponse})
    },
    modifier(){
      this.modif = true;
    },
    sauvegarder(){
      this.modif = false
    }
  },
  emits : ['sup'],
}

</script>

<template>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css"
    integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
  <div class="rep m-5">
    <label>
      <input v-if="modif" v-model="this.rep" type="text">
      <p v-else>{{ this.rep }}</p>
      <button @click="supprimer" class="btn btn-danger">Supprimer</button>
      <button v-if="modif" @click="sauvegarder" class="btn btn-primary">Sauvegarder</button>
      <button v-else @click="modifier" class="btn btn-warning">Modifier</button> 
      </label>
  </div>
</template>


