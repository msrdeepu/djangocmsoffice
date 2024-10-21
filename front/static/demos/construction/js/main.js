/*-----------------------------------------------------------------------------------

    Theme Name: Fabrex - Building Construction HTML Template
    Description: Building Construction HTML Template
    Author: Chitrakoot Web
    
    ---------------------------------- */    

!function(o){"use strict";var t=o(window);function a(){var e,a;e=o(".full-screen"),a=t.height(),e.css("min-height",a),e=o("header").height(),a=o(".screen-height"),e=t.height()-e,a.css("height",e)}o("#preloader").fadeOut("normall",function(){o(this).remove()}),t.on("scroll",function(){var e=t.scrollTop(),a=o(".navbar-brand img");e<=50?(o("header").removeClass("scrollHeader").addClass("fixedHeader"),a.attr("src","img/logos/logo-white.png")):(o("header").removeClass("fixedHeader").addClass("scrollHeader"),a.attr("src","img/logos/logo.png"))}),t.on("scroll",function(){500<o(this).scrollTop()?o(".scroll-to-top").fadeIn(400):o(".scroll-to-top").fadeOut(400)}),o(".scroll-to-top").on("click",function(e){e.preventDefault(),o("html, body").animate({scrollTop:0},600)}),o(".parallax,.bg-img").each(function(e){o(this).attr("data-background")&&o(this).css("background-image","url("+o(this).data("background")+")")}),t.resize(function(e){setTimeout(function(){a()},500),e.preventDefault()}),a(),o(document).ready(function(){var e;o(".testmonials-carousel").owlCarousel({loop:!1,responsiveClass:!0,nav:!1,dots:!0,autoplay:!0,smartSpeed:500,margin:0,responsive:{0:{items:1},600:{items:1},1e3:{items:1}}}),o(".testimonial-style2").owlCarousel({loop:!1,responsiveClass:!0,nav:!1,dots:!0,autoplay:!0,smartSpeed:500,margin:0,responsive:{0:{items:1},600:{items:1},1e3:{items:2,margin:30}}}),o(".carousel-style1 .owl-carousel").owlCarousel({loop:!0,dots:!0,nav:!1,navText:["<i class='fas fa-angle-left'></i>","<i class='fas fa-angle-right'></i>"],autoplay:!0,autoplayTimeout:5e3,responsiveClass:!0,autoplayHoverPause:!1,responsive:{0:{items:1,margin:0},768:{items:1,margin:0},992:{items:1,margin:0},1200:{items:1,margin:0}}}),o("#clients").owlCarousel({loop:!0,nav:!1,dots:!1,autoplay:!0,autoplayTimeout:3e3,responsiveClass:!0,autoplayHoverPause:!1,responsive:{0:{items:2,margin:20},768:{items:3,margin:40},992:{items:4,margin:60},1200:{items:5,margin:80}}}),o(".slider-fade .owl-carousel").owlCarousel({items:1,loop:!0,margin:0,autoplay:!0,smartSpeed:500,mouseDrag:!1,animateIn:"fadeIn",animateOut:"fadeOut"}),o(".owl-carousel").owlCarousel({items:1,loop:!0,dots:!1,margin:0,autoplay:!0,smartSpeed:500}),o(".slider-fade").on("changed.owl.carousel",function(e){e=e.item.index-2;o("h2").removeClass("animated fadeInUp"),o("h1").removeClass("animated fadeInUp"),o("p").removeClass("animated fadeInUp"),o(".butn").removeClass("animated fadeInUp"),o(".owl-item").not(".cloned").eq(e).find("h2").addClass("animated fadeInUp"),o(".owl-item").not(".cloned").eq(e).find("h1").addClass("animated fadeInUp"),o(".owl-item").not(".cloned").eq(e).find("p").addClass("animated fadeInUp"),o(".owl-item").not(".cloned").eq(e).find(".butn").addClass("animated fadeInUp")}),o(".countup").counterUp({delay:25,time:2e3}),0!==o(".countdown").length&&(e=jQuery)(document).ready(function(){null==e(".countdown").countdown?revslider_showDoubleJqueryError(".countdown"):e(".countdown").show().countdown({date:"01 Nov 2024 00:01:00",format:"on"})}),o(".current-year").text((new Date).getFullYear())}),t.on("load",function(){var a=o(".portfolio-gallery-isotope").isotope({});o(".filtering").on("click","span",function(){var e=o(this).attr("data-filter");a.isotope({filter:e})}),o(".filtering").on("click","span",function(){o(this).addClass("active").siblings().removeClass("active")}),o(".portfolio-gallery").lightGallery(),o(".portfolio-gallery-isotope").lightGallery(),t.stellar()})}(jQuery);