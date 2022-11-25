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

k = 0
j = 0
while k < len(lista):
    menor = lista[k]    
    while j < len(lista):

        if menor >= lista[j]:
            menor = lista[j]
            troca = j
        j = j + 1
    aux = lista[k]
    lista[k] = lista[troca]
    lista[troca] = aux
    k = k + 1
    j = k 
    
print(lista)
    



