from OpenGL.GL import *
import math

globVector = []
firstDerivate = []
secondDerivate = []

deltaUm = []
deltaDois = []
curvatureK = []

# Faz o calculo geral
def bezier(pontos, factor):
    global globVector
    global firstDerivate
    global secondDerivate

    global deltaUm
    global deltaDois
    global curvatureK

    globVector = []
    firstDerivate = []

    t = 0
    plus_factor = 1.0 / factor

    while t <= 1:
        bezier_Castel(pontos, t)
        t += plus_factor

    # Calculo o delta um e a primeira derivada
    if len(pontos) > 1:
        getdeltaUm(pontos)
        firstDerivate = []
        u = 0
        while u <= 1:
            first_derivate_castel(pontos, deltaUm, u)
            u += plus_factor


    # Calcula o delta dois e a segunda derivada
    if len(pontos) > 2:
        getdeltaDois(pontos)
        secondDerivate = []
        u = 0
        while u <= 1:
            second_derivate_castel(pontos, deltaDois, u)
            u += plus_factor


    # Calculo de curvatura
    if len(pontos) > 2:
        curvatureK = []
        curvature(firstDerivate, secondDerivate)

    return globVector

# Calculo da primeira derivada de bezier
def first_derivate_castel(pontos, deltaUm, t):
    global firstDerivate
    if len(deltaUm) == 1:
        firstDerivate.append(deltaUm[0])
    else:
        updated_points = []
        for i in range(0, len(deltaUm) - 1):
            p = {'x': 0.0, 'y': 0.0}
            p['x'] = t * deltaUm[i + 1]['x'] + (1 - t) * deltaUm[i]['x']
            p['y'] = t * deltaUm[i + 1]['y'] + (1 - t) * deltaUm[i]['y']

            updated_points.append(p)
        first_derivate_castel(pontos, updated_points, t)

# Calculo da segunda derivada de bezier
def second_derivate_castel(pontos, deltaDois, t):
    global secondDerivate
    if len(deltaDois) == 1:
        secondDerivate.append(deltaDois[0])
    else:
        updated_points = []

        for i in range(0, len(deltaDois) - 1):
            p = {'x': 0.0, 'y': 0.0}
            p['x'] = t * deltaDois[i + 1]['x'] + (1 - t) * deltaDois[i]['x']
            p['y'] = t * deltaDois[i + 1]['y'] + (1 - t) * deltaDois[i]['y']

            updated_points.append(p)
        second_derivate_castel(pontos, updated_points, t)


# Calculo da curva de bezier com algoritmo de de casteljau
def bezier_Castel(pontos, t):
    global globVector
    if len(pontos) == 1:
        globVector.append(pontos[0])
        glVertex2f(pontos[0]['x'], pontos[0]['y'])
    else:
        updated_points = []

        for i in range(0, len(pontos) - 1):
            p = {'x': 0, 'y': 0}
            p['x'] = t * pontos[i + 1]['x'] + (1 - t) * pontos[i]['x']
            p['y'] = t * pontos[i + 1]['y'] + (1 - t) * pontos[i]['y']

            updated_points.append(p)
        bezier_Castel(updated_points, t)


# Calcula o Delta um para usar na primeira derivada
def getdeltaUm(pontos):
    global deltaUm
    deltaUm = []
    for i in range(0, len(pontos) - 1):
        p = {'x': 0.0, 'y': 0.0}
        deltaX = pontos[i + 1]['x'] - pontos[i]['x']
        deltaY = pontos[i + 1]['y'] - pontos[i]['y']
        p['x'] = deltaX * (len(pontos) - 1)
        p['y'] = deltaY * (len(pontos) - 1)
        deltaUm.append(p)

# Calcula o delta dois para a segunda derivada
def getdeltaDois(pontos):
    global deltaDois
    deltaDois = []

    for i in range(0, len(pontos) - 2):
        p = {'x': 0.0, 'y': 0.0}
        deltaX = pontos[i + 2]['x'] - 2 * pontos[i + 1]['x'] + pontos[i]['x']
        deltaY = pontos[i + 2]['y'] - 2 * pontos[i + 1]['y'] + pontos[i]['y']
        p['x'] = deltaX * ((len(pontos) - 1) * (len(pontos) - 2))
        p['y'] = deltaY * ((len(pontos) - 1) * (len(pontos) - 2))

        deltaDois.append(p)

# calculo da curvatura
def curvature(firstDerivate, secondDerivate):
    global curvatureK
    for p in range(0, len(firstDerivate)):
        numK = (firstDerivate[p]['x'] * secondDerivate[p]['y']) - firstDerivate[p]['y'] * secondDerivate[p]['x']
        demK = math.pow(math.pow(firstDerivate[p]['x'], 2) + math.pow(firstDerivate[p]['y'], 2), 1.5)
        K = numK / demK
        curvatureK.append(K)
