from biblioteca import *
import sys
sys.setrecursionlimit(550000)
a = Digrafo("USA-road-d.NY.gr")
print(a.Gn())
print(a.Gm())
print(a.listaAdj.lista["1"])
pi,tempi,tempf = a.inicia_dfs()
print(pi,tempi,tempf)
