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
let nav = document.getElementById("navbar");
let menuVisible = false;
function menu() {
  if (menuVisible == false) {
    nav.style.visibility = "visible";
    menuVisible = true;
    nav.classList.add("nav-animation");
    document.getElementById("bar").classList.remove("fa", "fa-bars");
    document.getElementById("bar").classList.add("fa-x",  "fa-solid");
  }
  else {
    nav.style.visibility = "hidden";
    menuVisible = false;
    nav.classList.remove("nav-animation");
    document.getElementById("bar").classList.remove("fa-x",  "fa-solid");
    document.getElementById("bar").classList.add("fa", "fa-bars");
  }
}