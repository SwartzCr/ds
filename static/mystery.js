var img = document.getElementById("img");
var node = document.createElement("IMG");
node.src = "https://danielle.soy/spacer.gif";
var fnx = function() {document.getElementById("division").appendChild(node);};
img.addEventListener("click", fnx);
