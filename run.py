from MainFrame import *
from CurvatureGraph import *
import input
import thread

try:
    # Inicio do programa e das threads para rodar o grafico e a curva
    input.get()
    thread.start_new_thread(graph, ())
    thread.start_new_thread(main, ())
except KeyboardInterrupt:
    thread.exit()

while 1:
    pass
