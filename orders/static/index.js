document.addEventListener('DOMContentLoaded', () =>  {

	let counter = 0;

	let toppingbuttons = document.querySelectorAll('.toppings');
	disable_toppings();
	let value;
	let price;
	let cart;
	let items_amout;
	let items;
	let toppings;
	let add = 0;
	let prices;
	let total;




	document.addEventListener('click', event => {

		const button = event.target;





		if (button.className == "btn prices pizza"){
			value = button.value;
			price = parseFloat(button.innerHTML);
			cart = document.querySelector('.cart')
			items_amount=button.dataset.items;
			items = [];
			toppings =0;


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
	const channel_template = Handlebars.compile(document.querySelector('#new_pizza').innerHTML);
	
	function add_pizza(value, items, price){
		const pizza_item = channel_template({'value':value, 'items':items, 'price':price});
		document.querySelector('#items').innerHTML += pizza_item;
	 };

	function disable_toppings(){
		for (let i = 0; i<toppingbuttons.length;i++){
					toppingbuttons[i].disabled = true;
		}
	};

	function able_toppings(){
		for (let i = 0; i<toppingbuttons.length;i++){
					toppingbuttons[i].disabled = false;
		}
	};


	function update_total(){
		prices = document.querySelectorAll(".price");
		total = 0;
		for (i=0; i<prices.length; i++){
			console.log(parseFloat(prices[i].innerHTML));
			total = total + parseFloat(prices[i].innerHTML);
		}
		console.log(`Equals to`);
		console.log(total);
		document.querySelector("#total").innerHTML = total.toFixed(2);
	}
	
});