'''
Autor: Danielle Ozaki
Data: 17/06/2024
Versão: 1.0
Algoritmo: Mês
Descrição: Faça um algoritmo que receba o número do mês e apresente 
            ele por extenso:
            !Sem utilizar condicional!
'''
#=====================================================================

mes = ['', 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 
       'Julho', 'Agosto', 'Outubro', 'Novembro', 'Dezembro']

while True: 
    numMes = 0
    numMes = int(input('Qual o número do mês: '))
    print(mes[numMes])

   