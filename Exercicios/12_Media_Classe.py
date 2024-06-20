#==============================================================================================================
#Autor: Gustavo Simoes 
#Versao:  1.0
#Data: 11/06/2024
'''
Algoritmo "Média turma"
Descrição   : Faça um programa que receba duas notas de seis alunos. 
                Calcule e mostre:
            	A média aritmética das duas notas de cada aluno; e
            	A mensagem que está na tabela a seguir:
                    Média Aritmética	Mensagem
                    Até 3	            Reprovado 
                    Entre 3 e 7 	    Exame
                    De 7 para cima	    Aprovado

            	O total de alunos aprovados;
            	O total de alunos de exame;
            	O total de alunos reprovados;
            	A média da classe.
'''
#===============================================================================================================

#Inicio

#Variáveis

n1 = 0
n2 = 0
media = 0
aluno = 0
situaçao = ''
reprovados = 0
exame = 0
aprovados = 0
media_classe = 0
qtd_alunos = 6

#Entrada

while True:

    aluno = aluno + 1
  
    n1 = float(input(f'Digite a Nota 1 do aluno {aluno}:')) #formato para colocar ao ivés de usar virgula. coloca o f na frente e abre
                                                            #chaves para colocar a variavel
    n2 = float(input(f'Digite a Nota 2 do aluno {aluno}:'))
    media = (n1 + n2)/ 2
    media_classe = media_classe + media # pega o valor de media e soma com o valor de média da classe em cada loop. 
                                        # salvando assim a soma de todas as medias dentro da variavel 'media_classe'


    if media <= 3:
        situaçao = 'Reprovado'
        reprovados += 1 # mesma coisa que reprovados = reprovados + 1 

    elif media > 3 and media <= 7:
        situaçao = 'Exame'
        exame += 1
    
    elif media >= 8:
        situaçao = 'Aprovado'
        aprovados += 1

    print(round(media, 2) ,situaçao)

    if aluno == qtd_alunos:
        break



#Saida
print('total de alunos reprovados: ', reprovados)
print('total de alunos aprovados: ', aprovados)
print('total de alunos de exame: ', exame)
print('A média da classe foi: ', media_classe / qtd_alunos) #pega a soma das medias dos alunos e divide pela quantidade de alunos que foi setada