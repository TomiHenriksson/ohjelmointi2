
// t.8
/* Write a program that prompts the user for the start and end year.
The program prints all leap years from the interval given by the user.
Printing is done in an unordered list to the HTML document. */
let gap_years = []
let start_year1 = prompt("Start year")
let end_year1 = prompt("end year")
let start_year = parseInt(start_year1)
let end_year = parseInt(end_year1)

let gap_year = end_year - start_year

// print all values from gap year that are divisible by 4
//add values to list and print the list

for (let i=1;i<=gap_year;i++) {
  if (gap_year%3==0)
    gap_years.push(i)

}

document.querySelector("#p5").innerHTML = gap_years 