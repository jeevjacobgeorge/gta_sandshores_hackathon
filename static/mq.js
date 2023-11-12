const answers = [];

function showQuestion(nextQuestion, currentQuestion, answer) {
  answers.push(answer);
  const current = document.getElementById('question' + currentQuestion);
  current.style.display = 'none'; // Hide current question

  const next = document.getElementById('question' + nextQuestion);
  next.style.display = 'block'; // Show next question
}
function showlast(){
  window.location.href = "/submitmq";
}
document.getElementById('quiz-form').addEventListener('submit', function(e) {
  e.preventDefault();

  const result = document.getElementById('result');
  //result.innerHTML = `Thanks for completing the quiz!`;
  result.style.display = 'block';
});
