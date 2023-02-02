$(document).ready(function () {
    $('.show_more').on('click', function(){
        var nf= $("#name_fl").attr('data-fl')
        console.log(nf);
        $.ajax({
        type: "GET",
        url: "/show_more_payments/",
        data:{
            name_flat:nf
        },
        dataType: "json",
        success: function (response) {
            console.log(response.context)
            var spinnerBox=$('#spinner-circle');
            spinnerBox.removeClass('not-visible');
            setTimeout(()=>{
                spinnerBox.addClass('not-visible');
                var len_list=response.context.length-1
                var last_per_oplaty=response.context[len_list].period_oplaty;
                var month=new Date(last_per_oplaty).getMonth()+1;
                if(month<10) {
                    var new_month="0"+month
                    }else{
                        new_month=month
                    }
                var year=new Date(last_per_oplaty).getFullYear();
                var replace_per_oplaty=new_month +'.'+year;
                $('#table_row > tbody').html('');
                    var len=response.context.length;
                    var count=0
                    while(count<len) {
                        var dateString=response.context[count].period_oplaty;
                        var date=new Date(dateString).toLocaleDateString('ru',{month:'short',year:'numeric'}).replace(/['.']/g,'');
                        console.log(date)
                        var link='<a class="" href="'+'/Bill_pdf/'+ response.context[count].bill_save_pdf +'">'+response.context[count].bill_save_pdf+'</a>';
                        var date_=new Date(response.context[count].period_oplaty).toLocaleDateString('ru',{month:'short',year:'numeric'});
                        console.log(typeof(response.context[count].amount_of_real));
                        if(response.context[count].date_of_payment===null) {
                            response.context[count].date_of_payment='<i class="fa-solid fa-calendar"></i>'
                        }
                        $("#table_row > tbody ").append(
                            '<tr>\
                            <td>' + [count+1]+'</td>\
                            <td>' + response.context[count].cod_platelshika +'</td>\
                            <td>' + response.context[count].name_flat +'</td>\
                            <td>' +date_.slice(0,1).toUpperCase()+date_.slice(1,3)+" "+date_.slice(5).trim().replace(/г./,'')+'</td>\
                            <td>' + response.context[count].summa +'</td>\
                            <td>' +link+'</td>\
                            <td>' + response.context[count].amount_of_real.replace('.',',')+'</td>\
                            <td>' + response.context[count].date_of_payment +'</td>\
                            <td><button type="submit" class="btn btn-success btn-sm" id="conf_del" data-bs-toggle="modal"\
                            data-bs-target="#payment" data-bs-id="'+response.context[count].id +'">\<i class="fa-solid fa-sack-dollar">\
                            </i> оплатить</button></td>\
                            </tr>'
                            ) 
                        count++;
                        var str_per_oplaty=$("#period").text();
                        var replace_value_oplaty=str_per_oplaty.replace(/\d+\.\d+/,replace_per_oplaty)
                        console.log(replace_value_oplaty)
                        $("#period").html('');
                        $("#period").append('<th scope="col" id="period">'+replace_value_oplaty+'</th>')
                        var text_button=$('.show_get').text();
                        var text_replace=text_button.replace(text_button,'Счетов больше нет')
                        $('.show_get').html('')
                        $('.show_get').append(
                            '<span class="show_get">'+text_replace+'</span>' 
                        )
                        $('#show_more').attr('disabled',true)
                    }
            },500)  
        }
        
    });
    })

    });

