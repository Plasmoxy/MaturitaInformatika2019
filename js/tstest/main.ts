import $ from "jquery"

let i = 0

$("#button").click(e => {
    e.target.innerHTML = String(i)
    $("#textCounter").text(String(i))
    i++
})

setInterval(() => {
    $("#clocc").text( new Date().toLocaleTimeString() )
}, 10)