var img = document.getElementById("link");
var fnx = function( event ) {
    event.preventDefault();
    var node = document.createElement("IMG");
    node.addEventListener("load", function() { window.location = "https://danielle.soy/puzzle2";});
    node.src = "https://alinkisnotenabled.com/spacer.gif";
    document.getElementById("division").appendChild(node);};
img.addEventListener("click", fnx);
