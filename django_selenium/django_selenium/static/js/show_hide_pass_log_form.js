function show_pass_log_form() {
    
    let x = document.getElementById("id_password");
    let y = document.getElementById("eye-hide");
    let z= document.getElementById("eye-show");
    

    if(x.type === 'password') {
        x.type = 'text';
        y.style.display="block";
        z.style.display="none";
        } else {
            x.type = 'password';
            y.style.display="none";
            z.style.display="block";
        }
}

/* let showPassword =  document.querySelectorAll('.fa-regular.fa-eye-slash');
console.log(showPassword)

showPassword.forEach(item =>
    item.addEventListener('click', toggleType)

);


 function toggleType() {
    let pass = document.getElementById('id_password');
    if (pass.type === 'password') {
        pass.type = 'text';
      let eyehide = document.getElementsByClassName('fa-regular fa-eye-slash');
      let eyeshow = document.getElementsByClassName('fa-regular fa-eye');
      for(let i=0; i<eyehide.length; i++) eyehide[i].style.display='block';
      for(let i=0; i<eyeshow.length; i++) eyeshow[i].style.display='none';
        
    } else {
        pass.type = 'password';
      let eyehide = document.getElementsByClassName('fa-regular fa-eye-slash');
      let eyeshow = document.getElementsByClassName('fa-regular fa-eye');
        for(let i=0; i<eyehide.length; i++)eyehide[i].style.display='none';
      for(let i=0; i<eyeshow.length; i++)eyeshow[i].style.display='block';
    }
} */

/* let showPassword = document.querySelectorAll('.eye');


showPassword.forEach(item =>
    item.addEventListener('click', toggleType)
);


 function toggleType() {
   let input = document.getElementById('id_password');
   console.log(input);
   let show_pass=document.getElementsByClassName('fa-regular fa-eye-slash');
   let hide_pass=document.getElementsByClassName('fa-regular fa-eye');
   console.log(show_pass)
    if (input.type === 'password') {
      
        input.type = 'text';
        for(let i=0; i<show_pass.length; i++)show_pass[i].style.display='block';
        for(let i=0; i<hide_pass.length; i++)hide_pass[i].style.display='none';
        
      
    } else {
        input.type = 'password';
        for(let i=0; i<show_pass.length; i++)show_pass[i].style.display='none';
        for(let i=0; i<hide_pass.length; i++)hide_pass[i].style.display='block';
    }
} */