function multi(){
    var n1 = document.myForm.t1.value;
    var n2 = document.myForm.t2.value;
    var s = n1 * n2;
    document.myForm.result.value = s;
}
function summa(){
    var n1 = parseInt(document.myForm.t1.value);
    var n2 = parseInt(document.myForm.t2.value);
    var s = n1 + n2;
    document.myForm.result.value = s;
}
function subtract(){
    var n1 = parseInt(document.myForm.t1.value);
    var n2 = parseInt(document.myForm.t2.value);
    var s = n1 - n2;
    document.myForm.result.value = s;
}
function division(){
    var n1 = parseInt(document.myForm.t1.value);
    var n2 = parseInt(document.myForm.t2.value);
    var s = n1 / n2;
    document.myForm.result.value = s;
}