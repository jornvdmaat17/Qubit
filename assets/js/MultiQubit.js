let startoffset = 100;
let space = 20;
let size = 60;

function setup(){
    createCanvas(600, 600);
    
}

function draw(){
    /*
    Menu for choosing
    */

    line(startoffset, 0, startoffset, 600);
    var testC = new canvImg(10, 10, 40, 40, 'assets/img/pauliy.png');
    testC.display();
}

function canvImg(x, dX, y, dY, imgPath){
    this.x = x;
    this.dX = dX;
    this.y = y;
    this.dY = dY;
    this.imgPath = imgPath;
    var img = loadImage(imgPath);

    this.display = function(){
        // image(img, x, y, dX, dY);
        rect(this.x, this.dX, this.y, this.dY);
    };

};