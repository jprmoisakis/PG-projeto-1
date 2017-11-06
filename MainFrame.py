from func import *
from OpenGL.GLUT import *
import func
import input

pontos = []
#auxiliar
index = 0
window_w, window_h = 640, 480
window_wG, window_hG = 480, 320


def main():
    #setup inicial
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(window_w,window_h)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("window")
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glLineWidth(2.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMouseFunc(mouseClick)
    glutSpecialUpFunc(resetScreen)
    glutKeyboardFunc(exit)
    glutMainLoop()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    global globVector
    globVector = []

    # Desenha os pontos de controle
    if (len(pontos) > 0):
        glPointSize(9.0)
        glBegin(GL_POINTS)
        glColor3f(0.0, 0.0, 0.0)

        for p in pontos:
            glVertex2f(p['x'], p['y'])
        glEnd()
        # Desenha as linhas que liga os pontos de controle
        if (len(pontos) > 1):
            glBegin(GL_LINE_STRIP)
            glColor3f(0.0,1.0,0.0)

            for p in pontos:
                glVertex2f(p['x'], p['y'])
            glEnd()

            # Desenha a Curva
            glBegin(GL_LINE_STRIP)
            glColor3f(0.0,0.0,1.0)
            globVector = func.bezier(pontos, input.getFactor())
            glEnd()

            glPointSize(5.0)
            #
            #  Desenha os pontos de parametro
            glBegin(GL_POINTS)
            glColor3f(0.5,0.0,0.5)
            for p in globVector:
                glVertex2d(p['x'], p['y'])
            glEnd()

        else:
            p = pontos[0]
            glVertex2d(p['x'], p['y'])

    glFlush()

def reshape (width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, window_w, window_h, 0.0, -5.0, 5.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

#Botao de saida
def exit(*args):
    #esc
    if args[0] == '\x1b':
        sys.exit()

#limpa a tela
def resetScreen(key, x ,y):
    if key == GLUT_KEY_F5:
        global pontos
        pontos = []
        func.curvatureK = []
        glutPostRedisplay()

def mouseClick(button, state, x, y):
    global index
    exist = False
    # Verifica se o ponto existe
    for p in range(0,len(pontos)):
        if (x >= pontos[p]['x'] - 4.5) and (x <= pontos[p]['x'] + 4.5):
            if (y >= pontos[p]['y'] - 4.5) and (y <= pontos[p]['y'] +4.5):
                exist = True
                index = p
                break
    
    # Adiciona pontos
    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN and exist == False:
            p = {'x':float(x),'y':float(y)}
            pontos.append(p)
            index = len(pontos)-1
            glutPostRedisplay()

    # remove pontos
    elif button == GLUT_RIGHT_BUTTON:
        if state == GLUT_DOWN and exist == True:
            pontos.pop(0 + index)
            glutPostRedisplay()





