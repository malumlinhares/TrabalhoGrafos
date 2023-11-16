class Digrafo:
    def __init__(self, caminho): #dou o caminho de onde estara o grafo
        self.tipo = "digrafo"
        self.listaAdj = ListaAdj(self.tipo)
        self.qnt_arestas = 0
        with open(caminho, 'r') as arquivo:  # adicionando os vertices e arestas a lista
            for linha in arquivo:
                splitted_linha = linha.split(" ")
                if splitted_linha[0] == "a":
                    self.qnt_arestas += 1
                    if splitted_linha[1] not in self.listaAdj.lista:
                        self.listaAdj.addVertice(splitted_linha[1])
                    if splitted_linha[2] not in self.listaAdj.lista:
                        self.listaAdj.addVertice(splitted_linha[2])
                    self.listaAdj.addAresta(splitted_linha[1], splitted_linha[2], splitted_linha[3])
    def Gn(self):# retorna o numero de vertices do digrafo
        qnt_vertices = 0
        for i in self.listaAdj.lista:
            qnt_vertices+=1
        return qnt_vertices
    def Gm(self):# retorna o numero de arestas do grafo
        return self.qnt_arestas
    def Gvizpos(self, vertice): #o parametro e passado como string, retorna a vizinhanca positiva
        vizinhos = []
        for vizinho in self.listaAdj.lista[vertice]:
            vizinhos.append(vizinho[0])
        return vizinhos
    def Gvizneg(self,vertice):#a logica esta em verificar a pos[0] da listaAdj (vertice de destino) e pegar a chave do dicionario(vertice de origem)
        vizinhos = []
        for i in self.listaAdj.lista.keys():
            for j in self.listaAdj.lista[i]:
                if (j[0] == vertice):
                    vizinhos.append(i)
        return vizinhos
    def Gdpos(self, vertice): #retorna o grau de um vertice para sua vizinhanca positiva
        if vertice in self.listaAdj.lista:
            return len(self.listaAdj.lista[vertice])
    def Gdneg(self, vertice): #retorna o grau de um vertice para sua vizinhanca negativa
        vizinhosNegativos = self.Gvizneg(vertice)
        return len(vizinhosNegativos)
class ListaAdj: #resolvemos criar uma classe de lista adj para evitar repeticao de codigo, tambem escolhemos a lista por menor complexidade
    def __init__(self, tipo):
        self.lista = {} #dicionario, a chave seria o vertice, a key seria uma lista [[vertice de chegada, peso da aresta], ...]
        self.tipo = tipo #diz o tipo do grafo, digito "grafo" para grafo e "digrafo" para digrafo.
    def addVertice(self, vertice): #adicionando um vertice a lista adjacente.
        self.lista[vertice] = []
    def addAresta(self, origem, destino, peso): #adicionando uma aresta
        aresta = [destino, peso]
        arestaVolta=[origem, peso]
        self.lista[origem].append(aresta)
        if self.tipo == "grafo": #se nao for digrafo, tambem deve-se adicionar o vizinho no vertice de destino
            self.lista[destino].append(arestaVolta)
class Grafo:
    def __init__(self, caminho): #dou o caminho de onde estara o grafo
        self.tipo = "grafo"
        self.listaAdj = ListaAdj(self.tipo)
        self.qnt_arestas = 0
        with open(caminho, 'r') as arquivo: #adicionando os vertices e arestas a lista, e contabiliza a qnt de arestas
            for linha in arquivo:
                splitted_linha = linha.split(" ")
                if splitted_linha[0] == "a":
                    self.qnt_arestas += 1
                    if splitted_linha[1] not in self.listaAdj.lista:
                        self.listaAdj.addVertice(splitted_linha[1])
                    if splitted_linha[2] not in self.listaAdj.lista:
                        self.listaAdj.addVertice(splitted_linha[2])
                    self.listaAdj.addAresta(splitted_linha[1], splitted_linha[2], splitted_linha[3])
    def Gn(self):# retorna o numero de vertices do grafo
        qnt_vertices = 0
        for i in self.listaAdj.lista:
            qnt_vertices+=1
        return qnt_vertices
    def Gm(self):# retorna o numero de arestas do grafo
        return self.qnt_arestas
    def Gviz(self, vertice): #o parametro e passado como string, retorna a vizinhanca do vertice
        vizinhos = []
        for vizinho in self.listaAdj.lista[vertice]:
            vizinhos.append(vizinho[0])
        return vizinhos
    def Gd(self, vertice): #retorna o grau de um vertice
        if vertice in self.listaAdj.lista:
            return len(self.listaAdj.lista[vertice])