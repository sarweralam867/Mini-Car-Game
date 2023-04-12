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

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    colorSet(3, 236, 252) #konokichur color set (RGB)
    #call the draw methods here

    #circles
    radius = 90
    total_inside_circle = 20
    originX = 600
    originY = 600
    #Circle.All_Circles(radius, total_inside_circle,originX,originY)

    # Lines
    glPointSize(20)
    MIDpoint.MidPoint(290,0,290,1000)
    #MIDpoint.MidPoint(200,300,800,800)

    glutSwapBuffers()




glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(600, 1000) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"G5: Mini Car Game") #window name
glutDisplayFunc(showScreen)

glutMainLoop()