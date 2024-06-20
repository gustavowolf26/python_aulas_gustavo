#========================================================================
#Autor: Gustavo Simoes 
#Versao:  1.0
#Data: 28/05/2024
#Descrição: Calcular a área do circulo, dado o Raio
#           no valor de entrada
#           Fórmula:
#           pi*R^2
#           
#     OBS:  Para arredondar automatico um número é possivel    
#           utilizar o comando 'round':
#           round(3.141516, número de casas decimais após a virgula)
#=========================================================================

#Inicio


#Variáveis
raio = 0
pi = 3.14
area = 0


#Entrada

#Valor de entrada do Raio do circulo
raio = float(input("Digite o Valor do Raio do Circulo em metros: "))

#processamento
area = pi*(raio**2)

#saida
print("O valor da área do circulo para um raio =", raio, "é de", area, "m^2")
