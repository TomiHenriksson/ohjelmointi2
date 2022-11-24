document.getElementById("target").innerHTML = "Random text";



document.getElementById("target").innerHTML += `<li> First item </li> <li>Second item</li>
<li>Third item</li> `;

// element.classList.add("my-list")

function addClass() {
  let elem = document.getElementById("target");
  elem.classList.add("my-list"); }