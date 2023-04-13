let taps = 0;


function fallDown(img) {
    taps++;
    if (taps === 5) {
        img.style.transform = "translate(0px, 1000px) rotate(720deg)";
        setTimeout(function () {
            img.style.display = "none";
            setTimeout(function () {
                img.style.display = "";
                img.style.transform = "translate(0px, 0px) rotate(0deg)";
                taps = 0;
            }, 1500);
        }, 1000);
    }
}



function clickButton(btn){
    btn.style.transform = "translateY(4px)";
    setTimeout(function(){
        btn.style.transform = "";
    }, 200);
}

const centeredElement = document.getElementById("up_site");
window.addEventListener("scroll", () => {
    if (window.pageYOffset > 500) {
        centeredElement.style.display = "block";
        centeredElement.style.transform = "translateY(0px)";
    } else {
        // centeredElement.style.display = "none";
        centeredElement.style.transform = "translateY(-100px)";
    }
});