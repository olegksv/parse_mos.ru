function zero_first_format(value)
{
    if (value < 10)
    {
        value='0'+value;
    }
    return value;
}

function check_holidays(dayOfWeek,) {
    if (dayOfWeek === 'сб'  || dayOfWeek === 'вс') {
        
         /* '<span style="color:red;">' + day+ "/" +month+ "/"+ year + '</span>'; */
       
         return '<span style="color:red";>' + dayOfWeek + '</span>';
    }
    else {
        return dayOfWeek;
    }

}

function date()
{
    var current_datetime = new Date();
    var day = zero_first_format(current_datetime.getDate());
    var month = zero_first_format(current_datetime.getMonth()+1);
    var year = current_datetime.getFullYear();
    return check_holidays(day+ "/" +month+ "/" +year);

}

function clock_day() {
   var current_datetime = new Date();
   var date_of_week= new Array('вс','пн','вт','ср','чт','пт','сб');
   var dayOfWeek = check_holidays(date_of_week[current_datetime.getDay()]);
   var hours = zero_first_format(current_datetime.getHours());
   var minutes = zero_first_format(current_datetime.getMinutes());
   
    return dayOfWeek+  " "+hours+ ":" +minutes;
    
};

setInterval(function () {
   
    document.getElementById("date").innerHTML = date();
    document.getElementById('clock_day').innerHTML=clock_day();


}, 100);