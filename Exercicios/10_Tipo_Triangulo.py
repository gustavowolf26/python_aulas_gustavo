#==============================================================================================================
#Autor: Gustavo Simoes 
#Versao:  1.0
#Data: 07/06/2024
#Descrição: Escreva um programa que leia 3 valores e verifique se eles 
#           podem representar os lados em um triangulo.
#           
#           1 - Triangulo escaleno: triângulo que possui todos os lados com medidas diferentes
#           2 - triangulo isósceles: triângulo que possui dois lados com medidas iguais
#           3 - triangulo equilatero: triangulo que possui todos os lados com medidas iguais
#           
#           
#===============================================================================================================

#Inicio

#Variáveis

lado1 = 0
lado2 = 0
lado3 = 0
tipo_triangulo = ''


#entrada
lado1 = int(input('Insira o valor do lado 1: '))
lado2 = int(input('Insira o valor do lado 2: '))
lado3 = int(input('Insira o valor do lado 3: '))
saida = ''

#processamento

#verificando se a soma de dois lados do triangulo é maior que o terceiro e se todos os lados são maiores que zero
if ((lado1 + lado2) > lado3 and 
    (lado1 + lado3) > lado2 and 
    (lado2 + lado3) > lado1 and 
    lado1 > 0 and 
    lado2 > 0 and 
    lado3 > 0 ):
    print('Existe')

    #Equilatero
    if (lado1 == lado2 and lado2 == lado3): #lado1 == lado2 == lado3 (tbm funciona, mas somente no python)
        tipo_triangulo = 'Equilátero'

    #isóceles
    elif (lado1 ==lado2 or lado2 == lado3 or lado1 == lado3): 
        tipo_triangulo = 'isóceles'

    #Escaleno
    elif (lado1 != lado2 and lado2 != lado3 and lado1 != lado3):
        tipo_triangulo = 'Escaleno'

    print(tipo_triangulo)

else:
    print('Não Existe')







