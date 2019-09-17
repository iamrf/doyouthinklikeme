//  ***   set slider size equal to viewport   ***
$(document).ready(function() {
    function setHeight() {
      windowHeight = $(window).innerHeight() -56;
      $('.carousel-inner,.img-full,.full-view').css('height', windowHeight);
      $('.carousel-inner,.img-full,.full-view').width(window.innerWidth);
    };
    setHeight();
  
    $(window).resize(function() {
      setHeight();
    });
  });


//    *** BS4 tooltip
$(document).ready(function(){
  $('[data-toggle="tooltip"]').tooltip();
});


//    *** BS4 Popover
$(document).ready(function(){
  $('[data-toggle="popover"]').popover();
});


//    *** BS4 Toast 
$(document).ready(function(){
  $('.toast').toast('show');
});


// Scroll Indicator   --  When the user scrolls the page, execute myFunction
window.onscroll = function() {myFunction()};

function myFunction() {
  var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
  var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
  var scrolled = (winScroll / height) * 100;
  document.getElementById("scroll-indicator").style.width = scrolled + "%";
}



// Fade effect
$(window).on("load",function() {
  $(window).scroll(function() {
    var windowBottom = $(this).scrollTop() + $(this).innerHeight();
    $(".fade").each(function() {
      /* Check the location of each desired element */
      var objectBottom = $(this).offset().top + ($(this).outerHeight()/5);
      
      /* If the element is completely within bounds of the window, fade it in */
      if (objectBottom < windowBottom) {
      //object comes into view (scrolling down)
        if ($(this).css("opacity")==0) {$(this).fadeTo(500,1);}
      } 

    /* For Hide object after scrollUp following with this script: 
          else {
        //object goes out of view (scrolling up)
        if ($(this).css("opacity")==1) {$(this).fadeTo(500,0);}
      }
    */
    });
  }).scroll(); //invoke scroll-handler on page-load
});