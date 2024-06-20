'''
Autor: Danielle Ozaki
Data: 14/06/2024
Versão: 1.0
Algoritmo: Chamada
Descrição: Faça um algoritmo que receba o número da chamada dos alunos
           do curso de python no periodo noturno do SENAI e apresente
           o nome do aluno escolhido.
'''
#===================================================================================

#Variáveis
alunosPython = ['Luana', 'Gustavo', 'Danielle', 'Felipe', 'Jãoa P', 'Thiago', 
                'Vitor', 'Jose', 'Arthur', 'Pedrão', 'Mauricio', 'Davi', 'Kawan', 
                'Andrey', 'Lucas', 'Diego', 'João', 'Ana', 'Vinicius', 'Adriel', 
                'Patrick', 'Bruno', 'Professor Girafalles Pocket']      #22 PESSOAS

while True:
    numChamada = 0 
    numChamada = int(input('Insira o número da chamada: '))
    print(alunosPython[numChamada])

   
    continuar = input('Digite S para sair e C para continuar: ')

    if continuar == 's' or 'S':
        break