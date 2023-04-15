import pygame
from pygame.locals import *
import MIDpoint
import Circle
from OpenGL.GL import *
from OpenGL.GLU import *
import sys

width, height = 500, 500
WHITE = (1.0, 1.0, 1.0)
VEL = 0.1
def pixel(a):
    return glPointSize(a)

def colorSet(a,b,c):
    return glColor3f(a/255, b/255, c/255)
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
    global width, height, obj_vertices, obj_vbo, vel_x, vel_y
    pygame.init()
    pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    obj_vertices = [-25, -25, -25, 25, 25, 25, 25, -25]
    obj_vbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, obj_vbo)
    glBufferData(GL_ARRAY_BUFFER, 8 * 4, (GLfloat * 8)(*obj_vertices), GL_STATIC_DRAW)

    vel_x = 0
    vel_y = 0


    while True:
        display()


def display():
    global obj_vertices, obj_vbo, vel_x, vel_y, width, height
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    vel_x = (keys[pygame.K_d] - keys[pygame.K_a]) * VEL
    vel_y = (keys[pygame.K_w] - keys[pygame.K_s]) * VEL

    road()
    for i in range(0, len(obj_vertices), 2):
        if vel_x != 1 and vel_y != 1 and vel_x != -1 and vel_y != -1:
            obj_vertices[i] += vel_x
            obj_vertices[i + 1] += vel_y
        else:
            pass

    glBindBuffer(GL_ARRAY_BUFFER, obj_vbo)
    glBufferData(GL_ARRAY_BUFFER, 8 * 4, (GLfloat * 8)(*obj_vertices), GL_STATIC_DRAW)
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, width, 0, height, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glEnableClientState(GL_VERTEX_ARRAY)
    glBindBuffer(GL_ARRAY_BUFFER, obj_vbo)
    glVertexPointer(2, GL_FLOAT, 0, None)
    glColor3f(*WHITE)
    glDrawArrays(GL_QUADS, 0, 4)
    glDisableClientState(GL_VERTEX_ARRAY)


    pygame.display.flip()


main()