
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

#insert binarytree modificaso para AVLT

def insertw(B,newnode, currentnode):
    if newnode.key>currentnode.key:
        if currentnode.rightnode==None:
            newnode.parent=currentnode
            currentnode.rightnode=newnode
            #cuando ya insertamos tenemos que chequear que el arbol siga siendo AVL
            #tendremos que cheaquer en esa rama el bf de cada uno de sus padre si uno 
            #no se encuentra en el intervalo entonces balanceamos
            if check_balance_parent(newnode) != None:
                #balancear
                reBalance(B)
            return newnode.key
        else:
            return insertw(newnode, currentnode.rightnode)
        
    elif newnode.key<currentnode.key:
        if currentnode.leftnode==None:
            newnode.parent=currentnode
            currentnode.leftnode=newnode
            #chequeamos solo subieron en el arbol
            if check_balance_parent(newnode) != None:
                #balancear
                reBalance(B)

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
