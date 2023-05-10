// genera el número 1-10
var number = Math.floor(Math.random() * 10) + 1;
// comprova si és correcte el numero
function checkGuess() {
  var guess = document.getElementById("guessInput").value;
  if (guess == number) {
    alert("FELIÇITATS, HAS ENDEVINAT EL NÚMERO! TORNEM-HI?");
  } else if (guess < number) {
    alert("El número és massa PETIT");
  } else {
    alert("El número és massa GRAN");
  }
}
