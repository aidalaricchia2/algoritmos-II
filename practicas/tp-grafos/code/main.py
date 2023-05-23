from graph import*
LA=[]
arista1=(1,2)
arista2=(1,3)
arista3=(1,4)
arista4=(2,1)
arista5=(2,3)
arista7=(3,1)
arista8=(3,2)
arista9=(4,1)

LA.append(arista1)
LA.append(arista2)
LA.append(arista3)
LA.append(arista4)
LA.append(arista5)
LA.append(arista7)
LA.append(arista8)
LA.append(arista9)
LV=[1,2,3,4]
grafo=createGraph(LA,LV)

x=tiene_ciclos(grafo)

print(x)