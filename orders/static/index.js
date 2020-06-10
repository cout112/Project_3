document.addEventListener('DOMContentLoaded', () =>  {

	let counter = 0;

	document.querySelector('#increase').onclick = () => {
		counter++;
		document.querySelector('h2').innerHTML = counter;
	};

	document.querySelector('#decrease').onclick = () => {
		if (counter > 0){
		counter--;
		document.querySelector('h2').innerHTML = counter;
		}
	};

	document.addEventListener('click', event => {
		const element = event.target;
        if (element.className === 'btn login'){
        	let login = document.querySelector("#login");
        	while(login.firstChild){		
                  login.removeChild(login.firstChild);
        	};

        };
	});	

});