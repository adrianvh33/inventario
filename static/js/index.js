function EnableDisableTB() {
    let tienda = document.querySelector("#radio_0");
    let bloque2= document.querySelector("#radio_1");
    let bloque5= document.querySelector("#radio_2");
    let counterMinusElem = document.querySelector('#minus');
    let counterPlusElem = document.querySelector('#plus');
    let count = 0
    let displayTienda = document.querySelector('#counter-display1');
    let displayBloque2 = document.querySelector('#counter-display2');
    let displayBloque5 = document.querySelector('#counter-display3');
    if(tienda.checked){
        //displayTienda.disabled=false;
        display = displayTienda
        count = display.value;
    }

    if(bloque2.checked){
        //displayBloque2.disabled=false;
        display = displayBloque2
        count = display.value;
        //displayTienda.disabled=true;
        //displayBloque5.disabled=true;
    }

    if(bloque5.checked){
        //displayBloque5.disabled=false;
        display = displayBloque5
        count = display.value;
        //displayTienda.disabled=true;
        //displayBloque2.disabled=true;
        
    }
    counterPlusElem.addEventListener("click",()=>{
        console.log('click +')
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
        display.value = count;
    };

    updateDisplay(); 
}
