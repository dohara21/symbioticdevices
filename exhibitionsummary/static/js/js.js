$( document ).ready(function() {
	$("#drop1").click(function(){
		if ($(".drop2").is(':hidden'))
			$(".drop2").slideDown(200);
		else
			$(".drop2").slideUp(200);
	});


	$(".rollout").click(function(){
		if ($("nav").is(':hidden'))
			$("nav").slideDown(200);
		else
			$("nav").slideUp(200);
	});


});

