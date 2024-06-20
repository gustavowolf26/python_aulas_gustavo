#==============================================================================================================
#Autor: Gustavo Simoes 
#Versao:  1.0
#Data: 07/06/2024
#Descrição: Escreva um programa que solicite para o usuário a senha cadastrada, caso a senha seja digitada 
#           incorretamente 3 vezes ele finaliza o programa.  
#           senha: senai115
#          
#           
#           
#===============================================================================================================

#Inicio

#Variáveis

senha = ''
senha_padrao = 'senai115'
tentativas = 3


#Entrada

while True:
    senha = input('Digite a sua senha \n')


    if senha == senha_padrao:
        print('Acesso permitido')
        break
    else:
        tentativas = tentativas - 1
        print('Voce só possui mais',tentativas, 'tentativas')

    if tentativas <= 0 :
        print('Acesso bloqueado')
        break

   
        




    