
// t.5
/* Write a program that asks the user to enter a year and notifies the user whether the input year is
a leap year. A year is a leap year if it is divisible by four.
However, years divisible by 100 are leap years only if they are also divisible by 400.
Print the result on the HTML document. */

let year_promt1 = prompt("Enter a year")
let year_promt = parseInt(year_promt1)

if (year_promt % 4 == 0)
 document.querySelector("#p5").innerHTML = year_promt + " vuosi on karkausvuosi!"
else
 document.querySelector("#p5").innerHTML = year_promt + " vuosi ei ole karkausvuosi"
