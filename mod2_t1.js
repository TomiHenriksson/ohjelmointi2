/* Write a program that prompts the user for five numbers and prints them in the reverse order they were entered.
Print the result to the console.(2p)
Save the numbers to an array, then use for-loop to iterate in reverse order.
Do not use array.reverse() function. */
let promt_numbers = []



for (let i=1 ; i<6; i++){
  let PromtNumber = prompt(i +". Enter a number")
  let promtnumber = parseInt(PromtNumber)
  promt_numbers.push(promtnumber)
}
for (let i=0 ; i<5; i++){
  let LastNumber = promt_numbers.slice(-1)
  console.log(LastNumber)
  promt_numbers.pop()

}




