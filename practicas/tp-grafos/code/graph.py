from Trie import*
#Graph = ([]*n,[])
#Graph = Array(n,LinkedList())
#lista de vertices y lista de aristas
#recorrer toda la lista de vertices y en ese recorrido que devuelda
#  una lista con todas nodos que tienen como primer componente el vertice con el que estamos 
class Tree:
	root = None

class TreeNode:
    parent = None
    children = []




def createGraph(LA,LV):
    l_ady=[]
    for vertices in LV:
        lis=[]
        lis.append(vertices)
        l_ady.append(lis)

    for vertice in l_ady:
    #vamos recorriendo los vertices
        for aristas in LA:
            vertice[0]
            if vertice[0]==aristas[0]:
                vertice.append(aristas[1])
    return(l_ady)


#EJERCICIO 2
#operación existe camino que busca si existe un camino entre los vértices v1 y v2
def existPath(Grafo, v1, v2): 
    list= DFS(Grafo)
    if (v1 in list) and ( v2 in list):
        return True
    else:
        return False

#RECORRIDO DFS (PROFUNDIDAD)
def DFS(grafo):
    cicle = True
    vertice= grafo[0][0]
    visitados = []
    return(dfsR(grafo,visitados,vertice))

def dfsR(grafo, visitados,vertice):
    for i in range (len(grafo)):
        #chequeamos que los vertices tengan vertices adyacentes
        if len(grafo[i]) != 1:
            for j in range (len(grafo[i])):
                if grafo[i][j] not in visitados:
                    
                    vertice=grafo[i][j]
                    visitados.append(vertice)
                    dfsR(grafo, visitados, vertice)
    # Retornar la lista de vértices visitados
    return visitados

#EJERCICIO 3
#Implementa la operación es conexo
def isConnected(Grafo):
    list= DFS(Grafo)
    if len(list[0]) == len(Grafo):
        return True
    else:
        return False
    
def tiene_ciclos(grafo):
    visitados=[]
    for i in range (len(grafo[0])):
        nodo=grafo[0][i]
        if nodo not in visitados:
            if tiene_ciclos_util(grafo,nodo,visitados,None):
                return True
    return False
"""
def tiene_ciclos_util(grafo, nodo, visitados, padre):
    # Marcar el nodo actual como visitado
    visitados.append(nodo)
    # Recorrer los nodos adyacentes al nodo actual
    for vecino in grafo[nodo]:
        # Si el vecino no ha sido visitado, llamar recursivamente a la función
        if vecino not in visitados:
            if tiene_ciclos_util(grafo, vecino, visitados, nodo):
                return True
        # Si el vecino ya ha sido visitado y no es el padre del nodo actual, hay un ciclo
        elif vecino != padre:
            return True
    return False
"""

"""Ejercicio 6"""
def convertTree(Grafo):
    #dado un grafo devuelva una lista de aristas que si se eliminan el grafo se convierte en un árbol
    Aux=[]#cuento las aristas
    for each in Grafo:
        for i in range(0,len(each)):
            if i != 0:
                if (each[0],each[i]) not in Aux and (each[i],each[0]) not in Aux:
                    Aux.append((each[0],each[i]))
    visted=[]
    elimA=[]
    cont=0 #si ambas estan entonces esa arista tiene que eliminarse
    while cont<len(Aux):
        flag=True
        if Aux[cont][0] not in visted or Aux[cont][1] not in visted:
            if Aux[cont][0] not in visted: visted.append(Aux[cont][0])
            if Aux[cont][1] not in visted: visted.append(Aux[cont][1])
            cont=cont+1
        else:
            elimA.append(Aux[cont])
            Aux.remove(Aux[cont])
    print (Aux)
    return elimA

def search_list_value(l,value):
    for i in range(0,len(l)):
        if value==l[i]:
            return value
    return None 
def find_vertice(V,G):
    #nos devuelve en q fila esta el vertice
    for i in range(0,len(G)):
        if G[i][0]==V:
            return i
        
def BFS (grafo,V):
    queue=[]
    #agregamos vetice
    queue.append(V)
    #lista de pendientes por visitar
    grayList=[]
    grayList.append(V)
    #lista de vistados
    blackList=[]
    
    while len(queue)>0:
        #busco posicion de vertice en la lista de adyacencia 
        posc=find_vertice(queue[0],grafo)
        aux=queue.pop(0)
        #Se ubica en la fila del vertice
        L=grafo[posc]
        #si no estan sus elementos en la lista de pendientes los agrega 
        for current in L:
            if search_list_value(grayList,current)==None:
                grayList.append(current)
                queue.append(current)
        blackList.append(aux)
    return blackList