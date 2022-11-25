import random
import math

print('Qual a quantidade de numeros você deseja ?')
total = input()
total_numero = int(total)
i = 0
lista = []
print('Certo vamos gerar ', total,' números')
lista = random.sample(range(10),total_numero)
print(lista)
print('Vamos organizar a lista com InsertionSort')

k = 0
while k < len(lista): 
    j = 0
    while j < k:        
        if lista[k] < lista [j]:
            aux = lista[k]
            lista[k] = lista[j]
            lista[j] = aux
            j = j + 1
        else:                     
            j = j + 1
    print(lista)
    print(k)    
    k = k + 1  



    



