PARTICLE_NUM = 100

LINE_COLOR = "255,255,255"
LINE_THICKNESS = 1.5

DISTANCE_BETWEEN_PARTICLE = 130

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
    

    mousepos.x=event.pageX
    mousepos.y=event.pageY

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

function drawLines(c,x,y, x2, y2,color="rgb(0,0,0)",thick=5,dashed=[]){
    c.strokeStyle = color
    c.lineWidth = thick
    c.setLineDash(dashed);
    c.beginPath();
    c.moveTo(x, y)
    c.lineTo(x2,y2)
    c.stroke()
    c.closePath()
    c.setLineDash([]);
}

function dist(x1, x2, y1,y2){
    return ((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))**.5
}


class Particle {
    constructor(x,y,velx,vely,r){
        this.x = x
        this.y = y
        this.r = r

        this.vel = {x:velx,y:vely}

        this.alpha = 1
    }

    checkBorder(){
        if (this.x  - this.r <= 0 || this.x  + this.r >= canvas.width) {
            if (this.x  + this.r >= canvas.width) this.x = canvas.width - this.r;
            if (this.x  - this.r <= 0) this.x = 0 + this.r;

            this.vel.x *= -1

        }
        if (this.y  + this.r >= canvas.height || this.y - this.r <= 0) {
             if (this.y  + this.r >= canvas.height) this.y = canvas.height - this.r;   
                if (this.y  - this.r <= 0) this.y = 0 + this.r;
                this.vel.y *= -1
    
        }
    }

    applyForce(){
        this.x += this.vel.x
        this.y += this.vel.y
    }
    
    update(particles){
        this.draw(particles)
        this.applyForce()
        this.checkBorder()
    }
    draw(particles){
        drawCircle(c,this.x,this.y,this.r,`rgba(255,255,255,${this.alpha}`)

        for(let i = 0; i<particles.length;i++){
            let part = particles[i]

            let distance = dist(part.x,this.x,part.y,this.y)
            if(distance<DISTANCE_BETWEEN_PARTICLE){
                drawLines(c,this.x,this.y,part.x,part.y,"rgba("+LINE_COLOR+","+String(1-(distance/DISTANCE_BETWEEN_PARTICLE))+")",LINE_THICKNESS)
                let mouseDist = dist(this.x,mousepos.x,this.y,mousepos.y)
                // if(mouseDist < DISTANCE_BETWEEN_PARTICLE)             drawLines(c,this.x,this.y,part.x,part.y,"rgba("+LINE_COLOR+","+mouseDist/150+")",LINE_THICKNESS)
                
            }
        }
    }
}

particles = []
for(let i = 0;i<PARTICLE_NUM;i++){
    particles.push(new Particle(Math.random()*canvas.width,Math.random()*canvas.height,Math.random()-0.5,Math.random()-0.5,Math.random()*3))
}

function animate(){
    c.fillStyle = "rgb(0,15,25)"
    c.fillRect(0,0,window.innerWidth, window.innerHeight)

    for(let i = 0;i<particles.length;i++){
        particles[i].update(particles)
    }
    
    
    requestAnimationFrame(animate);
}

animate()