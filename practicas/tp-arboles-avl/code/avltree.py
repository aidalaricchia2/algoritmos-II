
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
        if 
