import Circle
import MIDpoint
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_points(x, y):
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
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
    radius = 100
    total_inside_circle = 20
    originX = 200
    originY = 300
    #Circle.All_Circles(radius, total_inside_circle,originX,originY)

    # Lines
    MIDpoint.MidPoint(300,0,300,800)

    glutSwapBuffers()




glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(600, 800) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"G5: Mini Car Game") #window name
glutDisplayFunc(showScreen)

glutMainLoop()