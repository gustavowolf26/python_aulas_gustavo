'''
Autor: Danielle Ozaki
Data: 17/06/2024
Versão: 1.0
Algoritmo: Array
Descrição: Estudo do tipo de dado Array (vetor)
'''
# ====================================================

carros = ['VW']

carros.append('GM')
carros.append('Ford')
carros.append('Fiat')
carros.append('Renalt') #adiciona na última posição o valor indicado

print(carros)

carros.remove('Ford')   #Remove item indicando o valor 
print(carros)

carros.pop(3)   #Remove iten indicado index
print(carros)

print(len(carros))  #Numero de quantos vetores tem
carros.pop(len(carros) - 1) #Deleta sempre a última posição do Array
print(carros)