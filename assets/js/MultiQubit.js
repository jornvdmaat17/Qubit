let startoffset = 100;
let space = 20;
let size = 60;
let lspace = 10;

var pXI;

function setup(){
    createCanvas(600, 600);
    
}

function draw(){
    /*
    Menu for choosing
    */

    line(startoffset, 0, startoffset, 600);
    var testC = new pauliX(50,50);
    testC.display();
}

function pauliX(x, y){
    this.x = x;
    this.y = y;

    this.display = function(){
        rect(this.x, this.y, size, size);
        line(this.x + lspace, this.y + lspace, this.x + size - lspace, this.y + size - lspace );
        line(this.x + lspace, this.y + size + lspace, this.x + size + lspace, this.y - size + lspace);
    };

};