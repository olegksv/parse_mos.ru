let div1=document.getElementById('success_register_message');
let timer1; // пока пустая переменная
let y =5; // стартовое значение обратного отсчета
let span1 = document.getElementById("timer");

if(div1) {
 
    countdown1();
}
 // вызов функции
function countdown1(){ // функция обратного отсчета
  span1.innerHTML = y;
  y--; // уменьшаем число на единицу
  if (y<0){
    document.location.href='/login/'
    clearTimeout(timer1); // таймер остановится на нуле
    setTimeout(()=> {
      div1.remove();
      
    },1000)
  }
  else {
    timer1 = setTimeout(countdown1, 1000);
  }
}

