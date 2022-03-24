let counterDisplayElem = document.querySelector('#counter-display');
let counterMinusElem = document.querySelector('#minus');
let counterPlusElem = document.querySelector('#plus');
let count = counterDisplayElem.value;

updateDisplay();

counterPlusElem.addEventListener("click",()=>{
    count++;
    updateDisplay();
}) ;

counterMinusElem.addEventListener("click",()=>{
    if (count<1){
        count = 0;
    }
    else{
        count--;
    }    
    updateDisplay();
});

function updateDisplay(){
    counterDisplayElem.value = count;
};