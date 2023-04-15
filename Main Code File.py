import Circle
import MIDpoint
import pygame
import random
import time
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from pygame.locals import *


def colorSet(a,b,c):
    return glColor3f(a/255, b/255, c/255)

def pixel(a):
    return glPointSize(a)

def road():
    pixel(20)
    colorSet(157, 162, 171)
    MIDpoint.MidPoint(0, 400, 0, -800)

    displacement = 0
    pixel(25)
    colorSet(255, 255, 255)
    for i in range(8):
        MIDpoint.MidPoint(-150, 400 - displacement, -150, 350 - displacement)
        MIDpoint.MidPoint(150, 400- displacement, 150, 350 - displacement)
        displacement += 300

def circle(d=0,dx=0):
    radius = 50
    total_inside_circle = 100
    colorSet(156, 3, 11)
    originX = -225 + d
    originY = 800 -dx
    Circle.All_Circles(radius, total_inside_circle, originX, originY)

def box(d=0):
    colorSet(156, 3, 11)
    pixel(60)
    MIDpoint.MidPoint(-75+d, 700, -75+d, 840)
    colorSet(5, 30, 71)


def car(d=0):
    colorSet(157, 255, 0)
    pixel(60)
    MIDpoint.MidPoint(0 + d, -400, 0 + d, -360)
    colorSet(157, 255, 0)


def minicargame():
    pygame.init()
    clock = pygame.time.Clock()
    display = (600,800) #Window Size
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45,(display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        road()
        circle()
        circle(300)
        box()
        box(300)
        car()



        pygame.display.flip()
        pygame.time.wait(10)
minicargame()