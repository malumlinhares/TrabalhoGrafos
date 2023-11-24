from biblioteca import *
a = Digrafo("USA-road-d.NY.gr")
print(a.Gn())
print(a.Gm())
print(a.listaAdj.lista["1"])
d,pi = a.bfs("1")
print(d["2"],pi["2"])
