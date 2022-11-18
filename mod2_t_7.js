function rolldice (numberofdice) {
  return Math.ceil(Math.random() * numberofdice);
}
function playDiceGame(numberOfSide) {
  const results = document.getElementById("results");
  const ulElem = document.createElement("ul");
  results.append(ulElem);
  let diceValue = -1;
  while (diceValue != numberOfSide) {
    diceValue = rolldice(numberOfSide);
    console.log(diceValue);
    const liElem = document.createElement("li");
    liElem.innerText = "Heiton tulos: " +  diceValue;
    ulElem.append(liElem);


  }
}
const diceSides = prompt("Nopan silmälukujen lukumaara")
playDiceGame(diceSides)


