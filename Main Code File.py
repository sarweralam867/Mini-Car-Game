import Circle
import MIDpoint
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def iterate():
    glViewport(0, 0, 600, 1000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 600, 0.0, 1000, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def colorSet(a,b,c):
    return glColor3f(a/255, b/255, c/255)

def pixel(a):
    return glPointSize(a)

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    157, 162, 171
    #call the draw methods here

    #circles
    radius = 50
    total_inside_circle = 100
    d= 0
    colorSet(156, 3, 11)
    for i in range(2):
        originX = 75
        originY = 75 + d
        Circle.All_Circles(radius, total_inside_circle,originX,originY)

        originX = 75+150
        originY = 75 + d + 150
        Circle.All_Circles(radius, total_inside_circle, originX, originY)

        originX = 75 + 300
        originY = 75 + d + 300
        Circle.All_Circles(radius, total_inside_circle,originX,originY)

        originX = 75+450
        originY = 75 + d + 450
        Circle.All_Circles(radius, total_inside_circle, originX, originY)

        d += 500

    # Lines
    pixel(20)
    colorSet(157, 162, 171)
    MIDpoint.MidPoint(290,0,290,1000)

    displacement = 0
    pixel(25)
    colorSet(255, 255, 255)
    for i in range(10):
        MIDpoint.MidPoint(150, 0+displacement, 150, 50+displacement)
        MIDpoint.MidPoint(450, 0 + displacement, 450, 50 + displacement)
        displacement += 250

    glutSwapBuffers()




glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(600, 1000) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"G5: Mini Car Game") #window name
glutDisplayFunc(showScreen)

glutMainLoop()