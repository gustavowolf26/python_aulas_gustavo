#========================================================================
#Autor: Gustavo Simoes 
#Versao:  1.0
#Data: 28/05/2024
#Descrição: O algoritmo exibe o nome de todos os lanches que podem ser 
#           escolhidos, o usuario escolhe de acordo com o número/código 
#           do lanche:
#           
#           nr.   lanche
#           1      BigMac
#           2      Quarteirão
#           3      McChicken
#           4      Cheddar McmMelt
#           5      Mcfish
#           
#=========================================================================

#Inicio


#Variáveis

pedido = ''

# nr. Lanche
l1 = 'Big Mac'
l2 = 'Quarteirão'
l3 = 'Mc Chicken'
l4 = 'Cheddar McMelt'
l5 = 'Mcfish'


#entrada
pedido = input('Digite o número do Lanche escolhido: \n Nr. Lanche \n 1. Big Mac \n 2. quarteirão \n 3. Mc Chicken \n 4. Cheddar McMelt \n 5. McFish \n')


# processamento
if pedido =='1':
    print('Você escolheu o', l1)

elif pedido == '2':
    print('você escolheu o', l2)

elif pedido == '3':
    print('você escolheu o', l3)

elif pedido == '4':
    print('você escolheu o', l4)

elif pedido == '5':
    print('você escolheu o',l5)
