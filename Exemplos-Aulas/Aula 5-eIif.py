#========================================================================
#Autor: Gustavo Simoes 
#Versao:  1.0
#Data: 28/05/2024
#Descrição: Estudos do condicional IF ... ELIF 
#           
#           
#           
#           
#=========================================================================

#Inicio


#Variáveis
nota = 0

#entrada
nota = int(input('Digite o valor da nota: '))

# processamento
if nota >= 6:
    print('Aluno Aprovado')

    # saida
    print(nota)
elif nota < 4:
    print('Aluno Reprovado')

else:
    print('Aluno em recuperação')