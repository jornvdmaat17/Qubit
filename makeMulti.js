var multiCount = 0;

$(document).ready(function(){  
    var acc = document.getElementById("acc");
    $('#multiCount').on('input',function(e){
        multiCount = $('#multiCount').val();
        while (acc.firstChild) {
            acc.removeChild(acc.firstChild);
        }
        for(i = 0; i < multiCount; i++){
            var inf = document.createElement("form");
            inf.setAttribute('id',("multi" + i));

            
            var paulix = document.createElement("input");
            inf.appendChild(paulix);
            inf.appendChild(document.createElement("br"));
            inf.appendChild(document.createElement("br"));

            var pauliy = document.createElement("input");
            inf.appendChild(pauliy);
            inf.appendChild(document.createElement("br"));
            inf.appendChild(document.createElement("br"));

            var pauliz = document.createElement("input");
            inf.appendChild(pauliz);
            inf.appendChild(document.createElement("br"));
            inf.appendChild(document.createElement("br"));

            var hadamard = document.createElement("input");
            inf.appendChild(hadamard);
            inf.appendChild(document.createElement("br"));
            inf.appendChild(document.createElement("br"));

            var sqrtNot = document.createElement("input");
            inf.appendChild(sqrtNot);
            inf.appendChild(document.createElement("br"));
            inf.appendChild(document.createElement("br"));

            var rphi = document.createElement("input");
            inf.appendChild(rphi);
            inf.appendChild(document.createElement("br"));
            inf.appendChild(document.createElement("br"));




            acc.appendChild(inf);
        }
    });    
});



function make(){
    console.log($("#multiCount").val());
}
