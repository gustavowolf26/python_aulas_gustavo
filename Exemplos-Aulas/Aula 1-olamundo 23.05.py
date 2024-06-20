
#=========================================================
#Autor: Gustavo Simoes 
#Versao:  1.0
#Data: 23/05/2024
#Descrição: Algoritmo que recebe o nome do usuário e
#           exibe uma frase de saudação concatenada com
#           a entrada do usuário.
#==========================================================
#Observações:
# 
#           a) Para iniciar um comentário utiliza-se o "#'
#           b)no visual studio utilizar o comando ctrl+;
#             para comentar em bloco. 
#==========================================================


#Inicio


#entrada
nome = input('Qual e o seu nome?') #variavel qe faz a leitura de entrada do nome que a pessoa digitar

#processamento
mensagem = 'olá, seja bem vindo ' # variavel de mensagem padrão para todos
frase = mensagem + nome # variavel que concatena a mensagem com o nome

#saida
print(frase) #exibe a frase com o nome do usuário

