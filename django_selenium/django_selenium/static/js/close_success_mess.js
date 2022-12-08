/* $(function (){

           $('#SerializedFormData').on('submit',function(e) {
            e.preventDefault();
            var field= $("#SerializedFormData").serialize();
            console.log(field);
            var csrf_token = $("input[name='csrfmiddlewaretoken']").val();
            $.ajax({
                url:'',
                data: { field,
                        'csrfmiddlewaretoken': csrf_token},
                        
                type:'post',
                success: function(field) {
                    console.log(field.field);
                },
                    });
                });
           $('#close_success_message').delay(3000).slideUp(300);
        
  
})
 */
