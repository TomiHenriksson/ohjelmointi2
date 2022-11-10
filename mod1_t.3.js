
// t.3
/* Write a program that prompts for three integers.
The program prints the sum, product and average of the numbers to the HTML document. */

let ask_int1 = prompt("Enter number")
let ask_int01 = parseInt(ask_int1)
let ask_int2 = prompt("Enter number")
let ask_int02 = parseInt(ask_int2)
let ask_int3 = prompt("Enter number")
let ask_int03 = parseInt(ask_int3)

let sum_of_ints = ask_int01 + ask_int02 + ask_int03
let product_of_ints = ask_int01 * ask_int02 * ask_int03
let avarage_of_ints = (ask_int01 + ask_int02 + ask_int03)/3

document.querySelector("#p1").innerHTML ="Sum is: " + sum_of_ints
document.querySelector("#p2").innerHTML ="Product of ints: " + product_of_ints
document.querySelector("#p3").innerHTML = "Avarage of ints: " + avarage_of_ints

