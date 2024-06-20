#========================================================================
#Autor: Gustavo Simoes 
#Versao:  1.0
#Data: 04/06/2024
#Descrição: O algoritmo exibe recebe um valor referente a um mês, dado  
#           por uma lista, e mostra qual é o mês relativo a esse número
#           
#          Código   Mes
            # 1       janeiro
            # 2       fevereiro
            # 3       março
            # 4       abril
            # 5       maio    
            # 6       junho
            # 7       julho
            # 8       agosto
            # 9       setembro
            # 10      outubro
            # 11      novembro
            # 12      dezembro

#           
#=========================================================================

#Inicio

#Variáveis

mes = 0
nome_mes = 0

#Entrada

mes = int(input('Digite o número do Mês: '))


#processamento

if mes == 1:
    nome_mes = 'janeiro'

elif mes == 2:
    nome_mes = 'Fevereiro'

elif mes == 3:
    nome_mes = 'Março'

elif mes == 4:
    nome_mes = 'Abril'

elif mes == 5:
    nome_mes = 'Maio'

elif mes == 6:
    nome_mes = 'junho'
    
elif mes == 7:
    nome_mes = 'julho'

elif mes == 8:
    nome_mes = 'Agosto'

elif mes == 9:
    nome_mes = 'Setembro'

elif mes == 10:
    nome_mes = 'Outubro'

elif mes == 11:
    nome_mes = 'Novembro'

elif mes == 12:
    nome_mes = 'Dezembro'

else:
    nome_mes = 'inxistente'

#saida

print('O mês é', nome_mes)