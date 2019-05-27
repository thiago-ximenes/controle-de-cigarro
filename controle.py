from datetime import date
import estoque as est
import pandas as pd
import os
import json


today = date.today()
todaybr = today.strftime('%d/%m/%Y')
def clear():
    return os.system('cls' if os.name == 'nt' else 'clear')

#cig = ['DERBY AZUL','DERBY VERMELHO', 'DERBY PRATA', 'HOLLYWOOD VERMELHO', 'HOLLYWOOD AZUL', 'HOLLYWOOD MENTA', 'KENT VERMELHO MAÇO', 'KENT VERMELHO BOX', 'KENT AZUL MAÇO', 'KENT AZUL BOX', 'CARLTON', 'ROTHMANS AZUL', 'ROTHMANS VERMELHO', 'LUCKY STRIKE AZUL', 'LUCKY STRIKE DOUBLECLICK', 'RITZ', 'PLAZA CURTO', 'PLAZA LONGO', 'LUXOR', 'CHESTERFIELD AZUL', 'CHESTERFIELD VERMELHO', 'MALBORO BOX VERMELHO', 'MALBORO BOX GOLD', 'ROTHMANS PRATA']
#pr = [6.75, 6.75, 6.75, 7.25, 7.25, 7.25, 8, 8.25, 8, 8.25, 8.75, 5.25, 5.25, 7.25, 7.75, 6.75, 6.75, 6.75, 6.75, 5.25, 5.25, 8.75, 8.75, 5.25 ]
estoque = est.getEstoque()
rest = {}
total = {}
linhas = '-'*60

print('\n\n\n')
print(( todaybr + " VERIFIQUE O ESTOQUE ABAIXO").center(65))
print(linhas)
est.printEstoque(estoque)
input()
clear()
    
for i in estoque:
    print("DIGITE O RESTANTE EM ESTOQUE")
    print(i)
    qtd = int(input("quantidade: ").rstrip())
    rest.update({i:qtd})
    clear()


for i in estoque:
    clear()
    qtd_vendido = estoque[i]['qtd'] - rest[i]
    total_vendido = estoque[i]['preco'] * qtd_vendido
    total.update({i:{'qtd':qtd_vendido,'total':total_vendido}})

# print do relatorio com pandas
name = list(estoque.keys())
qtd_res = list(rest.values())
qtd_est = []
qtd_total = []
v_total = []
for i in estoque:
    qtd_est.append(estoque[i]['qtd'])
    qtd_total.append(total[i]['qtd'])
    v_total.append(total[i]['total'])

df = pd.DataFrame({"NOME DO PRODUTO": name,
                    "ESTOQUE":qtd_est,
                    #"ENTRADA":,
                    "RESTANTE":qtd_res,
                    "VENDIDOS":qtd_total, 
                    "TOTAL":v_total})

print(df)
soma = 0
for i in v_total : 
    soma += i 
print('\n')
print(("R$" + str(soma)).rjust(65))
input()

#update dos dados e gerando o backup
for i in estoque:
    estoque[i]['qtd'] = rest[i]
est.updateEstoque(estoque)
#for i in estoque:
#  #   print((i.ljust(1) + str(estoque[i]['qtd']).rjust(25)).ljust(30) + ('0' + '\t' +  str(rest[i])).center(20) +  (str(total[i]['qtd']) +  '\t' + str(total[i]['total'])).rjust(20))
   

#frase = "DIGITE ABAIXO QUANTOS CIGÁRROS HÁ" + "\033[1;30m" + "NO ESTOQUE:" + "\033[47m"
#print(frase + "\033[33m")
#print('-'*55)

#for c in range(0, len(cig)): #ESTOQUE
#    estoque.append(int(input('{} em ESTOQUE: '.format(cig[c]))))
#print('-'*55)
#x = str(input('Existe nova' +  '\033[37m' + 'ENTRADA de cigarro? [S/N]:'+'\033[37m'))
#print('-'*55)
#for c in range(0, len(cig)): #ENTRADA
#    if x == 's':
#        entrada.append(int(input('{} em ENTRADA: '.format(cig[c]))))
#    elif x == 'n':
#        entrada.append(0)
#    else:
#        print('\033[41mENTRADA INVÁLIDA!\033[m')

#print('-'*55)
#print("DIGITE ABAIXO QUANTOS CIGÁRROS \033[7mRESTARAM NO DIA:\033[m")
#print('-'*55)
#for c in range(0, len(cig)): # RESTANTE
#    rest.append(int(input('{} restaram: '.format(cig[c]))))
#print('\n'*50)

                    # PLANILHA PARA SER COPIADA
#print('\033[7m{:>25}| ESTOQUE | ENTRADA | TOTAL | RESTANTE | VENDIDOS | TOTAL R$|\033[m'.format(' '))
#for c in range(0, len(cig)):
#    print(('\033[7m\033[4m|{:>25}\033[|{:^9}|{:^9}|{:^7}|{:^10}|{:^10}|{:^9.2f}|\033[m'.format(cig[c], estoque[c], entrada[c], estoque[c] + entrada[c], rest[c], (estoque[c] + # #entrada[c]) - rest[c], ((estoque[c] + entrada[c]) - rest[c]) * pr[c]  )))
#print()
#soma = 0
#for c in range(0, len(cig)):
#    soma += ((estoque[c] + entrada[c]) - rest[c]) * pr[c]
#TOTAL GERAL
#print('TOTAL GERAL: R$ {:.2f}'.format(soma))
#print()

