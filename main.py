from biblioteca import *
import sys
sys.setrecursionlimit(100000)
a = Grafo("USA-road-d.NY.gr")
print(a.Gn())
print(a.Gm())
print(a.listaAdj.lista["1"])
#d,pi = a.bf("1")
#print(d, pi)
