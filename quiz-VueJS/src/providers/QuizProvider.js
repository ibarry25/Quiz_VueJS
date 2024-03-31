export default class QuizProvider  {

    static testS(task){
      console.log(JSON.stringify(task));
    }

    static async getAllQuestionnaires() {
      try {
        const requete = "http://127.0.0.1:5000/quiz/api/v1.0/quiz";
        fetch(requete)
        .then(response => {
          if (response.ok) return response.json();
          else throw new Error('Request failed! : ', response.status);
        }).then(this.testS)
        // console.log('Erreur HTTP: ' + rep.status)
      } catch (error) {
        console.log('Erreur HTTP: ' + error)
      }

    }





}