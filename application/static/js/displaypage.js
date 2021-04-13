
let tabs = ["buyer", "plot", "CA", "ET", "deal"];


function clicked(name){
	
	//Turning on the cliked div
	document.getElementById(name+"-div").style.display = 'block';

	//Turning off the rest of divs
	for(let tab of tabs){
		if(tab != name){
			document.getElementById(tab+"-div").style.display = 'none';
			$('#'+name+'-info').html('');
		}
	}
}

function make_plot_card(plot){
	
	let str = "<p>" +
				"Plot ID: "     	+ plot.id 		+ "</br>" +
				"Plot Type: " 		+ plot.type 		+ "</br>" +
				"Plot Address: "	+ plot.address 	+ "</br>" +
				"Plot Status: " 	+ plot.status 	+ "</br>";

	if(!plot.price)
		str += "Plot Price: <span style='color: red;''>Not Set</span></br>";

	str += "Plot Size: " 		+ plot.size 		+ "</br>" +
		   "Plot Comments: " 	+ plot.comments 	+ "</br>";

	if(plot.deal){
		str += "Plot's Deal: " + 
		"<a href='" + "/dealinfo/" + plot.deal.id + "''>" + 
			plot.deal.id + 
		"</a></br>";
	}

	return str + "</p>\n";
}

function make_buyer_card(buyer){

	let str = "<p>" +
				"Buyer ID: "    + buyer.id    + "</br>" +
				"Buyer Name: "  + buyer.name  + "</br>" +
				"Buyer CNIC: "  + buyer.cnic  + "</br>" +
			  "</p>";

	return str;
}

function make_deal_card(deal){

	let str = "<p>" +
				"Deal ID: "    		+ deal.id    		+ "</br>" +
				"Date of Signing: " + deal.signing_date + "</br>" +
				"Plot ID: "  		+ buyer.plot.id  	+ "</br>" +
			  "</p>";

	return str;

}
function make_CA_card(CA){}
function make_ET_card(ET){}

function inject_div(name, list){

	let str 	   = '';
	let make_card  = window['make_'+name+'_card'];
	for(let element of list){
	  	str = make_card(element);			  	
	  	$('#'+name+'-info').append(str);
	}
}

function getall(name){
	
	clicked((name || "buyer"));
	$.post('/rest/'+name+'/all', function(data){
		inject_div(name, data.json_list);
	});	
}

$(document).ready(function(){
	$("#filterPlot-btn").on('click', function(){
		$.post('/rest/filterplot/'+$("#status").val(), function(plots) {
			$('#plot-info').html('');
		 	inject_div('plot', plots.json_list);		  
		});
	});
});