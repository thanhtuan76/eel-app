const reel = document.querySelector('.tab_reel');
const tab1 = document.querySelector('.tab1');
const tab2 = document.querySelector('.tab2');
const tab3 = document.querySelector('.tab3');
const panel1 = document.querySelector('.tab_panel1');
const panel2 = document.querySelector('.tab_panel2');
const panel3 = document.querySelector('.tab_panel3');

function slideLeft(e) {
	tab2.classList.remove('active');
    tab3.classList.remove('active');
	this.classList.add('active');

    panel1.classList.add('tab-active');
    panel2.classList.remove('tab-active');
    panel3.classList.remove('tab-active');
	// reel.style.transform = "translateX(0%)"
}

function slideRight(e) {
	tab1.classList.remove('active');
    tab3.classList.remove('active');
	this.classList.add('active');

    panel2.classList.add('tab-active');
    panel1.classList.remove('tab-active');
    panel3.classList.remove('tab-active');
	// reel.style.transform = "translateX(-49%)"
}
function slide3(e) {
	tab2.classList.remove('active');
    tab1.classList.remove('active');
	this.classList.add('active');

    panel3.classList.add('tab-active');
    panel1.classList.remove('tab-active');
    panel2.classList.remove('tab-active');
	// reel.style.transform = "translateX(-98%)"
}

tab1.addEventListener('click', slideLeft);
tab2.addEventListener('click', slideRight);
tab3.addEventListener('click', slide3);




