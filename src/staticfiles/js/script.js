document.addEventListener("DOMContentLoaded", function () {
  let formSubmitted = false;
  let questionModal = new bootstrap.Modal(
    document.getElementById("question-modal"),
    {}
  );
  questionModal.show();
  const questions = document.querySelectorAll(".question-container");
  let currentQuestion = 0;
  const modal = document.getElementById("question-modal");
  const questionText = document.getElementById("questionText");
  const answerOptions = document.getElementById("answerOptions");
  const prevButton = document.getElementById("prevQuestion");
  const nextButton = document.getElementById("nextQuestion");

  function showQuestion(index) {
    const question = questions[index];

    questionText.textContent = question.querySelector("h3").textContent;

    answerOptions.innerHTML = "";
    const answers = question.querySelectorAll('input[type="radio"]');
    answers.forEach((answer) => {
      const label = answer.nextElementSibling.textContent;
      const div = document.createElement("div");
      div.innerHTML = `
                    <label class="flex items-center space-x-2 p-2 border rounded cursor-pointer hover:bg-gray-100 list-group list-group-item list-group-item-action rounded-1 my-1 border-1 fs-5">
                        <input type="radio" name="modal_${answer.name}" value="${answer.value}">
                        <span>${label}</span>
                    </label>
                `;
      answerOptions.appendChild(div);
    });

    prevButton.disabled = index === 0;
    nextButton.textContent = index === questions.length - 1 ? "Submit" : "Next";
  }

  showQuestion(0);

  prevButton.addEventListener("click", () => {
    if (currentQuestion > 0) {
      currentQuestion--;
      showQuestion(currentQuestion);
    }
  });

  nextButton.addEventListener("click", () => {
    if (formSubmitted) {
      window.location.href = "/result/";
      return;
    }
    const currentAnswers = modal.querySelectorAll(
      `input[name="modal_${questions[currentQuestion].dataset.questionId}"]`
    );

    const selectedAnswer = Array.from(currentAnswers).find(
      (answer) => answer.checked
    );

    if (!selectedAnswer) {
      alert("Please select an answer before continuing.");
      return;
    }

    const mainFormInput = document.querySelector(
      `input[name="${questions[currentQuestion].dataset.questionId}"][value="${selectedAnswer.value}"]`
    );
    if (mainFormInput) mainFormInput.checked = true;

    if (currentQuestion === questions.length - 1) {
      submitForm();
    } else {
      currentQuestion++;
      showQuestion(currentQuestion);
    }
  });

  function submitForm() {
    const form = document.getElementById("questionnaireForm");
    const formData = new FormData(form);

    fetch("/submit/", {
      method: "POST",
      body: formData,
      headers: {
        "X-Requested-With": "XMLHttpRequest",
      },
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        formSubmitted = true;
        nextButton.textContent = "Show Result";
        prevButton.classList.add("d-none");
      })
      .catch((error) => {
        console.error("Error:", error);
        alert("An error occurred while submitting your responses.");
      });
  }
});
