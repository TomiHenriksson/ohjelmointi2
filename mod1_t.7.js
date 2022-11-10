
// t.7
/* Write a program that asks the user for the number of dice rolls.
The program throws all the dice once and prints the sum of the numbers. (2p) */

const dice_results = []
let number_of_dices = prompt("Enter how many dices you want to plat whit!")
let number_of_dice_int = parseInt(number_of_dices)
for (let i=-1 ; i<number_of_dices; i++){
  let dice = Math.floor(Math.random() *6);

  // dice_results.push(dice)
}