let currentTab = 0;
window.addEventListener("DOMContentLoaded", () => {
	let tabs = document.getElementsByClassName("sch-tab");
	let days = document.getElementsByClassName("sch-day");
	days[currentTab].classList.add("sch-day-current");
	tabs[currentTab].classList.add("sch-tab-current");
	for (let i = 0; i < tabs.length; i++) {
		tabs[i].addEventListener("click", () => {
			tabs[currentTab].classList.remove("sch-tab-current");
			days[currentTab].classList.remove("sch-day-current");
			currentTab = i;
			tabs[currentTab].classList.add("sch-tab-current");
			days[currentTab].classList.add("sch-day-current");
		});
	}
});
