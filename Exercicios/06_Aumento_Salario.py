#========================================================================
#Autor: Gustavo Simoes 
#Versao:  1.0
#Data: 04/06/2024
#Descrição: O algoritmo exibe recebe um valor de salário de um funcionário 
#           calcula e mostra o novo salário, sabendo que:
#           condições:
#           Salário < R$1000,00 - aumento de 25%
#           Salário >= R$1000,00 e < R$2000,00 - aumento de 15%
#           Salário >= R$2000,00 - aumento de 10%
#=========================================================================

#Inicio

#Variáveis

salario = 0
salarionovo = 0

#Entrada

salario = float(input('Digite o valor do salário do funcionário  '))

print('salário digitado foi R$', salario)


#processamento 

if salario < 1000:
    salarionovo = salario*1.25

elif salario >= 1000 and salario < 2000:
    salarionovo = salario*1.15

elif salario >= 2000:
    salarionovo = salario*1.10

#saida
print('O novo salário é de R$', round(salarionovo))


 
