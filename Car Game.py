import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
import MIDpoint
import Circle

objects = []  # list to store the coordinates and speed of each object
def pixel(a):
    return glPointSize(a)

def colorSet(a,b,c):
    return glColor3f(a/255, b/255, c/255)

def draw_object(position, color, type):
    if type == "box":
        pixel(50)
        x1,y1,x2,y2 = position
        glColor3fv(color)
        MIDpoint.MidPoint(x1, y1, x2, y2)
    else:
        x, y = position
        radius = 20
        total_inside_circle = 100
        glColor3fv(color)
        originX = x
        originY = y
        Circle.All_Circles(radius, total_inside_circle, originX, originY)



def init():
    # set up PyGame and PyOpenGL
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(-1, 1, -1, 1)
    glMatrixMode(GL_MODELVIEW)


    # set the initial coordinates and speed of each object
    for i in range(4):
        type= random.choice(["box", "circle"])
        if type == "box":
            x = random.choice([75,175,-75,-175])  # random x-coordinate between -1 and 1
            y1 = 220  # start at the top of the screen
            y2 = 250
            dy = -10 # random downward speed
            color = (random.random(), random.random(), random.random())  # random color for each object
            objects.append((x, y1, x, y2, dy, color,type))
        else:
            x = random.choice([75,175,-75,-175])
            y = 250
            dy = -10 # random downward speed
            color = (random.random(), random.random(), random.random())  # random color for each object
            objects.append((x, y, dy, color, type))

def road():
    pixel(20)
    colorSet(157, 162, 171)

    MIDpoint.MidPoint(0, 250, 0, -250)

    displacement = 0
    pixel(15)
    colorSet(255, 255, 255)
    for i in range(8):
        MIDpoint.MidPoint(125, 220 - displacement, 125, 250 - displacement)
        MIDpoint.MidPoint(-125, 220 - displacement, -125, 250 - displacement)
        displacement += 200



def main():
    init()
    clock = pygame.time.Clock()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT)


        road()

        # loop through each object and draw the objects
        for i in range(4):
            if objects[i][-1] == "box":
                x1, y1, x2, y2, dy, color, type = objects[i]
                draw_object((x1, y1, x2, y2), color,type)

               # update the position of the object
                y1 += dy
                y2 += dy
                objects[i] = (x1, y1, x2, y2, dy, color, type)

                # if the object has fallen off the bottom of the screen, reset its position and speed
                if y1 < -250:
                    x = random.choice([75,175,-75,-175])
                    dy = -10
                    color = (random.random(), random.random(), random.random())
                    objects[i] = (x, 220, x, 250, dy, color,type)
            else:
                x, y, dy, color, type = objects[i]
                draw_object((x, y), color,type)

                # update the position of the object
                y += dy
                objects[i] = (x, y, dy, color,type)

                # if the object has fallen off the bottom of the screen, reset its position and speed
                if y < -250:
                    x = random.uniform(-250,250)
                    y = 250
                    dy = -10
                    color = (random.random(), random.random(), random.random())
                    objects[i] = (x, y, dy, color,type)

        pygame.display.flip()
        clock.tick(60)



main()