from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
def draw_points(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()
def Determine_Zone(x1, y1, x2, y2):
  dx = x2 - x1
  dy = y2 - y1
  zone = None
  if abs(dx) >=  abs(dy):
    if dx >= 0 and dy > 0:
      zone = 0
    elif dx < 0 and dy >= 0:
      zone = 3
    elif dx < 0 and dy < 0:
      zone = 4
    elif dx >= 0 and dy < 0:
      zone = 7
  else:
    if dx >= 0 and dy >= 0:
      zone = 1
    elif dx < 0 and dy >= 0:
      zone = 2
    elif dx < 0 and dy < 0:
      zone = 5
    elif dx >= 0 and dy < 0:
      zone = 6
  return zone

def Convert_To_Zone_Zero(x, y, zone):
    if zone == 0:
        pass
    elif zone == 1:
        x, y = y, x
    elif zone == 2:
        x, y = y, -x
    elif zone == 3:
        x, y = -x, y
    elif zone == 4:
        x, y = -x, -y
    elif zone == 5:
        x, y = -y, -x
    elif zone == 6:
        x, y = -y, x
    elif zone == 7:
        x, y = x, -y
    return x, y

def Convert_To_Original_Zone(x, y, zone):
    if zone == 0:
        pass
    elif zone == 1:
        x, y = y, x
    elif zone == 2:
        x, y = y, -x
    elif zone == 3:
        x, y = -x, y
    elif zone == 4:
        x, y = -x, -y
    elif zone == 5:
        x, y = -y, -x
    elif zone == 6:
        x, y = -y, x
    elif zone == 7:
        x, y = x, -y
    return x, y

def MidPoint(x1, y1, x2, y2):
  zone = Determine_Zone(x1, y1, x2, y2)
  x1, y1 = Convert_To_Zone_Zero(x1, y1, zone)
  x2, y2 = Convert_To_Zone_Zero(x2, y2, zone)
  dx = x2 - x1
  dy = y2 - y1
  d = 2*dy - dx
  E = 2*dy
  NE = 2*(dy - dx)
  x = x1
  y = y1

  while (x < x2):
    a, b = Convert_To_Original_Zone(x, y, zone)
    draw_points(a, b)
    if d>0:
      d+= NE
      y=y+1
      x+=1
    else:
      d += E
      x+=1

