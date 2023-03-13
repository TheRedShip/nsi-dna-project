let canvas = document.querySelector("canvas")

canvas.width = window.innerWidth
canvas.height = window.innerHeight

var c = canvas.getContext("2d");

canvas.addEventListener('contextmenu', (ev)=>{
    ev.preventDefault();
});


let mousepos = {x:0,y:0, prevx:0, prevy:0,realx:0,realy:0}
let handleMousemove = (event) => {
    mousepos.prevx = mousepos.x
    mousepos.prevy = mousepos.y

    mousepos.realx=event.clientX
    mousepos.realy=event.clientY

    mousepos.x = currentTransformedCursor.x
    mousepos.y = currentTransformedCursor.y
};
document.addEventListener('mousemove', handleMousemove);

let mouseClick = false;
let handleMouseclick = (event) => {
    event.preventDefault()
    if(event.buttons==1) mouseClick = true
    else mouseClick = false
};
canvas.addEventListener('mousedown', handleMouseclick);
canvas.addEventListener('mouseup', handleMouseclick);



function drawCircle(c,x,y,r,color){
    c.fillStyle = color
    c.beginPath();
    c.arc(x,y,r,0,Math.PI*2)
    c.fill()
    c.closePath()
}

class Particle {
    constructor(x,y,r){
        this.x = x
        this.y = y
        this.r = r

        this.vel = {x:0,y:0}

        this.alpha = 1
    }

    checkBorder(){
        if (this.x + this.vel.x - this.r <= 0 || this.x + this.vel.x + this.r >= screenx) {
            if (this.x + this.vel.x + this.r >= canvas.width) this.x = canvas.width - this.r;
            if (this.x + this.vel.x - this.r <= 0) this.x = 0 + this.r;

            this.vel.x *= -1

            if (this.contraint) this.vel.x *= 0.60
            if (this.friction) this.vel.x *= ballConstant.collisionFriction
        }
    }

    applyForce(){
        this.x += this.vel.x
        this.y += this.vel.y
    }
    
    update(){
        this.draw()
        this.applyForce()
    }
    draw(){
        drawCircle(c,this.x,this.y,this.r,`rgba(255,255,255,${alpha}`)
    }
}


function animate(){
    c.fillStyle = "rgb(0,15,25)"
    c.fillRect(0,0,window.innerWidth, window.innerHeight)
    x+=1
    drawSimpleCircle(c,x,50,50,"rgb(255,255,255)")
    
    requestAnimationFrame(animate);
}

animate()