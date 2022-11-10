
// t.6
/* Write a program that prints the text "Should I calculate the square root?" in a confirmation window.
If the user selects OK, the program asks for the number and calculates and prints its square root
to the HTML document. If the user selects Cancel, the program prints the text:
"The square root is not calculated." to the HTML document (3p)
The confirmation window can be displayed with the function confirm().
The function returns true if the user selects OK. If the user selects Cancel, the function returns false.
You cannot calculate the square root of a negative number.
If the number entered by the user is negative, the program prints:
"The square root of a negative number is not defined" to the HTML document. */


let ask_the_user = confirm("Should I calculate the square root?")
if (ask_the_user == true)  {
  let ask_number = prompt("Enter a number")
  var ask_number_int = parseInt(ask_number) }
else
  document.querySelector("#p6").innerHTML = "The square root is not calculated."


if (ask_number_int >= 0) {
  var ask_number_to_sqr = Math.sqrt(ask_number_int)
  document.querySelector("#p6").innerHTML = "Sqare root of " + ask_number_int + " is " + ask_number_to_sqr }
else if (ask_number_int < 0)
  document.querySelector("#p7").innerHTML = "number: " + ask_number_int + " is negative so square root is not defined"

