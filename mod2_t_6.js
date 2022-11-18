function rolldice (numberofdice) {
  return Math.ceil(Math.random() * numberofdice);
}
function playDiceGame() {
  const results = document.getElementById("results");
  const ulElem = document.createElement("ul");
  results.append(ulElem);
  let diceValue = -1;
  while (diceValue != 6) {
    diceValue = rolldice(6);
    console.log(diceValue);
    const liElem = document.createElement("li");
    liElem.innerText = "Heiton tulos: " +  diceValue;
    ulElem.append(liElem);


  }
}
playDiceGame()


