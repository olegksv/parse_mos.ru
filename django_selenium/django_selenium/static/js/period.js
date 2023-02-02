var date =new Date();
date.setMonth(date.getMonth()-5)
console.log(date)
var f_month= date.getMonth()+1;
var f_year=date.getFullYear();
var first_half_year=f_month+'.'+ f_year;
var l_month=new Date().getMonth()+1;
var l_year=new Date().getFullYear();
var last_half_year=l_month+'.'+l_year





    $('#sandbox-container #period_start').datepicker({
        language: "ru",
        format: 'mm.yyyy',
        startView: "months",
        minViewMode: "months",
        autoclose:true, 
        orientation: "bottom",
      
    }).on('changeDate',function (selected){
        starper($('#period_s'),selected);
    });

    $('#period_start').datepicker('setDate',date);

    $('#sandbox-container #period_end').datepicker({
        language: "ru",
        format: 'mm.yyyy',
        startView: "months",
        minViewMode: "months",
        autoclose:true,  
        orientation: "bottom", 
        
    })
   /*  $('#period_end').datepicker('setStartDate',starper(start)); */

    $('#period_end').datepicker('setDate',last_half_year);

    function starper(input_start,selected){
        console.log(input_start.val());
        var start_date=(new Date(selected.date.valueOf()));
        var m_start=start_date.getMonth()+1;
        var y_start=start_date.getFullYear();
        var my_start=m_start+'.'+y_start;
        console.log(my_start)
        my_start;
        /* $('#period_end').datepicker('setDate',last_half_year); */
        /* $('#period_end').datepicker('setStartDate',my_start); */
        }   
    
   
   
    



      
/*     var start
    $(function(){
         $('#period_s').change(function(e){
        e.preventDefault();
        start=$(this).val();
        console.log(start);
        starper(start)
        })
        })

    function starper(start){
    console.log(start);
    return start
    } */
    

   
    
   
    



