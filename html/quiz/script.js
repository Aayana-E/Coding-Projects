const quizData = [
    {
        question: "What is the capital of France?",
        a: "Berlin",
        b: "Madrid",
        c: "Paris",
        d: "Rome",
        correct: "c"
    },
    {
        question: "Which language is used to style web pages?",
        a: "HTML",
        b: "CSS",
        c: "JavaScript",
        d: "Python",
        correct: "b"
    },
    {
        question: "What does HTML stand for?",
        a: "Hyperlinks and Text Markup Language",
        b: "Hyper Text Markup Language",
        c: "Home Tool Markup Language",
        d: "Hyper Text Main Language",
        correct: "b"
    }
];

function loadQuiz() {
    const quizContainer = document.getElementById("quiz");
    quizContainer.innerHTML = "";
    quizData.forEach((quizItem, index) => {
        quizContainer.innerHTML += `
            <div class="question">${index + 1}. ${quizItem.question}</div>
            <div class="answer">
                <input type="radio" name="question${index}" value="a"> ${quizItem.a}<br>
                <input type="radio" name="question${index}" value="b"> ${quizItem.b}<br>
                <input type="radio" name="question${index}" value="c"> ${quizItem.c}<br>
                <input type="radio" name="question${index}" value="d"> ${quizItem.d}
            </div>
        `;
    });
}

function submitQuiz() {
    let score = 0;
    quizData.forEach((quizItem, index) => {
        const answer = document.querySelector(`input[name="question${index}"]:checked`);
        if (answer && answer.value === quizItem.correct) {
            score++;
        }
    });
    const result = document.getElementById("result");
    result.innerHTML = `You scored ${score} out of ${quizData.length}`;
}

loadQuiz();
