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
    


def escribir_palabras(T,patron,n):
    lista_palabras=[]
    lista_nodos_finales=[]
    nodo=search_children(,)


#recorro el arbol y guardo los ultimos nodos en una lista 'lista_nodos_finales'
def lastnode(node,list):
       if (node.children ==None or node.children < 1) and node.isendOfWOrrd==True: 
        list.append(node)
        for i in range (len(node.children)):
            lastnode(node.children[i],list)



               



       """ buscamos el nodo en el que empieza la palabra
        nodeincio = search_children(T.root.childre,palabra[0])
        if (verificar_ramas(nodeincio) ==True): 
            #casso2
            if (letras_marcadas()==1):

            #casso3    
            else:
        #caso4:
        else:

        
        los desvinculamos: del arreglro T.root.children borramos el nodo del primer caracter de la palabra"""
    

