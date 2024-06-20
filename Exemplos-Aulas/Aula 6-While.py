#========================================================================
#Autor: Gustavo Simoes 
#Versao:  1.0
#Data: 07/06/2024
#Descrição: Estudos da estrutura de repetição "While".
#           
#           
#           
#           
#=========================================================================

indice = 1
while indice <= 21:
    print(indice, 'gustavo')
    indice = indice + 1 #indice +=1

#=========================================================================

indice2 = 10
while indice2 > 0:
    print(indice2, 'gustavo')
    indice2 = indice2 - 1

#=========================================================================

indice3 = 1
while True:
    print(indice3)
    indice3 = indice3 + 1 

    if indice3 > 5:
        break

# =========================================================================

opcao = ''
indice4 = 1

while True:
    opcao = input('Digite S para finalizar o programa: ')
    indice4 = indice4 + 1

    if indice4 == 5 or opcao == 's':
        break


#=========================================================================