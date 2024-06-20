#=========================================================
#Autor: Gustavo Simoes 
#Versao:  1.0
#Data: 24/05/2024
#Descrição: Faça um algoritmo que receba 5 notas e imprima
#           a média final do Aluno
#           Exemplo de execução
#           nota1: 10
#           nota2: 10
#           nota3: 10
#           nota4: 10
#           nota5: 10
#           média final: 10
#==========================================================

#Inicio


#Entrada

#pergunta o numero de notas que serão inseridas, para efetuar o calculo de média
numeroNotas = int(input('Quantas notas são? (valor máximo de 5 notas): '))

#informa para digitar o valor das notas
print('digite o valor das notas do Aluno')

#entrada das notas pelo usuario
#Condiciona a entrada de notas, se for menor que 5 faz o calculo e insere a quantidade para calculo de notas na entrada
if numeroNotas > 5:
    print('O numero deve ser menor que 5 notas')

else :
    if numeroNotas == 5:
        nota1 = int(input('primeira nota: '))
        nota2 = int(input('segunda nota: '))
        nota3 = int(input('terceira nota: '))
        nota4 = int(input('quarta nota: '))
        nota5 = int(input('quinta nota: '))
        somaNotas = nota1 + nota2 + nota3 + nota4 + nota5
    else:
        if numeroNotas == 4:  
            nota1 = int(input('primeira nota: '))
            nota2 = int(input('segunda nota: '))
            nota3 = int(input('terceira nota: '))
            nota4 = int(input('quarta nota: '))
            somaNotas = nota1 + nota2 + nota3 + nota4
        else:
            if numeroNotas == 3:
                nota1 = int(input('primeira nota: '))
                nota2 = int(input('segunda nota: '))
                nota3 = int(input('terceira nota: '))
                somaNotas = nota1 + nota2 + nota3
            else:
                if numeroNotas == 2:
                    nota1 = int(input('primeira nota: '))
                    nota2 = int(input('segunda nota: '))
                    somaNotas = nota1 + nota2


#Processamento
# calculo de média das notas
media = somaNotas / numeroNotas


#Saida
# Trás na saida a média das notsa que foram informadas
print('A média final do aluno é: ', media)