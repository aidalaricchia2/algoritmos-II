def hash_mode(k,m):
    return (k%m)

def CreateHashTable(Dim):
    Hash=[]
    #crea un Hash de M posciones
    for i in range (0,Dim):
        L=[]
        Hash.append(L)
    return Hash

def Insert(D,key,value):
    if len(D)==0 or D==None:
        print("crear tabla hash")
        return None
    else:
        index=hash_mode(key,len(D))
        if D[index]==None:
            list=[]
            tupla=(key,value)
            list.append(tupla)
            D[index]=list
        else:
            tupla=(key,value)
            D[index].append(tupla)

def search(D,key):
    index=hash_mode(key,len(D))
    for elemento in D[index]:
        if elemento[0]==key:
            return (elemento[1])

def delete (D,key):
    if search(D,key)!=None:
        index=hash_mode(key,len(D))
        for i in range (len(D[index])):
            if D[index][i][0]==key:
                D[index].pop(i)
                return D


def string_permutation(s,p):
    if len(s)!=len(p):
        return False
    else:
        dicS=[None]*(ord("z")-ord("a"))
        dicP=[None]*(ord("z")-ord("a"))
        for i in range(len(s)):
            dicS.Insert(hash_mode(ord(s[i])-ord("a"),len(dicS)),s[i])
        for i in range(len(p)):
            dicP.Insert(hash_mode(ord(p[i])-ord("a"),len(dicP)),p[i])
        for i in range(len(dicS)):
            if dicS[i] !=None:
                if len(dicS[i])!=len(dicP[i]):
                    return False
        return True
    
def list_repetidos(L):
    D=[None]*len(L)
    for i in range (len(L)):
        if search(D,L[i]) !=None:
            return False
        Insert(D,L[i],L[i])
    return True

#dudas con si m es len(code)
def hash_code(code):
    for i in range(len(code)):
        if code[i].isdigit():
            num=num+code[i]
        else:
            num=num+ord(code[i])
    return(hash_mode(num,len(code)))

def compre_char(cadena):
    letra=cadena[0]
    cadena_nueva=''
    cont=1
    for i in range (len(cadena)):
        if i !=0:
            if letra==cadena[i]:
                cont=cont+1
            else:
                cadena_nueva=cadena_nueva+letra+str(cont)
                cont=1
                letra=cadena[i]
    cadena_nueva += letra + str(cont)
    if (len(cadena_nueva)<(len(cadena))):
        return cadena_nueva
    else:
        return cadena
#solo para subcadenas de 4 elementos
def hash_subcadena(cadena,m):
    h=(ord(cadena[0])*10^4+ord(cadena[1])*10^3+ord(cadena[2])*10^2+ord(cadena[3])*10)%m
    #print(h)
    return h
    #m=longitud del universo
    #hacerlo generico con un for

#punto8
def ocurrencia (cadena,subcadena):
    dictionary=[]
    for i in range (len(cadena)-len(subcadena)+1):
        sublista=[]
        
        for j in range (len(subcadena)):  
            sublista.insert(j,cadena[i+j])
        tupla=(sublista,i)
        #if sublista == list(subcadena):
            #print(i)
        dictionary.insert(hash_subcadena(sublista,len(cadena)),tupla)
    haski_p=hash_subcadena(subcadena,len(cadena)) #key de la subcadena
    print(dictionary)
    print((dictionary[haski_p][1]))
    return(dictionary[haski_p][1]) #devuelve la posicion de la cadena donde se encnotro la subacadena



#punto9
def conjuntos(S,T):
    hash=CreateHashTable(len(T))
    for numeroT in T:
        Insert(hash,hash_mode(numeroT,len(T)),numeroT)
    for numeroS in S:
        if search(hash,hash_mode(numeroS,len(T))) != numeroS:
            return False
    return True   