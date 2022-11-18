/* Write a program that asks the user for numbers until he gives zero.
The given numbers are printed in the console from the largest to the smallest. */

numberList = []
let number = prompt("enter number")

numberList.push(number)
while (number!=="0")  {
  number = prompt("Enter number")
  // let number = parseInt(number)
  numberList.push(number)

}
console.log(numberList)