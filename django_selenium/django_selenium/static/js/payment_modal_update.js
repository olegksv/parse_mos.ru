function getCookie(name) {			
    var cookieValue = null;			
    if (document.cookie && document.cookie !== '') {			
    var cookies = document.cookie.split(';');			
    for (var i = 0; i < cookies.length; i++) {			
    var cookie = jQuery.trim(cookies[i]);			
    // Does this cookie string begin with the name we want?			
    if (cookie.substring(0, name.length + 1) === (name + '=')) {			
    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));			
    break;			
     }			
    }			
    }			
    return cookieValue;			
    }			
                
    var csrftoken = getCookie('csrftoken');			
                
    function csrfSafeMethod(method) {			
    // these HTTP methods do not require CSRF protection			
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));			
    }			
                
    $.ajaxSetup({			
    beforeSend: function(xhr, settings) {			
     if (!csrfSafeMethod(settings.type) && !this.crossDomain) {			
    xhr.setRequestHeader("X-CSRFToken", csrftoken);			
     }			
     }			
    });			
    

    $('#payment_modal').on('click', function (e){
        e.preventDefault();
        var payment_id=$('#payment_modal').attr('data-payment-id')
            $.ajax({
                type: "GET",
                url: "/add_payment/"+payment_id+"/",
                headers: {
                "X-Requested-With": "XMLHttpRequest",
                "X-CSRFToken": csrftoken, // don't forget to include the 'getCookie' function
                },
                    
                
                dataType: "dataType",
                success: function (response) {
                    console.log(response)
                }
            }); 
            
    })
  
   


   /*  $('#payment_modal').on('submit',function(e){
        e.preventDefault();
        var payment_id=$('#conf_del').attr('data-bs-id').val();
        console.log(payment_id);
        $.ajax({
            type: "POST",
            url: "/add_payment/"+{payment_id}+"/",
            data: "data",
            dataType: "dataType",
            success: function (response) {
                console.log(response)
            }
        });
    }) */
    