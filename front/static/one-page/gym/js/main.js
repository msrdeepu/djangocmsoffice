/*-----------------------------------------------------------------------------------

    Theme Name: Fabrex - Fitness and GYM HTML Template
    Description: Onepage Fitness and GYM HTML Template
    Author: Chitrakoot Web
        
    ---------------------------------- */    

$(function(){"use strict";var t=$(window);$("#preloader").fadeOut("normall",function(){$(this).remove()}),$.scrollIt({upKey:38,downKey:40,easing:"swing",scrollTime:600,activeClass:"active",onPageChange:null,topOffset:-70}),t.on("scroll",function(){600<t.width()&&(600<t.scrollTop()?$("#back-to-top").addClass("reveal"):$("#back-to-top").removeClass("reveal"))}),$("#back-to-top").on("click",function(){return $("html, body").animate({scrollTop:0},1e3),!1}),$("#sidebar_toggle").length&&($("body").addClass("sidebar-menu"),$("#sidebar_toggle").on("click",function(){$(".sidebar-menu").toggleClass("active"),$(".side-menu").addClass("side-menu-active"),$("#close_sidebar").fadeIn(700)}),$("#close_sidebar").on("click",function(){$(".side-menu").removeClass("side-menu-active"),$(this).fadeOut(200),$(".sidebar-menu").removeClass("active")}),$("#btn_sidebar_colse").on("click",function(){$(".side-menu").removeClass("side-menu-active"),$("#close_sidebar").fadeOut(200),$(".sidebar-menu").removeClass("active")})),t.on("scroll",function(){var a=t.scrollTop(),e=$(".navbar"),o=$(".blog-nav .logo> img"),s=$(".bg-black .logo> img"),n=$(".navbar .logo> img");100<a?(e.addClass("nav-scroll"),n.attr("src","img/logo-dark.png"),s.attr("src","img/logo-light.png")):(e.removeClass("nav-scroll"),n.attr("src","img/logo-light.png"),o.attr("src","img/logo-dark.png"))}),t.width()<=991&&$(".navbar-nav .nav-link").on("click",function(){$(".navbar-collapse.show").removeClass("show"),$(".navbar .navbar-toggler").addClass("collapsed")}),$(".bg-img, section, footer").each(function(a){$(this).attr("data-background")&&$(this).css("background-image","url("+$(this).data("background")+")")}),$(".story-video").magnificPopup({delegate:".video",type:"iframe"}),$(".countup").counterUp({delay:25,time:2e3}),$(".current-year").text((new Date).getFullYear()),$(document).ready(function(){var a=$(".header .owl-carousel");$(".slider-fade .owl-carousel").owlCarousel({items:1,loop:!0,margin:0,autoplay:!0,smartSpeed:500,mouseDrag:!1,animateIn:"fadeIn",animateOut:"fadeOut"}),$(".classes-section .owl-carousel").owlCarousel({items:1,loop:!0,margin:30,autoplay:!1,dots:!1,smartSpeed:500,responsive:{0:{items:1,autoplay:!1,margin:10},768:{items:2,autoplay:!1,margin:10},992:{items:2,margin:10},1200:{items:3,margin:20}}}),$(".blog-section .owl-carousel").owlCarousel({items:3,loop:!0,margin:30,autoplay:!1,dots:!1,smartSpeed:500,responsive:{0:{items:1,autoplay:!1,margin:10},768:{items:1,autoplay:!1,margin:10},992:{items:2,margin:10}}}),$(".owl-carousel").owlCarousel({items:1,loop:!0,margin:0,autoplay:!0,smartSpeed:500}),a.on("changed.owl.carousel",function(a){a=a.item.index-2;$("span").removeClass("animated fadeInUp"),$("h1").removeClass("animated fadeInUp"),$("p").removeClass("animated fadeInUp"),$(".butn").removeClass("animated fadeInUp"),$(".owl-item").not(".cloned").eq(a).find("span").addClass("animated fadeInUp"),$(".owl-item").not(".cloned").eq(a).find("h1").addClass("animated fadeInUp"),$(".owl-item").not(".cloned").eq(a).find("p").addClass("animated fadeInUp"),$(".owl-item").not(".cloned").eq(a).find(".butn").addClass("animated fadeInUp")})})});