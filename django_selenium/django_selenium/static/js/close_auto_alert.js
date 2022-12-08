let div=document.getElementById('close_success_message');
let timer; // пока пустая переменная
let x =5; // стартовое значение обратного отсчета
let span = document.getElementById("timer");

if(div) {
 
    countdown();
}
 // вызов функции
function countdown(){ // функция обратного отсчета
  span.innerHTML = x;
  x--; // уменьшаем число на единицу
  if (x<0){
    clearTimeout(timer); // таймер остановится на нуле
    setTimeout(()=> {
      div.remove();
      
    },1000)
  }
  else {
    timer = setTimeout(countdown, 1000);
  }
}



