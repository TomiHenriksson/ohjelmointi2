/* Write a program that asks for the names of six dogs.
The program prints dog names to unordered list <ul> in reverse alphabetical order.*/
listOfDogs = []
for (i=0 ; i<6 ; i++) {
  let dog = prompt("enter dog name")
  listOfDogs.push(dog)
}
listOfDogs.sort()
listOfDogs.reverse()

document.querySelector("#dogs").innerHTML = listOfDogs