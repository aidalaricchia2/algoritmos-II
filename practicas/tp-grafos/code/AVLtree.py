#Aida Laricchia legajo:13251
class AVLTree:
    root = None
class AVLNode:
    parent = None
    leftnode = None
    rightnode = None
    key = None
    value = None
    bf = None

#Copiar y adaptar todas las operaciones del binarytree.py
'rotateLeft(Tree,avlnode)'
'Descripción: Implementa la operación rotación a la izquierda'
'Entrada: Un Tree junto a un AVLnode sobre el cual se va a operar la'
'rotación a la izquierda'
'Salida: retorna la nueva raíz'

def rotateRight(tree,rotenode):
    new_root=rotenode.leftnode
    rotenode.leftnode=new_root.rightnode
    if new_root.rightnode != None:
        new_root.rightnode.parent=rotenode
    new_root.parent=rotenode.parent
    if rotenode.parent == None:
        tree.root=new_root
    else:
        if rotenode.parent.rightnode == rotenode:
            rotenode.parent.rightnode=new_root
        else:
            rotenode.parent.left=new_root
    new_root.rightnode=rotenode
    rotenode.parent=new_root.rightnode

def rotateLeft(tree,rotenode):
    new_root=rotenode.rightnode
    rotenode.rightnode=new_root.leftnode
    if new_root.leftnode != None:
        new_root.leftnode.parent=rotenode
    new_root.parent=rotenode.parent
    if rotenode.parent == None:
        tree.root=new_root
    else:
        if rotenode.parent.leftnode == rotenode:
            rotenode.parent.leftnode=new_root
        else:
            rotenode.parent.left=new_root
    new_root.leftnode=rotenode
    rotenode.parent=new_root.leftnode   

#funcion que al pasarle un nodo me dice su altura eesta sera necesaria para la f.calculateblance
#esta sera una funcion recursiva 
def altura(node):
    if node ==None:
        return 0
    return (1+max(altura(node.left),altura(node.right)))

#Esta funcion calcula el bf de un solo nodo
def calculate_balance(B):
    node=B.root
    if node != None:
        calculate_balance_node(node)

#En esta funcion se recorre todo el arbol mientras se va calculado el bf de cada nodo
def calculate_balance_node(node):
    if node != None:
        node.bf= altura(node.left)-altura(node.right)
        calculate_balance_node(node.leftnode)
        calculate_balance_node(node.rightnode)

#funcion que busca el nodo desbalanceado
def find_node_desbalance(AVLT):
    calculate_balance(AVLT)
    node=AVLT.root
    if node != None:
        return (find_node_desbalanceR(node))

#retorna el nodo que tiene el desbalance
def find_node_desbalanceR(node):
    if node != None:
        if node.bf != 1 and node.bf !=0 and node.bf !=-1:
            return node
        find_node_desbalanceR(node.leftnode)
        find_node_desbalanceR(node.rightnode)   


def reBalance(AVLTree):
    bf_arbol=calculate_balance_node(AVLTree.root)
    if bf_arbol != 1 and bf_arbol !=0 and bf_arbol !=-1:
        node = find_node_desbalance(AVLTree)
        #Rebalanceamos el arbol
        rebalanceR(AVLTree, node)

#esta funcion recibe el nodo que esta desbalanceado
def rebalanceR(AVLTree, node):
    if node.bf < -1:
        if node.rightnode.bf == 1:
            rotateRight(AVLTree,node.rightnode)
            rotateLeft(AVLTree, node)
        else:
            rotateLeft(AVLTree, node)
    if node.bf > 1:
        if node.leftnode.bf == -1:
            rotateLeft(AVLTree, node.leftnode)
            rotateRight(AVLTree, node)
        else:
            rotateRight(AVLTree, node)

#insert binarytree modificado para AVLT
def insertw(B,newnode, currentnode):
    if newnode.key>currentnode.key:
        if currentnode.rightnode==None:
            newnode.parent=currentnode
            currentnode.rightnode=newnode
            #cuando ya insertamos tenemos que chequear que el arbol siga siendo AVL
            #tendremos que cheaquer en esa rama el bf de cada uno de sus padre si uno 
            #no se encuentra en el intervalo entonces balanceamos
            node_desbalance=check_balance_parent(newnode)
            if node_desbalance != None:
                #balancear
                rebalanceR(B, node_desbalance)
            return newnode.key
        else:
            return insertw(newnode, currentnode.rightnode)
        
    elif newnode.key<currentnode.key:
        if currentnode.leftnode==None:
            newnode.parent=currentnode
            currentnode.leftnode=newnode
            #chequeamos solo subieron en el arbol
            node_desbalance=check_balance_parent(newnode)
            if node_desbalance != None:
                #balancear
                rebalanceR(B, node_desbalance)

            return newnode.key
        else:
            return insertw(newnode, currentnode.leftnode)
    else:
        return None


def check_balance_parent(node):
    while node != None:
        calculate_balance_node(node)
        if node.bf >1 or node.bf <-1:
            return node
        node=node.parent
    return None

#mismo inser de binarytree pero ahora pasamos el arbol como parametro
def insert(B,element,key):
    newnode=AVLNode()
    newnode.value=element
    newnode.key=key
    currentnode=B.root
    if B.root==None:
        B.root=newnode
    else:
        return insertw(B,newnode, currentnode)

#Funcion delete
def deletew(B,deletingnode):
    if deletingnode!=None:
        #Caso 1: Hoja
        if deletingnode.leftnode==None and deletingnode.rightnode==None:
            if deletingnode==B.root:
                B.root=None
                return deletingnode.key
            else:
                padre=deletingnode.parent
                #Me fijo si el nodo a eliminar es el hijo derecho o izquierdo de su padre
                if padre.rightnode==deletingnode:

                    padre.rightnode=None
                #balancear
                    node_desbalance=check_balance_parent(padre)
                    if node_desbalance != None:
                        #balancear
                        rebalanceR(B, node_desbalance)
                    return deletingnode.key
                else:
                    padre.leftnode=None
                    #balancear
                    node_desbalance=check_balance_parent(padre)
                    if node_desbalance != None:
                        #balancear
                        rebalanceR(B, node_desbalance)
                    return deletingnode.key
                
        #Caso 2: Un solo hijo
        #Si es el hijo izquierdo
        elif deletingnode.rightnode==None:
            if deletingnode==B.root:
                B.root=deletingnode.leftnode
                return deletingnode.key
            else:
                padre=deletingnode.parent
                #Me fijo si el nodo a eliminar es el hijo derecho o izquierdo de su padre
                if padre.rightnode==deletingnode:
                    padre.rightnode=deletingnode.leftnode
                    node_desbalance=check_balance_parent(padre)
                    if node_desbalance != None:
                        #balancear
                        rebalanceR(B, node_desbalance)
                    return deletingnode.key
                else:
                    padre.leftnode=deletingnode.leftnode
                    node_desbalance=check_balance_parent(padre)
                    if node_desbalance != None:
                        #balancear
                        rebalanceR(B, node_desbalance)
                    return deletingnode.key
        #Si es el hijo derecho            
        elif deletingnode.leftnode==None:
            if deletingnode==B.root:
                B.root=deletingnode.rightnode
                return deletingnode.key
            else:
                padre=deletingnode.parent
                #Me fijo si el nodo a eliminar es el hijo derecho o izquierdo de su padre
                if padre.rightnode==deletingnode:
                    padre.rightnode=deletingnode.rightnode
                    node_desbalance=check_balance_parent(padre)
                    if node_desbalance != None:
                        #balancear
                        rebalanceR(B, node_desbalance)
                    return deletingnode.key
                else:
                    padre.leftnode=deletingnode.rightnode
                    node_desbalance=check_balance_parent(padre)
                    if node_desbalance != None:
                        #balancear
                        rebalanceR(B, node_desbalance)
                    return deletingnode.key
                           
        #Caso 3: Dos hijos
        else:
            aux1=deletingnode.rightnode
            aux2=deletingnode.leftnode
            #Buscamos al mayor de menores
            mayor=mayordemenores(deletingnode)
            #En el caso de que el mayor de menores tenga hijos izquierdos y no sea el hijo izquierdo del nodo a eliminar:
            if mayor.leftnode!=None and mayor!=aux2:
                menor=menorhijoizq(mayor)
                #Para evitar crear un ciclo con padres=hijos
                if menor.parent!=deletingnode.leftnode:
                    menor.leftnode=aux2
            elif mayor.leftnode==None and mayor!=aux2:
                mayor.leftnode=aux2
            mayor.rightnode=aux1        

            if deletingnode==B.root:
                B.root=mayor
            else:
                padre=deletingnode.parent
                mayor.parent=padre 
                if padre.rightnode==deletingnode:
                    padre.rightnode=mayor
                    node_desbalance=check_balance_parent(padre)
                    if node_desbalance != None:
                        #balancear
                        rebalanceR(B, node_desbalance)
                else:
                    padre.leftnode=mayor
                    node_desbalance=check_balance_parent(padre)
                    if node_desbalance != None:
                        #balancear
                        rebalanceR(B, node_desbalance)

            return deletingnode.key
    else:
        return None

#Funcion que encuentra el nodo mayor entre los hijos menores de un nodo
def mayordemenores(node):
    currentnode=node.leftnode
    while currentnode.rightnode!=None:
        currentnode=currentnode.rightnode
    currentnode.parent.rightnode=None
    return currentnode

#Funcion que encuentra el ultimo hijo menor dentro de una rama
def menorhijoizq(node):
    if node.leftnode==None:
        return node
    else:
        return menorhijoizq(node.leftnode)
    

def delete(B,element):
    currentnode=B.root
    deletingnode=searchR(currentnode, element)
    return deletew(B,deletingnode)

def searchR(currentnode,element):
    if currentnode!=None:
        if element==currentnode.value:
            return currentnode        
        else:
            izq= searchR(currentnode.leftnode,element)
            der= searchR(currentnode.rightnode,element)
            if izq==None and der==None:
                return None
            elif izq==None:
                return der
            elif der==None:
                return izq
    else:
        return None
   
def search(AVL,element):
    currentnode=AVL.root
    result=searchR(currentnode, element)
    if result!=None:
        return result.key
    else:
        return None