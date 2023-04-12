from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
def draw_points(x,y):
    glPointSize(2)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
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
def All_Circles(r,n, x1, x2):
  MidpointCircle(x1, x2,r)
  a = r
  r = a // 2
  theta = (math.pi*2) / n
  i = 0
  while i <= n:
    x = r*math.cos(theta*i)
    y = r*math.sin(theta*i)
    MidpointCircle(x+x1, y+x2, r)
    i += 1




