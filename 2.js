
// const newDiv = document.createElement("div")

let ul = document.getElementById("target")
const nContent = document.createTextNode("Random text")
ul.appendChild(nContent)


document.getElementById("target").innerHTML += `<li> First item </li> <li>Second item</li>
<li>Third item</li> `;


function addLi2()  {
  let elem2 = document.getElementById("target")[1]
  elem2.classList.add("my-item")   }