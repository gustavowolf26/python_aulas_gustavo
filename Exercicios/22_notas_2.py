#==============================================================================================================
#Autor: Gustavo Simoes 
#Versao:  1.0
#Data: 26/06/2024
#Algoritmo: 
#Descrição: Jogo da velha 
#           
#           
#           
#           
#           
#           
#           
#===============================================================================================================

jogador1 = ''
jogador2 = ''
rodadas = 0
jogador = 'X'

jogador1 = input('Insira o nome do jogador 1: ')
print('jogador 1 é o x e inicia a rodada')
jogador2 = input('Insira o nome do jogador 2: ')
print('jogador 2 é o bolinha')
# nome = jogador1

tabuleiro =[['1','2','3'],
            ['4','5','6'],
            ['7','8','9']
]

def mostrar_vencedor(vencedor):
    print('temos um vencedor', vencedor) 

while rodadas < 10:
    
    posicao = input(f'digite a posicao escolhida {jogador} : ')
    posicao_encontrada = False

    for linha in range(3):
        linha_completa = ''

    

        for coluna in range(3):
            if posicao == tabuleiro[linha][coluna]:
                tabuleiro[linha][coluna] = jogador
                posicao_encontrada = True       
            linha_completa += (f'| {tabuleiro[linha][coluna]} | ')
            

        print(linha_completa)
            
    if posicao_encontrada == True:
        rodadas += 1
        if jogador == 'X':
            jogador = 'O'
            
        else:
            jogador = 'X'
           
    else:
        print('posiçao nao encontrada')

    if (tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2] or 
        tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2] or 
        tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2] or  
        tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0] or 
        tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1] or 
        tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2] or 
        tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] or 
        tabuleiro[2][0] == tabuleiro[1][1] == tabuleiro[2][0]):
        mostrar_vencedor(jogador)

        if jogador == 'O':
            print( 'o vencedor é', jogador1)
        else:
            print('o vencedor é', jogador2)

        break





