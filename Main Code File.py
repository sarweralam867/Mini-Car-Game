import Circle
import MIDpoint
import pygame
import random
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from pygame.locals import *
pygame.init()
display_width = 600
display_height = 800
displays=pygame.display.set_mode((display_width,display_height))

def colorSet(a,b,c):
    return glColor3f(a/255, b/255, c/255)

def pixel(a):
    return glPointSize(a)





def road():
    pixel(20)
    colorSet(157, 162, 171)
    MIDpoint.MidPoint(0, -600, 0, 600)

    displacement = 0
    pixel(25)
    colorSet(255, 255, 255)
    for i in range(10):
        MIDpoint.MidPoint(-150, 500 - displacement, -150, 450 - displacement)
        MIDpoint.MidPoint(150, 500- displacement, 150, 450 - displacement)
        displacement += 250

def circle(d=0):
    radius = 50
    total_inside_circle = 100
    colorSet(156, 3, 11)
    originX = -225 + d
    originY = 500
    Circle.All_Circles(radius, total_inside_circle, originX, originY)

def box(d=0):
    colorSet(156, 3, 11)
    pixel(100)
    MIDpoint.MidPoint(-75+d, 500, -75+d, 540)


def car(d=0):
    colorSet(157, 255, 0)
    pixel(100)
    MIDpoint.MidPoint(0 + d, -340, 0 + d, -300)


def minicargame():
    display = (600,1000) #Window Size
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(25,1, 0.1, 50.0)
    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        road()
        circle()
        box()
        circle(300)
        box(300)
        car()
        pygame.display.flip()
        pygame.time.wait(10)
minicargame()