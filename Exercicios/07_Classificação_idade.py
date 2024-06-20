#========================================================================
#Autor: Gustavo Simoes 
#Versao:  1.0
#Data: 04/06/2024
#Descrição: Escreva um programa que leia a idade de um individuo e 
#           escreva a faixa etária a que pertence, de acordo com a tabela
#           abaixo
#           faixa etária    classificação
#           <12                 Criança
#           13~17               Adolescente
#           18~59               Adulto
#=========================================================================

#Inicio

#Variáveis

idade = 0
faixa = ''


#Entrada
idade = int(input('Digite a idade: '))


#Processamento
if idade < 12:
    faixa = 'Criança'

elif idade >= 13 and idade <= 17:
    faixa = 'Adolescente'

elif idade >= 18 and idade <= 59:
    faixa = 'Adulto'


# saida
print('A faixa etária que essa idade pertence é:', faixa)