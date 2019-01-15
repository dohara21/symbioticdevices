$( document ).ready(function() {
	$("#drop1").click(function(){
		if ($(".drop2").is(':hidden'))
			$(".drop2").slideDown(200);
		else
			$(".drop2").slideUp(200);
	});


	$(".rollout").click(function(){
		if ($("nav").is(':hidden')){
			$("nav").animate({width:'toggle'},350);
			$(".rollout").css({'margin-left': '230px'});
			$(".iconrotate").toggleClass('rotate');}
		else{
			$("nav").animate({width:'toggle'},350);
			$(".rollout").css({'margin-left': '-20px'});
			$(".iconrotate").toggleClass('rotate');}
	});

	
});
