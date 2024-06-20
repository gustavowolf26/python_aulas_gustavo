#=========================================================
#Autor: Gustavo Simoes 
#Versao:  1.0
#Data: 24/05/2024
#Descrição: Algoritmo de conversão de reais para dólares
#           R$ para $, e apresente a quantidade em dolar
#           Exemplo de execução:
#           insira o valor em real: 5000
#           insira o valor do dólar hoje: 
#==========================================================

#Inicio
#Entrada

# Valor de entrada em reais e cotação do dolar hoje
real = float(input('Digite o valor que você possui em reais: R$ '))
cotaçaoDolar = float(input('Digite o valor do Dólar hoje: $ '))


#processamento

#calculo de conversão
conversao = real/cotaçaoDolar


#saida
print('Esse valor é igual a: $', conversao, 'dólares')
