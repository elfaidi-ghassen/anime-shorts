let visible = false;
let ul = document.getElementById("toShow")
function show() {
  if (visible == false) {
    ul.style.visibility = "visible";
    visible = true;
    ul.classList.add("start");
  }
  else {
    ul.style.visibility = "hidden";
    visible = false;
    ul.classList.remove("start");
  }
}