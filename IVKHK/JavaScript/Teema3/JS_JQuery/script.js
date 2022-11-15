$(document).ready(function(){
    var controll = false;
    $("#but1").click(function(){
        if(controll == false){
            controll = true;
            $("#n1").hide(2000);
            $("#but1").html("Show Block1");
        }
        else{
            controll = false;
            $("#n1").show(2000);
            $("#but1").text("Hide Block1");
        }
    });
    $("#but2").click(function(){
        $("#n2").toggle(2500);
    });
    $("#n4").css('display','none');
    $("#n5").css('display','none');
    $("#but3").click(function(){
        $("#n3").fadeIn(500);
        $("#n4").hide();
        $("#n5").hide();
    });
    $("#but4").click(function(){
        $("#n4").fadeIn(500);
        $("#n3").hide();
        $("#n5").hide();
    });
    $("#but5").click(function(){
        $("#n5").fadeIn(500);
        $("#n3").hide();
        $("#n4").hide();
    });
    $("#result").text("Введено символов:" + $(this).val().length);
    $("#username").keyup(function(){
        var k = $(this).val().length;
        $("#result").text("Введено символов: " +k);
        var n = $("#username").attr('maxlength');
        $("#counter").text("Осталось для ввода: "+(n - k)+ " Из " +n);
    });
});