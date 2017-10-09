function validar(valor){
    if (valor == null || valor.length == 0) {
        alert('[ERROR] Uno de los campos esta vacio');
        return false;
    }
    if(isNaN(parseInt(valor))) {
    	alert('[ERROR] Uno de los campos no es un numero');
  		return false;
	}
	if ((operacion == '/') && (operando2 == '0')){
		alert('[ERROR] No se puede dividir por 0');
  		return false;
	}
	else{
		return true;
	}
};

function refresca(){
	alert('ESTO E SUNA ALERTA');
	document.getElementById("op1").value ='';
	document.getElementById("op2").value ='';
}

function calcula(operacion) {
  var operando1 = document.getElementById("op1").value;
  var operando2 = document.getElementById("op2").value;

	if(validar(operando1) && validar(operando2)){
	  var result = eval(operando1 + operacion + operando2);
	  document.getElementById("resultado").innerHTML = result;
	}
}

/*****

- Si no son números?
- Si el divisor es 0?
- Si queremos resetear

- Mejoras a realizar ahora
-- solo habilitemos el control si los operandos son correctos
-- el resultado, si es negativo, mostrarlo en rojo, si es positivo, en verde (modificando el atributo "style")


*****/
