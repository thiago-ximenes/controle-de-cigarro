from datetime import date
today = date.today()
todaybr = today.strftime('%d/%m/%Y')

cig = ['DERBY AZUL','DERBY VERMELHO', 'DERBY PRATA', 'HOLLYWOOD VERMELHO', 'HOLLYWOOD AZUL', 'HOLLYWOOD MENTA', 'KENT VERMELHO MAÇO', 'KENT VERMELHO BOX', 'KENT AZUL MAÇO', 'KENT AZUL BOX', 'CARLTON', 'ROTHMANS AZUL', 'ROTHMANS VERMELHO', 'LUCKY STRIKE AZUL', 'LUCKY STRIKE DOUBLECLICK', 'RITZ', 'PLAZA CURTO', 'PLAZA LONGO', 'LUXOR', 'CHESTERFIELD AZUL', 'CHESTERFIELD VERMELHO', 'MALBORO BOX VERMELHO', 'MALBORO BOX GOLD', 'ROTHMANS PRATA']
pr = [6.75, 6.75, 6.75, 7.25, 7.25, 7.25, 8, 8.25, 8, 8.25, 8.75, 5.25, 5.25, 7.25, 7.75, 6.75, 6.75, 6.75, 6.75, 5.25, 5.25, 8.75, 8.75, 5.25 ]
estoque = []
rest = []
entrada = []

print(todaybr)
frase = 'DIGITE ABAIXO QUANTOS CIGÁRROS HÁ \033[7mNO ESTOQUE:\033[m'
print(frase)
print('-'*55)

for c in range(0, len(cig)): #ESTOQUE
    estoque.append(int(input('{} em ESTOQUE: '.format(cig[c]))))
print('-'*55)
x = str(input('Existe nova \033[m7mENTRADA de cigarro? [S/N]:\033[m '))
print('-'*55)
for c in range(0, len(cig)): #ENTRADA
    if x == 's':
        entrada.append(int(input('{} em ENTRADA: '.format(cig[c]))))
    elif x == 'n':
        entrada.append(0)
    else:
        print('\033[41mENTRADA INVÁLIDA!\033[m')

print('-'*55)
print("DIGITE ABAIXO QUANTOS CIGÁRROS \033[7mRESTARAM NO DIA:\033[m")
print('-'*55)
for c in range(0, len(cig)): # RESTANTE
    rest.append(int(input('{} restaram: '.format(cig[c]))))
print('\n'*50)

                    # PLANILHA PARA SER COPIADA
print('\033[7m{:>25}| ESTOQUE | ENTRADA | TOTAL | RESTANTE | VENDIDOS | TOTAL R$|\033[m'.format(' '))
for c in range(0, len(cig)):
    print(('\033[7m\033[4m|{:>25}\033[|{:^9}|{:^9}|{:^7}|{:^10}|{:^10}|{:^9.2f}|\033[m'.format(cig[c], estoque[c], entrada[c], estoque[c] + entrada[c], rest[c], (estoque[c] + entrada[c]) - rest[c], ((estoque[c] + entrada[c]) - rest[c]) * pr[c]  )))
print()
soma = 0
for c in range(0, len(cig)):
    soma += ((estoque[c] + entrada[c]) - rest[c]) * pr[c]
#TOTAL GERAL
print('TOTAL GERAL: R$ {:.2f}'.format(soma))
print()

