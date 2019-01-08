$( document ).ready(function() {
	$("#drop1").click(function(){
		if ($(".drop2").is(':hidden'))
			$(".drop2").slideDown(200);
		else
			$(".drop2").slideUp(200);
	});


	$(".rollout").click(function(){
		if ($("nav").is(':hidden'))
			$("nav").animate({width:'toggle'},350);
		else
			$("nav").animate({width:'toggle'},350);
	});


	$(".rollin").click(function(){
		if ($("nav").is(':hidden'))
			$("nav").animate({width:'toggle'},350);
		else
			$("nav").animate({width:'toggle'},350);
	});



});

