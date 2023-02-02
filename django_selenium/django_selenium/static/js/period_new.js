var cur_date =new Date();
var date =new Date();
date.setMonth(date.getMonth()-5)



$('#sandbox-container #period_start').datepicker({
    language: "ru",
    format: 'mm.yyyy',
    startView: "months",
    minViewMode: "months",
    autoclose:true, 
    orientation: "bottom",
      
}).on('changeDate',function (e){
    starper($('#period_start'),e);
});

$('#period_start').datepicker('setDate',date);

function starper(input_start,e){
    var start_date=(new Date(e.date.valueOf()));
    console.log(input_start)
    console.log(start_date)
$('#sandbox-container #period_end').datepicker({
    language: "ru",
    format: 'mm.yyyy',
    startView: "months",
    minViewMode: "months",
    autoclose:true,  
    orientation: "bottom", 
      
})
$('#period_end').datepicker('setStartDate',start_date);


$('#period_end').datepicker('setDate',cur_date);

}  
    
   
   
    




   
    
   
    



