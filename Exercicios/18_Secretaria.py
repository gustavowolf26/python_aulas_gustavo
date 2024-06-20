'''
Autor: Danielle Ozaki
Data: 17/06/2024
Versão: 1.0
Algoritmo: Secretaria
Descrição: Faça um programa que adicione alunos ao sistema de escola
            (array) ou remova um aluno específico.
            Nesse sistema deve estar previsto um menu com 3 opções:

        Sistema SENAI
        1 - Adicionar aluno
                Insira o nome do aluno:
        2 - Remover aluno
                Insira o nome do aluno a ser removido:
        3 - Apresentar alunos
                ['João', 'Pedro', 'Luana']
        4 - Sair
            Insira a opção desejada:

'''
# =============================================================================

opcao = 0       #numero inteiro
alunos = []     #array
novoAluno = ''  #string adicionar aluno novo 


while True:
    print('=='*30)
    opcao = int(input('OPÇÕES \n 1- Adicionar aluno \n 2- Remover aluno \n 3- Apresentar aluno \n 4- Sair \n Qual opção desejada? '))

    if (opcao == 1):
        print('=='*30)
        print('Adicionar aluno')
        novoAluno = input('Insira o nome do aluno: ')
        alunos.append(novoAluno)

    elif (opcao == 2):
        print('=='*30)
        print('Remover aluno')
        remover = input('Digite o nome do aluno para ser removido: ')
        alunos.remove(remover)

    elif (opcao == 3):
        print('=='*30)
        print('Alunos no sitema: ')
        print(alunos)
        
    else:
        print('=='*30)
        print('Saindo...')
        break
