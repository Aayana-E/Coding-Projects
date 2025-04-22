let count = 0;
const countDisplay = document.getElementById('count');
const button = document.getElementById('clickButton');
const buyAutoButton = document.getElementById('AutoUpgrade');
let autoClickOn = false;

let clickPower = 1;
let upgradeCost = 10;

buyAutoButton.addEventListener('click',()=>{
	if (count >= 100 && !autoClickOn){
		count -= 100;
		autoClickOn = true;
		buyAutoButton.disable = true;
		buyAutoButton.textContent = "Auto Clicker Activated";
		updateDisplay();
		setInterval(() =>{
			count++;
			updateDisplay();
		} , 1000);
	}
})

button.addEventListener('click', ()=> {
	count++;
	countDisplay.textContent = count;
});

//spacebar click
document.addEventListener('keydown', function(event) {
	if (event.key === " "){
		console.log("space pressed");
		count++;
		countDisplay.textContent = count;
	}		
});

function updateDisplay(){
	countDisplay.textContent = count;
}
