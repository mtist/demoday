$(function(){
	$('.gallery-slider').slick({
		dots: true,
		infinite:true,
		slidesToShow: 1,
		slidesToScroll: 1,
		autoplay: true,
		autoplaySpeed: 3000,
		pauseOnHover: false,
		cube: false,
		// fade: true, //Opacity
		cssEase: 'linear'
	});
	$('.reviews-slider').slick({
		dots: true,
		infinite:true,
		slidesToShow: 1,
		slidesToScroll: 1,
		autoplay: true,
		autoplaySpeed: 4000,
		pauseOnHover: false,
		cube: false,
		// fade: true, //Opacity
		cssEase: 'ease'
	});
	$('.bestdeals-slider').slick({
		dots: true,
		infinite:true,
		slidesToShow: 3,
		slidesToScroll: 1,
		autoplay: true,
		autoplaySpeed: 3000,
		pauseOnHover: false,
		cube: false,
		// fade: true, //Opacity
		cssEase: 'ease'
	});
});