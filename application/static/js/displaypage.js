
let tabs = ["buyers", "plots", "CAs", "ETs"];

//clicked("{{ active }}");

function clicked(name){
	//Turning on the cliked button and div
	document.getElementById(name+"-div").style.display = 'block';
	document.getElementById(name+"-button").className  = 'btn btn-info';

	//Turning off the resst of buttons and divs
	for(let tab of tabs){
		if(tab != name){
			document.getElementById(tab+"-div").style.display = 'none';
			document.getElementById(tab+"-button").className  = 'btn btn-outline-info';
		}
	}
}

function makePlotCard(id, type, address, status, price, size, comments){
	return 	"<p>" +
				"Plot ID: "     	+ id 		+ "</br>" +
				"Plot Type: " 		+ type 		+ "</br>" +
				"Plot Address: "	+ address 	+ "</br>" +
				"Plot Status: " 	+ status 	+ "</br>" +
				"Plot Price: " 		+ price 	+ "</br>" +
				"Plot Size: " 		+ size 		+ "</br>" +
				"Plot Comments: " 	+ comments 	+ "</br>" +
			"</p>\n";

}

$(document).ready(function(){
	$("#filter-btn").on('click', function(){
		console.log($("#status").val());
		$.post('/filterplot/'+$("#status").val(), function(plots) {
		  let str = '';
		  for(let plot of plots.json_list){
		  	str += makePlotCard(plot.id, plot.type, plot.address, plot.status, plot.price, plot.size, plot.comments);
		  }
		  $("#plots-div").html(str);
		  
		});
	});
});