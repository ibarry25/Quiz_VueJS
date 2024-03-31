<template>
  <div class="bg">
    <Questionnaires></Questionnaires>
  </div>
</template>

<script>
import Questionnaires from './components/Questionnaires.vue'
// import Questions from './components/Questions.vue'


export default {
  components: {
    Questionnaires,
    // Questions
  },
  data() {
    return {
      questionnaires: []
    }
  },
  mounted() {
  }
}
</script>
