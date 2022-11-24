'use strict';


const names = ['John', 'Paul', 'Jones'];


/*let li1 = document.getElementById("target").innerHTML += <li></li>
let li2 = document.getElementById("target").innerHTML += <li></li>
let li3 = document.getElementById("target").innerHTML += <li></li>*/
let li1 = document.createElement("ul")
let li2 = document.createElement("ul")
let li3 = document.createElement("ul")


let target = document.getElementById("target")
target.appendChild(li1)
target.appendChild(li2)
target.appendChild(li3)



names.reverse()
for ( let i =-2 ; i < names.length ; i++) {
  if (i => -1) {
    names.reverse()
  }
  if (i == -1) {
    document.getElementById("target")[0] += names[0]
  }
  else if (1 == 0)  {
    document.getElementById("target")[1] += names[0]
  }
  else {
    document.getElementById("target")[2] += names[0]
  }
  document.getElementById("target").innerHTML += names[0]
  names.reverse()
  names.pop()
    

}