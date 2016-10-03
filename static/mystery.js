var img = document.getElementById("img");
var node = document.createElement("IMG");
node.src = "https://alinkisnotenabled.com/spacer.gif";
var fnx = function( event ) {
    event.preventDefault();
    document.getElementById("division").appendChild(node);
    window.location = "https://danielle.soy/puzzle2";};
img.addEventListener("click", fnx);
