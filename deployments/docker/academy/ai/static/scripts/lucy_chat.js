const btn = document.querySelector(".lucy-chat__left-menu-btn");
const menu = document.querySelector(".lucy-chat__left");
btn && btn.addEventListener("click", () => {
  if (menu.classList.contains("hide")) {
    menu.classList.remove("hide");
    btn.innerHTML = "HIDE";
  } else {
    menu.classList.add("hide");
    btn.innerHTML = "MENU";
  }
});
