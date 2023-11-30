from biblioteca import *
import sys
sys.setrecursionlimit(100000)
a = Digrafo("USA-road-d.NY.gr")
print(a.Gn()) #qnt vertices
print(a.Gm()) #qnt arestas
enter = input("pressione enter para o item a")
print(a.Gmind()[1]) #item a, coloco pos [1] pois retorno uma lista com o vertice com menor grau tambem
enter1 = input("pressione enter para o item b")
print(a.Gmaxd()[1]) #item b, coloco pos [1] pois retorno uma lista com o vertice com maior grau
enter2 = input("pressione enter para o item c")
print(a.achaCaminho("4597","125"))
enter3 = input("pressione enter para o item d")
print(a.detectaCiclos("1", 5))
enter4 = input("pressione enter para o item e")
d, pi = a.djikstra("129")
maiord= 0
vertice = ""
for key in d.keys():
    if int(d[key]) > maiord:
        maiord = int(d[key])
        vertice = key
print("Maior distancia: " + maiord)
print("Vertice mais distante: " + vertice)

