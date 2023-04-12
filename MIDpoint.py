from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_points(x, y):
    glPointSize(5) #pixel size. by default 1 thake
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


######## DIgits ########
def digit_zero(displacement=0):
  d = displacement
  MidPoint(200 + d, 200, 200 + d, 400)
  MidPoint(100 + d, 400, 200 + d, 400)
  MidPoint(100 + d, 200, 200 + d, 200)
  MidPoint(100 + d, 200, 100 + d, 400)

def digit_one(displacement=0):
  d = displacement
  MidPoint(150 + d, 350, 200 + d, 400)
  MidPoint(200 + d, 200, 200 + d, 400)
  MidPoint(150 + d, 200, 250 + d, 200)

def digit_two(displacement=0):
  d = displacement
  MidPoint(200 + d, 300, 200 + d, 400)
  MidPoint(100 + d, 300, 200 + d, 300)
  MidPoint(100 + d, 400, 200 + d, 400)
  MidPoint(100 + d, 200, 200 + d, 200)
  MidPoint(100 + d, 200, 100 + d, 300)

def digit_three(displacement=0):
  d = displacement
  MidPoint(200 + d, 200, 200 + d, 400)
  MidPoint(100 + d, 300, 200 + d, 300)
  MidPoint(100 + d, 400, 200 + d, 400)
  MidPoint(100 + d, 200, 200 + d, 200)

def digit_four(displacement=0):
  d = displacement
  MidPoint(200+d, 200, 200+d, 400)
  MidPoint(100+d, 300, 200+d, 300)
  MidPoint(100+d, 300, 100+d, 400)


def digit_five(displacement=0):
  d = displacement
  MidPoint(200 + d, 200, 200 + d, 300)
  MidPoint(100 + d, 300, 200 + d, 300)
  MidPoint(100 + d, 400, 200 + d, 400)
  MidPoint(100 + d, 200, 200 + d, 200)
  MidPoint(100 + d, 300, 100 + d, 400)

def digit_six(displacement=0):
  d = displacement
  MidPoint(200 + d, 200, 200 + d, 300)
  MidPoint(100 + d, 300, 200 + d, 300)
  MidPoint(100 + d, 400, 200 + d, 400)
  MidPoint(100 + d, 200, 200 + d, 200)
  MidPoint(100 + d, 200, 100 + d, 400)

def digit_seven(displacement=0):
  d = displacement
  MidPoint(100 + d, 400, 200 + d, 400)
  MidPoint(150 + d, 200, 200 + d, 400)

def digit_eight(displacement=0):
  d = displacement
  MidPoint(200 + d, 200, 200 + d, 400)
  MidPoint(100 + d, 300, 200 + d, 300)
  MidPoint(100 + d, 400, 200 + d, 400)
  MidPoint(100 + d, 200, 200 + d, 200)
  MidPoint(100 + d, 200, 100 + d, 400)

def digit_nine(displacement=0):
  d = displacement
  MidPoint(200 + d, 200, 200 + d, 400)
  MidPoint(100 + d, 300, 200 + d, 300)
  MidPoint(100 + d, 400, 200 + d, 400)
  MidPoint(100 + d, 200, 200 + d, 200)
  MidPoint(100 + d, 300, 100 + d, 400)

def Print_Last_Two_Digit(user_id):
    if user_id[-2] == "0":
        digit_zero()
    elif user_id[-2] == "1":
        digit_one(-20)
    elif user_id[-2] == "2":
        digit_two()
    elif user_id[-2] == "3":
        digit_three()
    elif user_id[-2] == "4":
        digit_four()
    elif user_id[-2] == "5":
        digit_five()
    elif user_id[-2] == "6":
        digit_six()
    elif user_id[-2] == "7":
        digit_seven()
    elif user_id[-2] == "8":
        digit_eight()
    elif user_id[-2] == "9":
        digit_nine()

    if user_id[-1] == "0":
        digit_zero(150)
    elif user_id[-1] == "1":
        digit_one(120)
    elif user_id[-1] == "2":
        digit_two(150)
    elif user_id[-1] == "3":
        digit_three(150)
    elif user_id[-1] == "4":
        digit_four(150)
    elif user_id[-1] == "5":
        digit_five(150)
    elif user_id[-1] == "6":
        digit_six(150)
    elif user_id[-1] == "7":
        digit_seven(150)
    elif user_id[-1] == "8":
        digit_eight(150)
    elif user_id[-1] == "9":
        digit_nine(150)

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

    user_id = "20301137"
    Print_Last_Two_Digit(user_id)

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)

glutMainLoop()