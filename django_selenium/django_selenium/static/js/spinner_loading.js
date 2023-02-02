$(window).bind("pageshow", function(event) {
    if (event.originalEvent.persisted) {
      $("#id_name_flat").val('');
    }
});
$(window).bind("pageshow", function(){
    //$(".spinner-border").hide();
    //location.reload();
 });
$(document).ready(function(){
/* $(document).ajaxSend(function (){
        $("spinner-border").fadeIn(500);
        var loading= `<div class="spinner-border"></div>&nbsp;&nbsp; Подождите...`
        $("#log_btn").html(loading);
    }); */

/*  $(window).bind("pageshow", function(){
    $(".spinner-border").hide();
 }); */
   
 $( document ).ajaxSend(function( event, jqxhr, settings ) {
    if ( settings.url == "/get_list_epd" ) {
        $("spinner-border").fadeIn(500);
        var loading= `<div class="spinner-border"></div><span class="spinner"> Подождите ...</span>`
        $("#log_btn").html(loading);
        
    }
  });

    $("#log_btn").click(function () { 

        $(".spinner-border").fadeIn(500);
        /* var h=history.pushState(data,title, url);
        console.log(h); */
        console.log('we are here')
        $.ajax({
            type:"GET",
            url:'/choose_flats/',
            success:function(data) {
                console.log(data["root"]);
                console.log("{{root}}")
                
            }
        }).done(function() {
            setTimeout(function(){
                $(".spinner-border").fadeOut(500);
            },5000);
        });
    });
    })
    