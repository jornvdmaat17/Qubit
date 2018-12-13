let startc = 100;
let space = 20;
let size = 60;

function setup(){
    createCanvas(600, 600);
}

function draw(){
    /*
    Menu for choosing
    */

    line(startc, 0, startc, 600);

    x = new vis(0,0,size,size, "X");
    x.display();
}

function vis(x0, y0, x1, y1, txt){
    this.x0 = x0;
    this.y0 = y0;

    this.x1 = x1;
    this.y1 = y1;

    this.txt = txt;

    this.display = function(){        
        
        stroke(1);
        rect(x0 + startc + space, y0, x1, y1);
        textSize(60);
        text(txt, x0 + startc + size,  y0 + size/2);  
    };
}