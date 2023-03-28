window.addEventListener("DOMContentLoaded", () => {
	let spLogos = document.getElementsByClassName("sp-logo");
	for (let i = 0; i < spLogos.length; i++) {
		spLogos[i].style.order = Math.floor(Math.random() * 1000);
	}
});
