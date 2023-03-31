#Ejercicio 4
"""Implementar un algoritmo que ordene una lista de elementos
 donde siempre el elemento del medio de la lista contiene antes que
 él en la lista la mitad de los elementos menores que él. Explique 
 la estrategia de ordenación utilizada."""
def Order_list(lista):
    # Encuentro el elemento de la mitad
    pivot = lista[len(lista) // 2]
    menores = []
    mayores = []
    # Recorro la lista y lleno las nuevas listas
    for i in range(len(lista)):
        if i == pivot:
            continue
        if lista[i] < lista[pivot]:
            menores.append(lista[i])
        else:
            mayores.append(lista[i])
    # Llamo a la recursividad con las nuevas listas
    menores_new = Order_list(menores)
    mayores_new = Order_list(mayores)
    # + concatena las listas y forma la nueva lista
    return menores_new + [lista[pivot]] + mayores_new


#Ejecicio 5
"""Implementar un algoritmo Contiene-Suma(A,n) que recibe una lista de enteros A y un 
entero n y devuelve True si existen en A un par de elementos que 
sumados den n. Analice el costo computacional."""

def Contiene_Suma(A,n):
    for i in range(len(A)):
        if A[i]< n:
            for j in range(len(A)):
                if j!=i:
                    if A[i]+A[j]==n:
                        return True
    return False
#O(n^2) el tiempo de ejecucion aumenta  a medida que aumenta el tamaño del array