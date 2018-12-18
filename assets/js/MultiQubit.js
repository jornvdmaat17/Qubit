// Constants
let startoffset = 100;
let space = 20;
let size = 60;
let lspace = 10;
let strokeOffset = 2;
let sphereRadius = 10;
let duplicateOffset = 5;

// Global
var paulix;
var pauliy;
var pauliz;
var onScreen = [];
var startScreen = [];
var dragging;
var newScreenObject;
var isLine = false;
var startedLineObjIndex;
var startedLineDotSide;

function preload(){
    paulix = loadImage('assets/img/paulix.png');
    pauliy = loadImage('assets/img/pauliy.png');
    pauliz = loadImage('assets/img/pauliz.png')
}

function setup(){
    createCanvas(600, 600);
    var startPaulix = new ImageRect(0 + space, 0, paulix, "paulix");
    var startPauliy = new ImageRect(0 + space, 60 + space, pauliy, "pauliy");
    var startPauliz = new ImageRect(0 + space, 120 + space, pauliz, "pauliz");
    startScreen.push(startPaulix);
    startScreen.push(startPauliy);
    startScreen.push(startPauliz);    
}

function draw(){ 
    // if(newScreenObject != null){
    //     clear();
    // } 
    
    clear();

    for(i=0;i<startScreen.length;i++){
        startScreen[i].display();
    }
    stroke(strokeOffset);
    line(startoffset, 0, startoffset, 600);

    for(i=0;i<onScreen.length;i++){
        onScreen[i].display();
    }
    if(newScreenObject != null && !isLine){
        newScreenObject.setPos(mouseX - size/2, mouseY - size/2);
        newScreenObject.display();
    }
    if(newScreenObject != null && isLine){
        newScreenObject.setPos(mouseX, mouseY);
        newScreenObject.display();
    }

    onScreen.push(new inputQubit(200, 200));
}

function mousePressed(){
    for(i=0;i<startScreen.length;i++){
        if(startScreen[i].inRange()){
            newScreenObject = startScreen[i].duplicate();
            break;
        }
    }
    for(i=0;i<onScreen.length;i++){
        if(onScreen[i].leftDotInRange() && !onScreen[i].leftConnected){
            var tmp = onScreen[i].getLeftDot();
            newScreenObject = new Line(tmp[0], tmp[1], mouseX, mouseY);
            isLine = true;
            startedLineObjIndex = i;
            startedLineDotSide = "left";
        }
        if(onScreen[i].rightDotInRange() && !onScreen[i].rightConnected){
            var tmp = onScreen[i].getRightDot();
            newScreenObject = new Line(tmp[0], tmp[1], mouseX, mouseY);
            isLine = true;
            startedLineObjIndex = i;
            startedLineDotSide = "right";
        }
    }
}

function mouseReleased(){
    if(newScreenObject != null && !isLine){
        onScreen.push(newScreenObject);    
    }
    if(newScreenObject != null && isLine){
        for(i=0;i<onScreen.length;i++){
            if(!startedLineObjIndex == i){
                var found = false;
                if(onScreen[i].leftDotInRange() && !onScreen[i].leftConnected){
                    onScreen.push(newScreenObject);
                    onScreen[i].setLeftConnected(true);
                    found = true;
                }
                if(onScreen[i].rightDotInRange() && !onScreen[i].rightConnected){
                    onScreen.push(newScreenObject);
                    onScreen[i].setRightConnected(true);
                    found = true;
                }
                if(found){
                    if(startedLineDotSide == "left"){
                        onScreen[startedLineObjIndex].setLeftConnected(true);
                    }
                    if(startedLineDotSide == "right"){
                        onScreen[startedLineObjIndex].setRightConnected(true);
                    }
                    break;
                }
            }  
        }
        isLine = false;
    }
    startedLineObjIndex = null;
    startedLineDotSide = null;
    newScreenObject = null;
}

function ImageRect(x, y, img, name){
    this.x = x;
    this.y = y;
    this.img = img;
    this.name = name;
    this.leftConnected = false;
    this.rightConnected = false;

    this.display = function(){
        image(img ,this.x, this.y, size, size); 
        fill(0); 
        ellipse(this.x + 1, this.y + 1 + size / 2, sphereRadius);  
        ellipse(this.x - 1 + size, this.y + 1 + size / 2, sphereRadius);      
    }

    this.inRange = function(){
        if(mouseX >= this.x && mouseX <= this.x + size && mouseY >= this.y && mouseY<= this.y + size ){
            return true;
        }else{
            return false;
        }
    }

    //Todo
    this.leftDotInRange = function(){
        return (sq(mouseX - (this.x + 1)) + sq(mouseY - (this.y - 1 + size / 2))) < sphereRadius * sphereRadius;
    }

    this.rightDotInRange = function(){
        return sq(mouseX - (this.x - 1 + size)) + sq(mouseY - (this.y + 1 + size / 2)) < sphereRadius * sphereRadius;
    }

    this.getLeftDot = function(){
        return [this.x + 1, this.y - 1 + size / 2];
    }

    this.getRightDot = function(){
        return [this.x - 1 + size, this.y + 1 + size / 2];
    }

    this.duplicate = function(){
        return new ImageRect(this.x + 5, this.y + 5, img, name);
    }

    this.setPos = function(x , y){
        this.x = x;
        this.y = y;
    }

    this.setLeftConnected = function(left){
        this.leftConnected = left;        
    }

    this.setRightConnected = function(right){
        this.rightConnected = right;
    }
}

function Line(x, y, dX, dY){
    this.x = x;
    this.y = y;
    this.dX = dX;
    this.dY = dY;

    this.display = function(){
        strokeWeight(3);
        line(this.x, this.y, this.dX, this.dY);
        strokeWeight(1);
    }

    this.setPos = function(dX, dY){
        this.dX = dX;
        this.dY = dY;
    }

    this.leftDotInRange = function(){
        return false;
    }

    this.rightDotInRange = function(){
        return false;
    }
}

function inputQubit(x, y){
    this.x = x;
    this.y = y;
    this.alpha = createInput().position(this.x, this.y);
    this.beta = createInput().position(this.x, this.y + 23);

    this.display = function(){
        this.alpha.position(this.x, this.y);
        this.beta.position(this.x,this.y + 23);
    }

    this.setPos = function(x, y){
        this.x = x;
        this.y = y;
    }

    this.getAlphaValue = function(){
        return this.alpha.value();
    }

    this.getBetaValue = function(){
        return this.beta.value();
    }
}