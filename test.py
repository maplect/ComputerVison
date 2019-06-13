from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def drawFunc():
    glClear(GL_COLOR_BUFFER_BIT)
    # glRotatef(1, 0, 1, 0)
    glutWireTeapot(0.5)
    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
glutInitWindowSize(400, 400)
# 参数为b类型而不是string
glutCreateWindow(b"First")
glutDisplayFunc(drawFunc)
# glutIdleFunc(drawFunc)
glutMainLoop()