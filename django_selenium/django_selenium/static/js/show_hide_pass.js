// Hide and show password
const eyeIcons = document.querySelectorAll(".fa-eye-slash");

eyeIcons.forEach((eyeIcon) => {
  eyeIcon.addEventListener("click", () => {
    const pInput = eyeIcon.parentElement.querySelector("input"); //getting parent element of eye icon and selecting the password input
    // console.log(pInput); выведет <input type="password" name="password" class="form-control" placeholder="Пароль" required="" id="id_password">
    if (pInput.type === "password") {
        eyeIcon.classList.replace("fa-eye-slash", "fa-eye");
            return (pInput.type = "text");
    }
        eyeIcon.classList.replace("fa-eye", "fa-eye-slash");
            return (pInput.type = "password");
  });
});
/* $(function () {
    $('.password-group').find('.form-control').each(function(index, input) {
        var $input = $(input);
       
        $input.parent().find('.eye').click(function() {
           
            var change = "";
            if ($(this).find('i').hasClass('fa-eye-slash fa-lg ')) {
                $(this).find('i').removeClass('fa-eye-slash fa-lg ')
                $(this).find('i').addClass('fa-regular fa-eye fa-lg')
                change = "text";
            } else {
                $(this).find('i').removeClass('fa-eye fa-lg')
                $(this).find('i').addClass('fa-regular fa-eye-slash fa-lg')
                change = "password";
            }
            var rep = $("<input type='" + change + "' />")
                .attr('id', $input.attr('id'))
                .attr('name', $input.attr('name'))
                .attr('class', $input.attr('class'))
                .val($input.val())
                .insertBefore($input);
            $input.remove();
            $input = rep;
        }).insertAfter($input);
    });
});
 */

/* function show_pass_reg_form() {
    
    let x = document.getElementById("id_password1");
    let y = document.getElementById("eye-hide_pass1");
    let z= document.getElementById("eye-show_pass1");
    let x1 = document.getElementById("id_password2");
    let y1 = document.getElementById("eye-hide_pass2");
    let z1= document.getElementById("eye-show_pass2");

    if(x.type === 'password') {
        x.type  = 'text';
        y.style.display="block";
        z.style.display="none";
        } 
    else if(x.type==='text') { 
            x.type = 'password';
            y.style.display="none";
            z.style.display="block";
        }
    else if(x1.type ==='password'){
            x1.type='text';
            y1.style.display="block";
            z1.style.display="none";
    } else {
            x1.type='password';
            y1.style.display="none";
            z1.style.display="block";
        }

    } */ 
        /* else if(x1.type === 'password') {
            x1.type = 'text';
            y.style.display="block";
            z.style.display="none";
        }
        else {
            x.type = 'password';
            x1.type='password';
            y.style.display="none";
            z.style.display="block";
        }
} */