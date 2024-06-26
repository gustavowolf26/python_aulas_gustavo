#========================================================================
#Autor: Gustavo Simoes 
#Versao:  1.0
#Data: 25/06/2024
#Descrição: Estudos do tipo de dado Array(vetor)
#           
#           
#           
#           
#=========================================================================

alunos_sala = ['Luana','Gustavo', 'Danielle']

#ou da seguinte forma também:

alunos_sala.append('Felipe') #adiciona mais um item dentro da lista do array
print(alunos_sala)

print (alunos_sala[2]) #printa o item de endereço e -> Danielle

#para printar todos da lista que estão dentro da variavel array, usando for

for indice in range(4): #decarando o range que queremos
    print(alunos_sala[indice])

#ou também:

for aluno in alunos_sala: #ao invés de fornecer um range, fornecemos a variavel array, que irá trazer os valores de cada posição
    print(aluno)

'''
alunos_sala.remove('Gustavo') #remove um valor de dentro do array indicado
print(alunos_sala)
'''

#posição       0        1          2
cabecalho = ['nome', 'idade', 'matricula']

#posição      0       1       2
dado_um = ['Pele', 'Eterno', '10']
print(dado_um[0]) #posição 0 --> 'Pele'


#montagem de matriz
#posição      0         1       
tabela = [cabecalho, dado_um] # dentro dessa variavel tabela(array), inclui-se cabecalho(array) e dado_um (array)


# matriz dica disposta da seguinte forma, estrutura:

# [            0         1          2
#        0 ['nome' ,  'idade' ,'matricula'],
#        1 ['Pele,',  'Eterno',    '10'   ]
# ]

# coordenadas [L][C] --> L = linha e C = coluna
print(tabela[0][1]) # --> traz a informação da linha 0, coluna 1 --> idade
print(tabela[1][2]) # --> traz a informação da linha 1, coluna 2 --> 10
print(tabela[1][0]) # --> traz a informação da linha 1, coluna 0 --> Pele
