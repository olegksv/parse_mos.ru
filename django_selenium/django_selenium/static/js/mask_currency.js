
$(document).ready(function(){
    var num=$('#id_amount_of_bill');
    num.keyup(function() {
    var value =$(this).val();
    console.log(value);
   })
});


  $(function (){
    $('input[id^=id_amount_of').before('<i class="fa-solid fa-ruble-sign"></i>');
  });
