import {Circle} from "./components/circle"

let h1 = document.createElement("h1")
h1.id = "heading"
let textNode = document.createTextNode("SP Is Cool")
h1.appendChild(textNode)
new Circle()

document.body.appendChild(h1)