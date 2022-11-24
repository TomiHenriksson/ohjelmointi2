function hOver() {
  document.querySelector("#target").src = "img/picB.jpg"

}

function hOff() {
  document.querySelector("#target").src = "img/picA.jpg"

}

document.querySelector("#trigger").addEventListener("Mouse over", hOver)
document.querySelector("#trigger").addEventListener("Mouse off", hOff)