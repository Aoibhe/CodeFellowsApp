#write a prgram that draws a winter scene with a tree and a snow man

from visual import *
from visual.text import *
from visual.controls import *
import time
import random


# nondenominational winter holiday ie christmas
def main():

    scene.title = "merry christmas"
    scene.height = 600
    scene.width = 600
    scene.range = (18,18,18)
    scene.center = (0,3,0)

    Nslabs = 8
    R = 3.1
    w = 10.0
    d = 5.0
    h = 10.0


# The ground and trunk
    box(pos=(0,-0.1,0),length=24,height=0.2,width=24, color=(10,10,10))
    cylinder(pos=(0,0,0),axis=(0,h-1,0), radius=.5, color=(4,1,0))
    


# leaves
    Nwires = 50
    for i in range(Nwires):
        theta = i*2*pi/Nwires
        cylinder(pos=(0,(h+1),0), axis=(R*cos(theta),-h-0.1,R*sin(theta)),
             radius=0.2, color=(0,7,0))
    Nwires1 = 25
    for i in range(Nwires1):
        theta = i*2*pi/Nwires1
        cylinder(pos=(0,(h+1),0), axis=((2)*cos(theta),-4,2*sin(theta)),
             radius=.2, color=(0,10,0))
    Nwires2 = 70
    for i in range(Nwires2):
        theta = i*2*pi/Nwires2
        cylinder(pos=(0,(h+1),0), axis=((2.8)*cos(theta),-7,(2.8)*sin(theta)),
             radius=0.2, color=(0,3,0))
# star
    sphere(pos=(0,h+1.3,0), radius = .3, color=(5,5,0))
    


#snowman
    y1 = 1
    y2 = 8*h
    v0 = 8
    vball0 = 2.5*v0
    vball = vball0
    ball = sphere(pos=(5,(y1-.2),4), radius=y1, color=(1,2,3))
    rbaseball = 0.3
    vbaseball0 = 3*v0
    
    vball1 = 2.5*(v0-1)
    vball1 = vball0
    ball1 = sphere(pos=(5,(y1+1),4), radius=(y1-.2), color=(1,2,3))
    rbaseball1 = 0.4
    vbaseball1 = 3*(v0-1)

    vball2 = 2.5*(v0-3)
    vball2 = vball0
    ball2 = sphere(pos=(5,(y1+2),4), radius=(y1-.5), color=(1,2,3))
    rbaseball2 = 0.5
    vbaseball2 = 3*(v0-2)

    cylinder (pos=(5, (y1+2.4), 4), axis=(0, .5, 0),
              radius=.4, color=(1,1,1))
    cylinder (pos=(5, (y1+2.4), 4), axis=(0, .1, 0),
              radius=.6, color=(1,1,1))
    eye1=sphere(pos=(5.2, (y1+2.1), 4.5), radius=.07, color=(0,0,0))
    eye2=sphere(pos=(4.8, (y1+2.1), 4.5), radius=.07, color=(0,0,0))

    nose=cylinder (pos =(5, (y1+2), 4), axis=(0, 0, .8), radius=.06,
                   color=(7,2,0))
    rarm=cylinder (pos = (5, (y1+1.5), 4), axis = (1.5, -.5, 0), radius=.07,
                   color=(4,1,0))
    larm=cylinder (pos = (5, (y1+1.5), 4), axis = (-1.5, -.5, 0), radius=.07,
                   color=(4,1,0))
#snow
    y1 = 0
    y2 = 20
    x1 = -3
    z1 = 4
    ball = sphere(pos=(x1,y2,z1), radius=.3, color=color.white)
    ball1 = sphere(pos=(-4,y2+1,3), radius=.3, color=color.white)
    ball2 = sphere(pos=(3,y2+2,-4), radius=.3, color=color.white)
    ball3 = sphere(pos=(6,y2+3,0), radius=.3, color=color.white)
    ball4 = sphere(pos=(0,y2+4,-4), radius=.3, color=color.white)
    ball5 = sphere(pos=(2,y2+5,9), radius=.3, color=color.white)
    ball6 = sphere(pos=(9,y2+6,5), radius=.3, color=color.white)
    ball7 = sphere(pos=(9,y2+7,9), radius=.3, color=color.white)

    while 1:
     #Run the snow
        ball.pos.y = ball.pos.y-1
        ball1.pos.y = ball.pos.y-.1
        ball2.pos.y = ball.pos.y-2
        ball3.pos.y = ball.pos.y-2.5
        ball4.pos.y = ball.pos.y-3
        ball5.pos.y = ball.pos.y-1
        ball6.pos.y = ball.pos.y-1.25
        ball7.pos.y = ball.pos.y-1.75
        if ball.pos.y >= 19:
            y2 = y2-.1
        if ball.pos.y <= 0:
            ball.pos.y = 20


        rate(10)


main()

