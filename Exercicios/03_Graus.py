#=========================================================
#Autor: Gustavo Simoes 
#Versao:  1.0
#Data: 24/05/2024
#Descrição: Conversão de Graus Celsius, para Kelvin e 
#           Fahrenheit
#           Equações de conversão:
#           fahrenheit - (Celsius x 1.8) + 32
#           kelvin -   celsius + 273
#           Digite o valor em Celsius: 
#           Retorna o valor em Kelvin e Fahrenheit
#==========================================================

#Inicio

#Entrada
valorCelsius = float(input('Digite o valor em graus Celsius\n'))



#Processamento
print(valorCelsius, '°C')

#Converte para Kelvin
valorKelvin = valorCelsius +273

#converte para fahrenheit
valorFahrenheit = (valorCelsius * 1.8) + 32


#Saida
print('O valor em kelvin é: ', valorKelvin, 'K')
print('O valor em Fahrenheit é: ', valorFahrenheit, '°F')