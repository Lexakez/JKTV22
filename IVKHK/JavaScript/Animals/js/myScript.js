$(document).ready(function(){
    for(var i=0; i<category.length;i++){
        var li=document.createElement('li');
li.innerHTML=('<a href ="#" onclick="myContent(`'+category[i] +'`)" >'+category[i]+'</a>');
document.getElementById("menu").appendChild(li);
    }
});

function myContent(val){
    var header='<h2>'+val+'</h2>';
    var text='';
    var controll = false;
    for(var i=0; i<animals.length;i++){
        if(val==animals[i].classname){
            text+='<div style="float:left;">';
            text+='<img src = "images/'+animals[i].image+'" style="margin:5px;">"';
            text+='<p>'+animals[i].name+'</p>';
            text+='<p><a href="#" onClick="Detail(\''+animals[i].name +  '\')"> Подробнее ... </a></p>';
            text+='</div>';
            controll=true;
        }
    }

    if(controll==true)
        $("#content").html(header+text);
    else
        $("#content").html(header+"Данных нет");      
};

function Detail (item) {

    var text='';
    var controll=false;
    for(var i=0; i<animals.length;i++) {
        if (item==animals[i].name) { 
            var header='<h2>'+animals[i].classname+': '+animals[i].name+'</h2>';
            text+='<div style="float:left;">';
            text+='<img src="images/'+animals[i].image+'" style="margin:5px;">';  
            text+='<p>'+animals[i].description+'</p>';
            text+='<p><a href="#" onClick="myContent (\''+animals[i].classname +'\')">Back categories</a></p>';
            text+='</div>';
            controll=true;
        }
    }
    if (controll==true)
        $("#content").html (header+text);
    else
        $("#content").html (header+"Данных нет");
}