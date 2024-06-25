#==============================================================================================================
#Autor: Gustavo Simoes 
#Versao:  1.0
#Data: 13/06/2024
#Algoritmo: 
#Descrição: Escreva um algoritmo que receba dois valores, sendo que o primeiro deve ser menor que o segundo,
#           O programa deve apresentar todos os numeros impares contidos nesta sequencia.
#           (modulo %. Exemplo: 7%2 = 1) -> essa conta com "%" retorna o valor de resto da divisão,
#           todos numeros divididos por 2 que derem resto = 1, são impares.
#           
#           
#===============================================================================================================

#Inicio

#Variáveis

n1 = 0
n2 = 0
resto = 0

#entrada
n1 = int(input('escreva o valor inicial do seu range: '))
n2 = int(input('escreva o valor final do seu range: '))


#processamento


for numrange in range(n1, n2):

    resto = numrange%2 #resto 0 é par, resto 1 é impar
    
    if resto == 1:
        print(numrange)

