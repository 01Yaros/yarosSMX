// genera el numero 1-10
var number = Math.floor(Math.random() * 10) + 1;
// comprova si es correcte el numero
function checkGuess() {
  var guess = document.getElementById("guessInput").value;
  if (guess == number) {
    alert("¡Adivinaste!");
  } else if (guess < number) {
    alert("masa petit");
  } else {
    alert("masa gran");
  }
}
