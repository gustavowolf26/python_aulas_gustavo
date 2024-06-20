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

n_1 = 0
n_2 = 0
ran = (n_1, n_2)
resto = 0
sequencia = 0
multiplicador = 0

#entrada
n_1 = int(input('escreva um numero inteiro: '))
n_2 = int(input('escreva um outro numero, menor que o primeiro e inteiro: '))


#processamento


for sequencia in range(n_1, n_2):

    resto = sequencia%2

    print(sequencia)


