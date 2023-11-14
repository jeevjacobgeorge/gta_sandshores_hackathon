let no = 0.0;

function showQuestion(nextQuestion, currentQuestion, answer) {
  no = no + answer;
  const current = document.getElementById('question' + currentQuestion);
  current.style.display = 'none'; // Hide current question
    
  const next = document.getElementById('question' + nextQuestion);
  next.style.display = 'block'; // Show next question
}
function showlast(answer){
  no = no + answer; 
  let result = no / 14;
  result *= 10;
  let url = "/submitmq/" + result.toFixed(1);
  window.location.href = url;
}
document.getElementById('quiz-form').addEventListener('submit', function(e) {
  e.preventDefault();

  const result = document.getElementById('result');
  //result.innerHTML = `Thanks for completing the quiz!`;
  result.style.display = 'block';
});
