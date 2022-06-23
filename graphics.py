import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

def points():
    glBegin(GL_POINTS)
    glVertex2fv((0, 0))
    glVertex2fv((0, 1))
    glVertex2fv((1, 0))
    glVertex2fv((1, 1))
    glEnd()

def square():
    glBegin(GL_QUADS)
    glVertex2fv((0, 0))
    glVertex2fv((0, 1))
    glVertex2fv((1, 0))
    glVertex2fv((1, 1))
    glEnd()

pg.init()
display = (1000, 800)
pg.display.set_mode(display, DOUBLEBUF | RESIZABLE | OPENGL)

gluPerspective(60, (display[0]/display[1]), 0.1, 100.0)
glTranslatef(0.0, 0.0, -5)
glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

while True:
    # this makes the red x button work
    for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
    
    glColor3fv((1, 0, 0))
    square()
    glColor3fv((0, 1, 0))
    points()

    pg.display.flip()
    pg.time.wait(1)