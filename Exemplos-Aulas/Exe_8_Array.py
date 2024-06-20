'''
Autor: Danielle Ozaki
Data: 14/06/2024
Versão: 1.0
Algoritmo: Estudo do tipo de dado Array
Descrição: 

'''
#===========================================

aluno1 = 'Danielle' 
aluno2 = 'Luana' 
aluno3 = 'Henrique' 
aluno4 = 'Iury' 
aluno5 = 'Beatriz'
aluno6 = 'Rafaella'             #OU dessa forma vc consegue mudar os nomes sempre sem dar erro

#   posição         0         1         2         3         4           5
turmaPython = ['Danielle', 'Luana', 'Henrique', 'Iury', 'Beatriz', 'Rafaella'] #array
print(turmaPython)

turmaPython[1] = 'Bianca' #atribuir um nome nome para a antiga posição
print(turmaPython)

turmaPython = ['Luana', 'Henrique', 'Iury', 'Beatriz', 'Rafaella', 'Danielle']
print(turmaPython)

print(f'posição 0 do vetor turmaPython é igual {turmaPython[0]}')
print(f'posição 1 do vetor turmaPython é igual {turmaPython[1]}')
print(f'posição 2 do vetor turmaPython é igual {turmaPython[2]}')
print(f'posição 3 do vetor turmaPython é igual {turmaPython[3]}')
print(f'posição 4 do vetor turmaPython é igual {turmaPython[4]}')
print(f'posição 5 do vetor turmaPython é igual {turmaPython[5]}')

#================================================================
alunoPythonNoturno = [4, 5, 3, 2, 0, 1]
print(alunoPythonNoturno)

alunoPythonNoturno[0] = 'Iury'
alunoPythonNoturno[1] = 'Beatriz'
alunoPythonNoturno[2] = 'Rafaella'
alunoPythonNoturno[3] = 'Danielle'
alunoPythonNoturno[4] = 'Luana'
alunoPythonNoturno[5] = 'Henrique'

print(alunoPythonNoturno)