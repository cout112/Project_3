document.addEventListener('DOMContentLoaded', () =>  {



	let toppingbuttons = document.querySelectorAll('.toppings');
	let subtoppingbuttons = document.querySelectorAll(".subtoppings");
	disable_toppings();
	disable_subtoppings();
	let value;
	let price;

	let items_amout;
	let items;
	let toppings;
	let add = 0;
	let prices;
	let total;




	document.addEventListener('click', event => {

		const button = event.target;


		if (button.className == 'btn prices platter'){
			value = button.value;
			price = parseFloat(button.innerHTML);
			add_other(value, price);
			value='';
			price = 0;
		}



		if (button.className == 'btn prices pasta'){
			value = button.value;
			price = parseFloat(button.innerHTML);
			add_other(value, price);
			value='';
			price = 0;
		}

		if (button.className == 'btn prices salad'){
			value = button.value;
			price = parseFloat(button.innerHTML);
			add_other(value, price);
			value='';
			price = 0;
		}


		if (button.className == 'submit btn'){
			add_pizza(value, items, price);
			disable_subtoppings();
			items.length = 0;
			price = 0;
			update_total();
		}


		if (button.className == 'btn prices sub'){
			document.querySelector(".displaysubmit").innerHTML='';
			value = button.value;
			price = parseFloat(button.innerHTML);
			console.log(price);
			items = [];
			able_subtoppings();
		}

		if (button.className == 'subtoppings col-sm-3 btn'){
			button.style.background = '#ffe6e6';
			items.push(button.innerHTML);
			button.disabled = true;
			price = price + 0.50;
			console.log(price);
		}


		if (button.className == "btn prices pizza"){
			value = button.value;
			price = parseFloat(button.innerHTML);
			items_amount=button.dataset.items;
			items = [];
			toppings = 0;


			if (items_amount  === '0'){ 
				items = ['Cheese'];
				add_pizza(value, items, price);
				update_total();
			} else if (items_amount === '1'){
				toppings = 1;
				able_toppings();
			} else if (items_amount === '2'){
				toppings = 2;
				able_toppings();
			} else if (items_amount === '3'){
				toppings = 3;
				able_toppings();
			} else if (items_amount === '3+'){
				toppings = 4;
				able_toppings();
			}
		}



		if (button.className == 'toppings col-sm-auto btn'){
			add = add +1;
			items.push(button.innerHTML);
			button.style.background = '#ffe6e6';
			button.disabled = true;
			if (add >= toppings){
				disable_toppings();
				add_pizza(value, items, price);
				add = 0;
				items.length = 0;
				toppings = 0;
				update_total();
			}
		}


		
		if (button.className == 'btn btn-light +'){
			let times = parseInt(button.parentElement.querySelector(".amount").innerHTML);
			let amount = button.parentElement.querySelector(".amount");
			amount.innerHTML = times + 1;
			let new_times = times+1;
			let old_price = parseFloat(button.parentElement.nextElementSibling.querySelector(".price").innerHTML);
			let new_price_decimals = old_price / times * new_times;
			let new_price = new_price_decimals.toFixed(2);
			button.parentElement.nextElementSibling.querySelector(".price").innerHTML=new_price;
			update_total();


		}
		if (button.className == 'btn btn-light -'){
			let times = parseInt(button.parentElement.querySelector(".amount").innerHTML);
			if (times > 1){
				let amount = button.parentElement.querySelector(".amount");
				amount.innerHTML = times - 1;
				let new_times = times-1;
				let old_price = parseFloat(button.parentElement.nextElementSibling.querySelector(".price").innerHTML);
				let new_price_decimals = old_price / times * new_times;
				let new_price = new_price_decimals.toFixed(2);
				button.parentElement.nextElementSibling.querySelector(".price").innerHTML=new_price;
			}else {
				button.parentElement.parentElement.parentElement.outerHTML='';
			}
			update_total();
			
		}
	});

	
	const channel_template = Handlebars.compile(document.querySelector('#new_pizza').innerHTML);
	
	function add_pizza(value, items, price){
		const pizza_item = channel_template({'value':value, 'items':items, 'price':price});
		document.querySelector('#items').innerHTML += pizza_item;
	};

	const channel_template_other = Handlebars.compile(document.querySelector('#new_item').innerHTML);
	function add_other(value, price){
		const other_item = channel_template_other({'value':value, 'price':price});
		document.querySelector('#items').innerHTML += other_item;
	};




	function disable_toppings(){
		for (let i = 0; i<toppingbuttons.length;i++){
			toppingbuttons[i].style.background = '';
			toppingbuttons[i].disabled = true;
		}
		document.querySelector(".toppingssquare").style.border = "none";
		document.querySelector(".toppingsinfo").innerHTML = '';

	};

	function able_toppings(){
		for (let i = 0; i<toppingbuttons.length;i++){
					toppingbuttons[i].disabled = false;
		}
		document.querySelector(".toppingssquare").style.border = "solid red 1px";
		if (toppings === 1){
			document.querySelector(".toppingsinfo").innerHTML = 'Choose ' + toppings + ' topping';
		}else{
			document.querySelector(".toppingsinfo").innerHTML = 'Choose ' + toppings + ' toppings';
		}
		
	};

	function disable_subtoppings(){
		document.querySelector(".displaysubmit").innerHTML='';
		document.querySelector(".subtoppingssquare").style.border = "none";
		for (let i=0; i<subtoppingbuttons.length;i++){
			subtoppingbuttons[i].style.background = '';
			subtoppingbuttons[i].disabled = true;
		}
	}

	function able_subtoppings(){
		for (let i=0; i<subtoppingbuttons.length;i++){
			subtoppingbuttons[i].disabled = false;
		}
		submitbutton = document.createElement('button');
		submitbutton.className = 'submit btn';
		submitbutton.innerHTML = 'Submit';
		submitbutton.style.position = "relative";
		submitbutton.style.bottom = "10px";
		document.querySelector(".displaysubmit").append(submitbutton);
		document.querySelector('.subtoppingssquare').style.border = "solid red 1px";
	}


	function update_total(){
		prices = document.querySelectorAll(".price");
		total = 0;
		for (i=0; i<prices.length; i++){
			total = total + parseFloat(prices[i].innerHTML);
		}

		document.querySelector("#total").innerHTML = total.toFixed(2);
	}
	
});