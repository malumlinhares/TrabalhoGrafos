from biblioteca import *
import sys
sys.setrecursionlimit(100000)
a = Digrafo("USA-road-d.NY.gr")
print(a.Gn())
print(a.Gm())
print(a.listaAdj.lista["1"])
#pi, tempi, tempf = a.inicia_dfs("1")
#print(pi)
d,pi = a.djikstra("1")
print(d, pi)
#d,pi = a.bf("1")
#print(d, pi)
