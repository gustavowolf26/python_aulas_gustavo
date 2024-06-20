#========================================================================
#Autor: Gustavo Simoes 
#Versao:  1.0
#Data: 04/06/2024
#Descrição: Escreva um programa que leia a velocidade maxima permitida em 
#           uma avenida e a velocidade com que o motorista estava dirigindo
#           nela e calcule a multa que uma pessoa vai receber:
#
#           velocidade ultrapassada    valor da multa
#           até 10 km/h                 R$ 50
#           11 a 30 km/h               R$ 100
#           mais de 31 km/h             R$ 200
#=========================================================================

#Inicio

#Variáveis
velocidade_via = 50
velocidade_condutor = 0

# entrada
velocidade_condutor = int(input('digite a velocidade do motorista: '))

#processamnto
print('A velocidade máxima da via é', velocidade_via, 'km/h')
print('A velocidade do motorista é', velocidade_condutor, 'km/h')

