

function myFunction() {
    let ubicacion = document.querySelector('input[name="ubicacion"]:checked');
    localStorage.setItem('ubicacionSaved',ubicacion.id);
 }

 function saveCheck(){
    const ubicacionSaved = localStorage.getItem('ubicacionSaved');
    if(ubicacionSaved){
        let ubicacion = document.querySelector(`#${ubicacionSaved}`);
        ubicacion.checked = true
    }
 }
 saveCheck()