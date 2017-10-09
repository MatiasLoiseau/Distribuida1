
function calcula(operacion) {
  var operando1 = $("#op1").val();
  var operando2 = $("#op2").val();
  var result = eval(operando1 + operacion + operando2);
  $("#resultado").html(result);
}
