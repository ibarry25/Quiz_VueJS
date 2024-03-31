function get_all_quiz() {
    fetch('/quiz/api/v1.0/quiz')
        .then((rep) => {
            rep.json()
                .then((json) => console.log(json)); 
        })
}

async function get_all_quiz2() {
    const rep = await fetch('/quiz/api/v1.0/quiz');
    const json = await rep.json();
    console.log(json);
}

async function get_quiz(quiz_id) {
    const rep = await fetch(`/quiz/api/v1.0/quiz/${quiz_id}`);
    const json = await rep.json();
    console.log(json); 
}

async function create_quiz(json) {
    const rep = await fetch('/quiz/api/v1.0/quiz',
        {
            "method": "POST",
            "headers": {
                "Content-Type": "application/json"
            },
            "body": JSON.stringify(json)
        });
    json = await rep.json();
    console.log(json);
}

async function create_question(json) {
    const rep = await fetch('/quiz/api/v1.0/question',
        {
            "method": "POST",
            "headers": {
                "Content-Type": "application/json"
            },
            "body": JSON.stringify(json)
        });
    json = await rep.json();
    console.log(json);
}

async function deleteQuiz(quizId) {
    const rep = await fetch(`/quiz/api/v1.0/quiz/${quizId}`, { method: "DELETE" });
    const json = await rep.json();
    console.log(json);
}

async function deleteQuestion(questionId) {
    const rep = await fetch(`/quiz/api/v1.0/question/${questionId}`, { method: "DELETE" });
    const json = await rep.json();
    console.log(json);
}

async function updateQuiz(quizId, newName) {
    const rep = await fetch(`/quiz/api/v1.0/quiz/${quizId}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ name: newName })
    });
    const json = await rep.json();
    console.log(json);
}

async function updateQuestion(questionId, newTitle) {
    const rep = await fetch(`/quiz/api/v1.0/question/${questionId}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ title: newTitle })
    });
    const json = await rep.json();
    console.log(json);
}



async function get_all_question() {
    const rep = await fetch('/quiz/api/v1.0/question');
    const json = await rep.json();
    console.log(json);
}

async function show_all_quiz(quizs) {
    const div = $("all-quiz");
    div.empty();
    div.append($("<ul>"));
    for (const q of quizs) {
        $("#all-quiz ul")
        .append(
            $("<li>")
            .append($("a"))
                .text(q["name"])
        )
    }
}

get_all_quiz2();

