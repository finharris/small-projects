const showPopup = document.getElementById("show-popup");

const popup = document.getElementById("popup");
const backgroundShade = document.getElementById("background-shade");

function handleShowPopup() {
  popup.style.display = "flex";
  backgroundShade.style.display = "block";
}

function handleClosePopup() {
  popup.style.display = "none";
  backgroundShade.style.display = "none";

  popup.style.left = "calc(50% - 350px)";
  popup.style.top = "calc(50% - 250px)";
}

showPopup.addEventListener("click", () => {
  handleShowPopup();
});

let popupClosers = [
  document.getElementById("popup-close"),
  document.getElementById("popup-cancel"),
];

popupClosers.forEach((e) => {
  e.addEventListener("click", handleClosePopup);
});

const popupCancel = document.getElementById("popup-cancel");

// Make the DIV element draggable:
dragElement(popup);

function dragElement(elmnt) {
  var pos1 = 0,
    pos2 = 0,
    pos3 = 0,
    pos4 = 0;
  if (document.getElementById(elmnt.id + "-header")) {
    // if present, the header is where you move the DIV from:
    document.getElementById(elmnt.id + "-header").onmousedown = dragMouseDown;
  }

  function dragMouseDown(e) {
    e = e || window.event;
    e.preventDefault();
    // get the mouse cursor position at startup:
    pos3 = e.clientX;
    pos4 = e.clientY;
    document.onmouseup = closeDragElement;
    // call a function whenever the cursor moves:
    document.onmousemove = elementDrag;
  }

  function elementDrag(e) {
    e = e || window.event;
    e.preventDefault();
    // calculate the new cursor position:
    pos1 = pos3 - e.clientX;
    pos2 = pos4 - e.clientY;
    pos3 = e.clientX;
    pos4 = e.clientY;
    // set the element's new position:
    elmnt.style.top = elmnt.offsetTop - pos2 + "px";
    elmnt.style.left = elmnt.offsetLeft - pos1 + "px";
  }

  function closeDragElement() {
    // stop moving when mouse button is released:
    document.onmouseup = null;
    document.onmousemove = null;
  }
}
