// Get the  model
var myModal = document.getElementById('modal');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
	if (event.target == myModal) {
		myModal.style.display = "none";
		window.history.back();
	}
}

// Left bar open nav
function openNav() {
	let classnames = document.getElementById('left_menu').className
	document.getElementById('left_menu').className = classnames.includes('show') ? classnames : `${classnames} show`
}

// Left bar close nav
function closeNav() {
	document.getElementById('left_menu').classList.remove('show')
}
