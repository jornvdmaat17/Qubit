var multiCount = 0;

$(document).ready(function(){  
    var acc = document.getElementById("acc");
    $('#multiCount').on('input',function(e){
        multiCount = $('#multiCount').val();
        while (acc.firstChild) {
            acc.removeChild(acc.firstChild);
        }
        if(multiCount < 11){
            for(i = 0; i < multiCount; i++){
                var f = document.createElement("form");
                var inf = document.createElement("fieldset");
                var title = document.createElement("h1");
                var txt = document.createTextNode("MultiQubit " + (i + 1) + ": ");
                title.setAttribute("class", "multiQubitTitle");
                title.appendChild(txt);            
                inf.appendChild(title);
                inf.setAttribute('id',("multi" + i));
                inf.appendChild(document.createElement("br"));
                inf.appendChild(document.createElement("br"));
                
                //Pauli-X
                var xq = document.createElement("div");
                xq.setAttribute("class", ("inputdiv"));
                xq.appendChild(document.createElement("label").appendChild(document.createTextNode("Qubits: ")));
                var qubits = document.createElement("input");
                qubits.setAttribute("type", "text");
                qubits.setAttribute('id', ("qubits" + i ));
                qubits.setAttribute('class', "ininf");
                xq.appendChild(qubits);
                inf.appendChild(xq);
    
                inf.appendChild(document.createElement("br"));
                inf.appendChild(document.createElement("br"));
    
                //Pauli-X
                var xdiv = document.createElement("div");
                xdiv.setAttribute("class", ("inputdiv"));
                xdiv.appendChild(document.createElement("label").appendChild(document.createTextNode("Pauli-X indeces: ")));
                var paulix = document.createElement("input");
                paulix.setAttribute("type", "text");
                paulix.setAttribute('id', ("paulix" + i ));
                paulix.setAttribute('class', "ininf");
                xdiv.appendChild(paulix);
                inf.appendChild(xdiv);
    
                inf.appendChild(document.createElement("br"));
                inf.appendChild(document.createElement("br"));
    
                //Pauli-Y
                var ydiv = document.createElement("div");
                ydiv.setAttribute("class", ("inputdiv"));
                ydiv.appendChild(document.createElement("label").appendChild(document.createTextNode("Pauli-Y indeces: ")));
                var pauliy = document.createElement("input");
                pauliy.setAttribute("type", "text");
                pauliy.setAttribute('id', ("pauliy" + i ));
                pauliy.setAttribute('class', "ininf");
                ydiv.appendChild(pauliy);
                inf.appendChild(ydiv);
    
                inf.appendChild(document.createElement("br"));
                inf.appendChild(document.createElement("br"));            
    
                //Pauli-Z
                var zdiv = document.createElement("div");
                zdiv.setAttribute("class", ("inputdiv"));
                zdiv.appendChild(document.createElement("label").appendChild(document.createTextNode("Pauli-Z indeces: ")));
                var pauliz = document.createElement("input");
                pauliz.setAttribute("type", "text");
                pauliz.setAttribute('id', ("pauliz" + i ));
                pauliz.setAttribute('class', "ininf");
                zdiv.appendChild(pauliz);
                inf.appendChild(zdiv);
    
                inf.appendChild(document.createElement("br"));
                inf.appendChild(document.createElement("br"));
    
                //Hadamard
                var hdiv = document.createElement("div");
                hdiv.setAttribute("class", ("inputdiv"));
                hdiv.appendChild(document.createElement("label").appendChild(document.createTextNode("Hadamard indeces: ")));
                var hadamard = document.createElement("input");
                hadamard.setAttribute("type", "text");
                hadamard.setAttribute('id', ("hadamard" + i ));
                hadamard.setAttribute('class', "ininf");
                hdiv.appendChild(hadamard);
                inf.appendChild(hdiv);
                inf.appendChild(document.createElement("br"));
                inf.appendChild(document.createElement("br"));
    
                //Sqrtnot
                var sdiv = document.createElement("div");
                sdiv.setAttribute("class", ("inputdiv"));
                sdiv.appendChild(document.createElement("label").appendChild(document.createTextNode("SqrtNot indeces: ")));
                var sqrt = document.createElement("input");
                sqrt.setAttribute("type", "text");
                sqrt.setAttribute('id', ("sqrt" + i ));
                sqrt.setAttribute('class', "ininf");
                sdiv.appendChild(sqrt);
                inf.appendChild(sdiv);
    
                inf.appendChild(document.createElement("br"));
                inf.appendChild(document.createElement("br"));
    
                //Rphi
                var rdiv = document.createElement("div");
                rdiv.setAttribute("class", ("inputdiv"));
                rdiv.appendChild(document.createElement("label").appendChild(document.createTextNode("Rphi indeces: ")));
                var rphi = document.createElement("input");
                rphi.setAttribute("type", "text");
                rphi.setAttribute('id', ("rphi" + i ));
                rphi.setAttribute('class', "ininf");
                rdiv.appendChild(rphi);
                rdiv.appendChild(document.createElement("br"));
                rdiv.appendChild(document.createElement("label").appendChild(document.createTextNode("Rotation variable PI/")));            
                var rotat = document.createElement("input");
                rotat.setAttribute("type", "text");
                rotat.setAttribute('id', ("rotat" + i ));
                rotat.setAttribute('class', "ininf");
                rdiv.appendChild(rotat);
                inf.appendChild(rdiv);
    
                inf.appendChild(document.createElement("br"));
                inf.appendChild(document.createElement("br"));
    
    
                //Print
                var pdiv = document.createElement("div");
                pdiv.setAttribute("class", "inputdiv");
                pdiv.appendChild(document.createElement("label").appendChild(document.createTextNode("Print steps? ")));
                var pin = document.createElement("input");
                pin.setAttribute("type", "text");
                pin.setAttribute("id", ("pin" + i));
                pin.setAttribute('class', "ininf");
                pdiv.appendChild(pin);
                inf.appendChild(pdiv);
    
    
                f.appendChild(inf);
                acc.appendChild(f);
            }
        }else{
            alert("Vul een waarde tussen 1 en 10 in");
            multiCount = $('#multiCount').val(1);
        }
    });    
});



function make(){
    var json = '{\n\t"multi": [\n';
    for(i = 0; i < multiCount; i++){
        var qubits = $('#qubits' + i).val();
        if(qubits == []){
            alert("Er zijn geen qubits ingevoerd bij MultiQubit " + (i + 1));
            continue;
        }
        var qLen = qubits.length;
        if(!Array.isArray($('#qubits' + i).val()) && qLen == 1){
            alert("Qubit heeft een verkeerde syntax");
            continue;
        }
        if(qubits.substring(qubits.length - 1, qubits.length) != "]"){
            
            alert("Qubit heeft een verkeerde syntax");
            continue;
            
        }
        var rotat = 1;
        var print = false;
        var qubits = $('#qubits' + i).val();
        var paulix = $('#paulix' + i).val();
        var pauliy = $('#pauliy' + i).val();
        var pauliz = $('#pauliz' + i).val();
        var hadamard = $('#hadamard' + i).val();
        var sqrt = $('#sqrt' + i).val();
        var rphi = $('#rphi' + i).val();
        if($('#print' + i).val() != ""){
            print = $('#print' + i).val();
        }
        if($('#rotat' + i).val() != ""){
            rotat = $('#rotat' + i).val();
        }    
       
        json += '\t\t{\n\t\t\t"qubits" : [' + qubits + '],\n';
        json += '\t\t\t"paulix" : [' + paulix + '],\n';
        json += '\t\t\t"pauliy" : [' + pauliy + '],\n';
        json += '\t\t\t"pauliz" : [' + pauliz + '],\n';
        json += '\t\t\t"hadamard" : [' + hadamard + '],\n';
        json += '\t\t\t"sqrnot" : [' + sqrt + '],\n';
        json += '\t\t\t"rphi" : {\n\t\t\t\t"index" : [' + rphi + '],\n';
        json += '\t\t\t\t"phi" : ' + rotat + '\n\t\t\t},\n';
        json += '\t\t\t"print" : "' + print + '"\n';
        if(i + 1 == multiCount){
            json += '\t\t}\n'
        }else{
            json += '\t\t},\n'
        }     
    }
    json += '\t]\n}'
    $('#jsonout').val(json);
    document.getElementById("jsonout").hidden = false;
}
