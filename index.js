window.addEventListener("DOMContentLoaded", () => {
	let spLogos = document.getElementsByClassName("sp-logo");
	for (let i = 0; i < spLogos.length; i++) {
		spLogos[i].style.order = Math.floor(Math.random() * 1000);
	}
	
	let goldSponsorsOuter = document.getElementsByClassName("sp-level-outer-gold");
	if (Math.random() > 0.5) {
		goldSponsorsOuter[0].style.order = -1;
		goldSponsorsOuter[1].style.order = -2;
	}
	
	let date = new Date();
	let daysRemaining = -1;
	if (date.getUTCFullYear() == 2023) {
		if (date.getUTCMonth() == 5) {
			daysRemaining = 45 - date.getUTCDate();
		} else if (date.getUTCMonth() == 6) {
			daysRemaining = 15 - date.getUTCDate();
		}
	}
	if (daysRemaining > 0) {
		let text = daysRemaining.toString() + " day";
		if (daysRemaining > 1)
			text += "s";
		text += " left!";
		document.getElementById("time-remaining").innerText = text;
	}
});
