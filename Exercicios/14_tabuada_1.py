#==============================================================================================================
#Autor: Gustavo Simoes 
#Versao:  1.0
#Data: 13/06/2024
#Algoritmo: 
#Descrição: Escreva um algoritmo que receba dois valores, sendo que p primeiro deve ser menor que o segundo,
#           O programa deve apresentar todos os numeros impares contidos nesta sequencia.
#           (modulo %. Exemplo: 7%2 = 1) -> essa conta com "%" retorna o valor de resto da divisão,
#           todos numeros divididos por 2 que derem resto = 1, são impares.
#           
#           
#===============================================================================================================

#Inicio

#Variáveis

multiplicador = 0
numero = 0 


# entrada

for multiplicador in range(11): # de 0 a 10
    for numero in range(11): # de 0 a 10
        resultado = multiplicador * numero
        print(f' {multiplicador} x {numero} = {resultado}') # apresenta os resultados
    

