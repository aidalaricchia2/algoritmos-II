from itertools import cycle
class Trie:
	root = None


class TrieNode:
    parent = None
    children = None
    key = None
    isEndOfWord = False


"""insert(T,element)
Descripción: insert un elemento en T, siendo T un Trie.
Entrada: El Trie sobre la cual se quiere agregar el elemento (Trie)
 y el valor del elemento (palabra) a  agregar.
Salida:  No hay salida definida"""


def search_children(array, caracter):
    for i in range(len(array)):
        if array[i] != None:
            if array[i].key == caracter:
                return array[i]
    return None


def insert(T, elemento):
    if T.root == None:
        T.root = TrieNode()
        T.root.children = []
    current = T.root
    for i in range(len(elemento)):
        new_node = search_children(current.children, elemento[i])
        if new_node != None:
            current = new_node
        else:
            nodo = TrieNode()
            nodo.key = elemento[i]
            nodo.children = []
            current.children.append(nodo)
            nodo.parent = current
            current = nodo
    current.isEndOfWord = True


def search(T, palabra):
    current = T.root
    for letra in palabra:
        new_node = search_children(current.children, letra)
        if new_node != None:
            current = new_node
        else:
            return False
    if current.isEndOfWord == True:
        return True


"""def cant_EndOfWord(array):
    for i in range (len(array)):
        if array[i]!=None:
            if array[i].key == caracter:
                return array[i]
    return None"""
"""esta funcion verifica no existan elementos compartidos en ningun nodo del elemento que estamos analizando"""
"""def verificar_ramas(node):
    flag=0
    while node.children !=None:
        if len(node.children)>1:
            flag=1
        node=node.children
    if flag==0: return True
    else: return False

#def letras_marcadas():"""


def search_ultimonodo(T, palabra):
    current = T.root
    """falta si el len de la palabra el 1 devolver ese"""
    for i in range(len(palabra)-1):
        if i == (len(palabra)-1) and new_node.isEndOfWord == True:
            return new_node
        else:
            new_node = search_children(current.children, palabra[i])


""" for letra in palabra:
        new_node=search_children(current.children,letra)
        if new_node == None:
            return 
        current=new_node

    if current.isEndOfWord == True:
        return True    """

def delete(T,palabra):
    #caso1 El elemento no se encuentra en el trie
    encontrado=search (T,palabra)
    if encontrado == False:
        return False
    
    else:
        #buscar el nodo fin de la palabra
        nodo_final=search_ultimonodo(T,palabra)
        nodo_final.isEndOfWord=False  
        flag = True
        while flag:
           if nodo_final.children != None or len(nodo_final.children)>0  or nodo_final.parent != T.root or nodo_final.isEndOfWord==True:
               flag = False
           else:
               nodo_final=nodo_final.parent
        nodo_final.parent.remove(nodo_final)
        return True


"""
def palabras(nodo,palabra_actual,n):

    if nodo.isEndOfWord== True and (len(palabra_actual)==n):
        print_list(palabra_actual)
    elif (len(palabra_actual)<n):
        for letra in nodo.children:
            palabra_generada=palabra_actual+letra
            palabras(letra,palabra_generada,n)
    
"""

"""
def escribir_palabras(T,patron,n):
    lista_palabras=[]
    lista_nodos_finales=[]
    nodo=search_children(,)


#recorro el arbol y guardo los ultimos nodos en una lista 'lista_nodos_finales'
def lastnode(node,list):
       if (node.children ==None or node.children < 1) and node.isendOfWOrrd==True: 
        list.append(node)
        for i in range (len(node.children)):
            lastnode(node.children[i],list)"""
#punto4    
def prefijo(T,p):
    pre=[]
    children=cycle(T.root.children)
    current=next(children)
    for i in range (len(p)):
        while current.key != p[i]:
            children=cycle(current.children)
            current=next(children)
        if current.key == p[i]:
            pre.append(current)
                
    if len(pre) !=0:
        return pre[len(pre)-1]#devuelve el ultimo nodo
    else:
        return None

def patron(T,p,n):
    palabras=[]
    nodo=prefijo(T,p)
    traverse_level(nodo,p,palabras,n)
    return palabras

def traverse_level(nodo,prefijo,palabras,n):
    if nodo.isEndOfWord==True and len(prefijo)==n:
        palabras.append(prefijo)
    for i in range (len(nodo.children)):
        traverse_level(nodo.children[i],prefijo+ nodo.children[i].key,palabras,n)

#Recorre Argo y nos guarda la palabras PUNTO 5
def traverse(nodo,prefijo,palabras):
    if nodo.isEndOfWord==True:
        palabras.append(prefijo)
    for i in range (len(nodo.children)):
        traverse(nodo.children[i],prefijo+ nodo.children[i].key,palabras)
               
def get_words(T):
    words = []
    traverse(T.root, '', words)
    return words

def is_sublist(lst1, lst2):
    return set(lst1).issubset(set(lst2))

#punto 6
"""Implemente un algoritmo que dado el Trie T devuelva True si existen en el documento 
T dos cadenas invertidas. Dos cadenas son invertidas si se leen de izquierda a derecha y 
contiene los mismos caracteres que si se lee de derecha a izquierda, ej: abcd y dcba son
 cadenas invertidas, gfdsa y asdfg son cadenas invertidas, sin embargo abcd y dcka no son
   invertidas ya que difieren en un carácter."""
def palabras_invertidas(T):
    words= get_words(T)
    return has_inverted_list(words)

""" [::-1] se utiliza para obtener la list invertida"""
def has_inverted_list(lst):
    for sublst in lst:
        if sublst[::-1] in lst:
            return True
    return False

#punto 7
