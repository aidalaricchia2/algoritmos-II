import string
"Ejercicio 7"
def reduce_len(string):
    string = str(string)  #convierte el string si no es
    new_string = ""
    flag=False
    for i in range(len(string)):
        if flag == False:
            if i == len(string)-1 or string[i] != string[i+1]:
                new_string += string[i]
            else:
                flag = True
        else:
            flag = False

    return new_string

#print(reduce_len('aaabccddd'))

"Ejerccicio 8"

def  isContained(string1,string2):
    palabra = sorted(string1)  #ordena la primer entrada
    indice = 0  
    string2 = list(string2)
    for char in palabra:
        if char == string2[indice]:
            indice += 1  #recorre

            if indice == len(string2):
                return True  #encontrada
    return False  

#print(isContained('aaaaabbbbbccc','abc'))

"Ejercicio 9"

#def is_pattern_contained(string, pattern, c):
"Ejercicio 11"
'''Sean el texto T y el patrón P de longitudes m y n respectivamente.
Plantee un algoritmo para encontrar el mayor prefijo de P que se encuentra en T en O(n+m).'''

def prefijo_mayor(T, P):
    m = len(T)
    n = len(P)
    i = 0  
    j = 0  
    pre_mayor = 0  #len(del mayor prefijo encontrado)
    flag=True
    while i < m and j < n and flag==True:
        if T[i] == P[j]:
            i += 1
            j += 1
            pre_mayor += 1
        else:
            flag=False
    return T[:pre_mayor]


"Ejercicio 12 AEF"
'''FINITE-AUTOMATON-MATCHER.T; ı; m/
1 n D T:length
2 q D 0
3 for i D 1 to n
4 q D ı.q; T Œi/
5 if q == m
6 print “Pattern occurs with shift” i  m'''

def finite_automaton_matcher(t,p):
    n=len(t)
    q=0
    matriz = transition_function(t, p)
    for i in range (n):
        q=matriz[q,t[i]]
        if q==len(p):
            print('patter occurs withshift',i-len(p))


'''COMPUTE-TRANSITION-FUNCTION.P; †/
1 m D P:length
2 for q D 0 to m
3 for each character a 2 †
4 k D min.m C 1; q C 2/
5 repeat
6 k D k  1
7 until Pk ❂ Pqa
8 ı.q; a/ D k
9 return ı'''

def transition_function(p, alf):
    m = len(p)
    filas = m
    columnas = len(alf)
    valor_inicial = 0
    matriz = [[valor_inicial] * columnas for _ in range(filas)]

    for i in range(m):
        for j in range(len(alf)):
            k = min(m + 1, i + 2)
            k =k- 1
            while sufijo(p[0:k], (p + j)[0:i]):
                matriz[i][j] = k
    return matriz

def sufijo(string1, string2):
   return string2[len(string2) - len(string1):len(string2)] == string1



"Ejercicio 13  Rabin-Karp"

def RK(s,p):
    for i in range (len(s)-len(p)+1): #+1 para que tome el ultimo
        sub_s= s[i:len(p)+i] #nos devolvera las subcadenas de s con longitud de p
        if hash(sub_s) == hash(p):
            if sub_s==p:
                return True
    return False
def hash(string):
   unique_num = 0
   index_pow = 0
   for i in range(len(string)-1, 0, -1):
      unique_num += pow(128, index_pow) * ord(string[i])
      index_pow += 1
   return unique_num % len(string)

#print(RK('asdfghjkl','hjk'))


"Ejercicio 14 KMP"
def pi_function(string):
    m=len(string)
    pi=[0]*len(string)
    pi[0]=0
    i=0
    for q in range(1,m,1):
        while i>0 and string[i] != string[q]:
            i=pi[i]
        if string[i] == string[q]:
            i=i+1
        pi[q]=i
    return pi

#print(pi_function('asdaasdasdasdasdasdasd'))
def KMP(t,p):
    n=len(t)
    m=len(p)
    pi=pi_function(p)
    i=0
    for j in range(1,n,1):
        while i>0 and p[i]!=t[j]:
            i=pi[i]
        if p[i]==t[j]:
            i=i+1
        if i==m:
            return True
    return False

#print(KMP('aashshaabaca','abaca'))