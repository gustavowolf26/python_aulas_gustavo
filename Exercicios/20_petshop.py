#==============================================================================================================
#Autor: Gustavo Simoes 
#Versao:  1.0
#Data: 26/06/2024
#Algoritmo: 
#Descrição: Crie uma matriz e apresente ela no final da execução, aonde existe duas colunas [tipo, nome]
#           e 4 linhas preenchidas com o tipo de animal e seu respectivo nome
#
#           #       tipo      nome
#           0       gato      frajola
#           1       cão       coragem
#           2       passarinho Pica-Pau
#           3       Urso       Catatau
#===============================================================================================================

# cabecalho = ['#','tipo', 'nome']
# linha1 = ['0','gato', 'frajola']
# linha2 = ['1','cão', 'Coragem']
# linha3 = ['2','Passarinho', 'Pica-Pau']
# linha4 = ['3','Urso', 'Catatau']

# tabela = [cabecalho, linha1, linha2, linha3, linha4]

# ou também pode ser:
tabela = [
['#','tipo', 'nome'],
['0','gato', 'frajola'],
['1','cão', 'Coragem'],
['2','Passarinho', 'Pica-Pau'],
['3','Urso', 'Catatau']
]


# print(tabela[0][0], tabela[0][1], tabela[0][2]) #ou print(f'{tabela[0][0]} {tabela[0][1]} {tabela[0][2]}')
# print(tabela[1][0], tabela[1][1], tabela[1][2]) #ou print(f'{tabela[1][0]} {tabela[1][1]} {tabela[1][2]}')
# print(tabela[2][0], tabela[2][1], tabela[2][2]) #ou print(f'{tabela[2][0]} {tabela[2][1]} {tabela[2][2]}')
# print(tabela[3][0], tabela[3][1], tabela[3][2])
# print(tabela[4][0], tabela[4][1], tabela[4][2])


#criando um for, para variar linha e coluna, para que não seja necessário printar varias vezes e le faça em loop

for linha in range (5): #varia as linhas
    linha_completa = ''
    for coluna in range (3): #varia as colunas

        linha_completa += tabela[linha][coluna] + ' | '#consegue fazer os itens ficarem na mesma linha, apresentados da forma de lista 

    print(f'{linha_completa}')