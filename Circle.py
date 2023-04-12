from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_points(x,y):
    glPointSize(2) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()

def eight_way_circlePoints(x, y, x0, y0):
  draw_points(x + x0, y + y0) #0
  draw_points(y + x0, x + y0) #1
  draw_points(-y + x0, x + y0) #2
  draw_points(-x + x0, y + y0) #3
  draw_points(-x + x0, -y + y0) #4
  draw_points(-y + x0, -x + y0) #5
  draw_points(y + x0, -x + y0) #6
  draw_points(x + x0, -y + y0) #7

def MidpointCircle(x0, y0, r):
  x = 0
  y = r
  d = 1 - r
  eight_way_circlePoints(x, y, x0, y0)
  while x < y:
    if d < 0:  # East
      d += ((2*x)+3)
      x += 1
    else:      #South East
      d += (2*x) - (2*y) + 5
      x += 1
      y -= 1
    eight_way_circlePoints(x, y, x0, y0)

import math
def All_Circles(r,n):
  MidpointCircle(250,250,r)
  a = r
  r = a // 2
  theta = (math.pi*2) / n
  i = 0
  while i <= n:
    x = r*math.cos(theta*i)
    y = r*math.sin(theta*i)
    MidpointCircle(x+250, y+250, r)
    i += 1

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 1.0) #konokichur color set (RGB)
    #call the draw methods here
    radius = 200
    total_inside_circle = 8
    All_Circles(radius,total_inside_circle)

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)
glutMainLoop()