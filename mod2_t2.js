/* Write a program that asks the user for the number of participants.
After this, the program asks for the names of all participants.
Finally, the program prints the names of the participants
 on the web page in an ordered list (<ol>) in alphabetical order.*/


let PromtNumber = prompt("Enter number")
let NumberOfPar = parseInt(PromtNumber)

let par = []
for (let i = 0; i <NumberOfPar; i++) {
  let names = prompt("Enter name ")
  par.push(names)
}
console.log(par)
par.sort()
console.log(par)

let newL = []
newL.push(par)
for (let i = 1; i < NumberOfPar+1; i++) {
  document.querySelector("#listOfNames" + i).innerHTML = i + ". " + par[0]
  par.shift()

}

