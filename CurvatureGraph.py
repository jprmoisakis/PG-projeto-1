import matplotlib.pyplot as plt
import func
import numpy
import input


def graph():
    fig = plt.figure(figsize=(10.5, 8))
    ax = fig.add_subplot(111)
    valueX = 1
    a = []
    a.append(0.0)
    while len(a) < int(input.getFactor()):
        a.append(valueX / input.getFactor())
        valueX = valueX + 1
    b = []
    b.append(0.0)

    while len(b) < int(input.getFactor()):
        b.append(0.0)

    x = a
    y = b

    li, = ax.plot(x, y)

    plt.xticks(numpy.arange(0.0, 1.05, 0.05))
    plt.yticks(numpy.arange(-1.0, 1.2, 0.1))

    plt.xlabel('t = %s' % input.getFactor())
    plt.ylabel('Curvatura (k)')
    plt.title('Grafico de Curvatura')
    plt.grid(True)

    # plota o grafico
    fig.canvas.draw()
    plt.show(block=False)

    # Mantem o grafico atualizado
    while True:
        try:
            curvature = []

            if func.curvatureK:
                minimum = min(func.curvatureK)
                maximum = max(abs(i) for i in func.curvatureK)

                for x in func.curvatureK:
                    k = x / maximum
                    curvature.append(k)

            if len(curvature) != 0:
                y = curvature

            else:
                y = b

            li.set_ydata(y)
            fig.canvas.draw()

        except Exception as error:
            raise error
            break
