from datetime import date
today = date.today()
todaybr = today.strftime('%d/%m/%Y')
print(todaybr)
estoque = 'DIGITE ABAIXO QUANTOS CIGÁRROS HÁ NO ESTOQUE:'
print(estoque)
print('-'*55)
derbyazul = int(input('Digite quantos \033[44mDERBY AZUL\033[m existe em estoque: '))
derbyprata = int(input('Digite quantos \033[41mDERBY VERMELHO\033[m existe em estoque: '))
derbyverm = int(input('Digite quantos \033[47;30mDERBY PRATA\033[m existe em estoque: '))
hollverm = int(input('Digite quantos \033[44mHOLLYWOOD AZUL\033[m existe em estoque: '))
hollazul = int(input('Digite quantos \033[41mHOLLYWOOD VERMELHO\033[m existe em estoque: '))
hollmenta = int(input('Digite quantos \033[42;30mHOLLYWOOD MENTA\033[m existe em estoque: '))
kentvermmaco = int(input('Digite quantos \033[41mKENT VERMELHO MAÇO\033[m existe em estoque: '))
kentvermbox = int(input('Digite quantos \033[1;41mKENT VERMELHO BOX\033[m existe em estoque: '))
kentazulmaco = int(input('Digite quantos \033[44mKENT AZUL MAÇO\033[m existe em estoque: '))
kentazulbox = int(input('Digite quantos \033[1;44mKENT AZUL BOX\033[m existe em estoque: '))
carlton = int(input('Digite quantos \033[7;41mCARLTON\033[m existe em estoque: '))
rothazul = int(input('Digite quantos \033[44mROTHMANS AZUL\033[m existe em estoque: '))
rothverm = int(input('Digite quantos \033[41mROTHMANS VERMELHO\033[m existe em estoque: '))
rothprata = int(input('Digite quantos \033[47;30mROTHMANS PRATA\033[m existe em estoque: '))
lustazul = int(input('Digite quantos \033[44mLUCKY STRIKE AZUL\033[m existe em estoque: '))
lustdb = int(input('Digite quantos \033[7mLUCKY STRIKE \033[m\033[30;44mDOUBLE\033[m\033[42;30mCLICK\033[m existe em estoque: '))
ritz = int(input('Digite quantos \033[7mRITZ\033[m existe em estoque: '))
plazac = int(input('Digite quantos \033[7mPLAZA CURTO\033[m existe em estoque: '))
plazal = int(input('Digite quantos \033[7mPLAZA LONGO\033[m existe em estoque: '))
luxor = int(input('Digite quantos \033[43;30mLUXOR\033[m existe em estoque: '))
chestazul = int(input('Digite quantos \033[44mCHESTERFIELD AZUL\033[m existe em estoque: '))
chestverm = int(input('Digite quantos \033[41mCHESTERFIELD VERMELHO\033[m existe em estoque: '))
malbbverm = int(input('Digite quantos \033[1;41mMALBORO BOX VERMELHO\033[m existe em estoque: '))
malbbg = int(input('Digite quantos \033[1;30;43mMALBORO BOX GOLD\033[m existe em estoque: '))
print()   

    #Daqui pra baixo cigarros sobraram
print("DIGITE ABAIXO QUANTOS CIGÁRROS HÁ \033[7mRESTARAM NO DIA:\033[m")
print('-'*55)
derbyazuls = int(input('Digite quantos \033[44mDERBY AZUL\033[m restaram?: '))
derbypratas = int(input('Digite quantos \033[41mDERBY VERMELHO\033[m restaram?: '))
derbyverms = int(input('Digite quantos \033[47;30mDERBY PRATA\033[m restaram?: '))
hollverms = int(input('Digite quantos \033[44mHOLLYWOOD AZUL\033[m restaram?: '))
hollazuls = int(input('Digite quantos \033[41mHOLLYWOOD VERMELHO\033[m restaram?: '))
hollmentas = int(input('Digite quantos \033[42;30mHOLLYWOOD MENTA\033[m restaram?: '))
kentvermmacos = int(input('Digite quantos \033[41mKENT VERMELHO MAÇO\033[m restaram?: '))
kentvermboxs = int(input('Digite quantos \033[1;41mKENT VERMELHO BOX\033[m restaram?: '))
kentazulmacos = int(input('Digite quantos \033[44mKENT AZUL MAÇO\033[m restaram?: '))
kentazulboxs = int(input('Digite quantos \033[1;44mKENT AZUL BOX\033[m restaram?: '))
carltons = int(input('Digite quantos \033[7;41mCARLTON\033[m restaram?: '))
rothazuls = int(input('Digite quantos \033[44mROTHMANS AZUL\033[m restaram?: '))
rothverms = int(input('Digite quantos \033[41mROTHMANS VERMELHO\033[m restaram?: '))
rothpratas = int(input('Digite quantos \033[47;30mROTHMANS PRATA\033[m restaram?: '))
lustazuls = int(input('Digite quantos \033[44mLUCKY STRIKE AZUL\033[m restaram?: '))
lustdbs = int(input('Digite quantos \033[7mLUCKY STRIKE \033[m\033[30;44mDOUBLE\033[m\033[42;30mCLICK\033[m restaram?: '))
ritzs = int(input('Digite quantos \033[7mRITZ\033[m restaram?: '))
plazacs = int(input('Digite quantos \033[7mPLAZA CURTO\033[m restaram?: '))
plazals = int(input('Digite quantos \033[7mPLAZA LONGO\033[m restaram?: '))
luxors = int(input('Digite quantos \033[43;30mLUXOR\033[m restaram?: '))
chestazuls = int(input('Digite quantos \033[44mCHESTERFIELD AZUL\033[m restaram?: '))
chestverms = int(input('Digite quantos \033[41mCHESTERFIELD VERMELHO\033[m restaram?: '))
malbbverms = int(input('Digite quantos \033[1;41mMALBORO BOX VERMELHO\033[m restaram?: '))
malbbgs = int(input('Digite quantos \033[1;30;43mMALBORO BOX GOLD\033[m\033[1;30;43mMALBORO BOX GOLD\033[m restaram?: '))


#Aqui nós iremos mostrar o resultado

vend = derbyazul - derbyazuls
vend1 = derbyverm - derbyverms
vend2 = derbyprata - derbypratas
vend3 = hollazul - hollazuls
vend4 = hollverm - hollverms
vend5 = hollmenta - hollmentas
vend6 = kentvermmaco - kentvermmacos
vend7 = kentvermbox - kentvermboxs
vend8 = kentazulmaco - kentazulmacos
vend9 = kentazulbox - kentazulboxs
vend10 = carlton - carltons
vend11 = rothazul - rothazuls
vend12 = rothverm - rothverms
vend13 = rothprata - rothpratas
vend14 = lustazul - lustazuls
vend15 = lustdb - lustdbs
vend16 = ritz - ritzs
vend17 = plazac - plazacs
vend18 = plazal - plazals
vend19 = luxor - luxors
vend20 = chestazul - chestazuls
vend21 = chestverm - chestverms
vend22 = malbbverm - malbbverms
vend23 = malbbg - malbbgs


#Agora vem o total de vendidos que é o valor do cigarro * a quantidade vendida
tot = vend * 6.75
tot1 = vend1 * 6.75
tot2 = 6.75 * vend2
tot3 = 7.25 * vend3
tot4 = 7.25 * vend4
tot5 = 7.25 * vend5
tot6 = 8 * vend6
tot7 = 8.25 * vend7
tot8 = 8 * vend8
tot9 = 8.25 * vend9
tot10 = 8.75 * vend10
tot11 = 5.25 * vend11
tot12 = 5.25 * vend12
tot13 = 5.25 * vend13
tot14 = 7.25 * vend14
tot15 = 7.75 * vend15
tot16 = 6.75 * vend16
tot17 = 6.75 * vend17
tot18 = 6.75 * vend18
tot19 = 6.75 * vend19
tot20 = 5.25 * vend20
tot21 = 5.25 * vend21
tot22 = 8.75 * vend22
tot23 = 8.75 * vend23

# resultado total de venda
totg = tot + tot1 + tot2 + tot3 + tot4 + tot5 + tot6 + tot7 + tot8 + tot9 + tot10 + tot11 + tot12 + tot13 + tot14 + tot15 + tot16 + tot17 + tot18 + tot19 + tot20 + tot21 + tot22 + tot23
# Aqui eu mostro o resultado total
print('\n'*100)
print('\033[7m{:^55}| ESTOQUE | ENTRADA | TOTAL | RESTANTE | VENDIDOS | TOTAL R$|'.format(' '))
print('\033[4m{:^55}|{:^9}|         |{:^7}|{:^10}|{:^10}|{:^9.2f}|'.format('\033[44mDERBY AZUL\033[m', derbyazul, derbyazul, derbyazuls, vend, tot))
print('{:^55}|{:^9}|         |{:^7}|{:^10}|{:^10}|{:^9.2f}|'.format('\033[41mDERBY VERMELHO\033[m',derbyverm, derbyverm, derbyverms, vend1, tot1))
print('{:55}|{:^9}|         |{:^7}|{:^10}|{:^10}|{:^9.2f}|'.format('\033[47;30mDERBY PRATA\033[m',derbyprata, derbyprata,derbypratas, vend2, tot2)) 
print('{:^55}|{:^9}|         |{:^7}|{:^10}|{:^10}|{:^9.2f}|'.format('\033[44mHOLLYWOOD VERMELHO\033[m',hollverm, hollverm, hollverms,vend3, tot3))
print('{:^55}|{:^9}|         |{:^7}|{:^10}|{:^10}|{:^9.2f}|'.format('\033[44mHOLLYWOOD AZUL\033[m',hollazul, hollazul, hollazuls, vend4, tot4)) 
print('{:^55}|{:^9}|         |{:^7}|{:^10}|{:^10}|{:^9.2f}|'.format('\033[42;30mHOLLYWOOD MENTA\033[m',hollmenta, hollmenta, hollmentas, vend5, tot5)) 
print('{:^55}|{:^9}|         |{:^7}|{:^10}|{:^10}|{:^9.2f}|'.format('\033[41mKENT VERMELHO MAÇO\033[m',kentvermmaco, kentvermmaco, kentvermmacos, vend6, tot6))
print('{:^55}|{:^9}|         |{:^7}|{:^10}|{:^10}|{:^9.2f}|'.format('\033[44mKENT AZUL MAÇO\033[m',kentazulmaco, kentazulmaco, kentazulmacos, vend8, tot8)) 
print('{:^55}|{:^9}|         |{:^7}|{:^10}|{:^10}|{:^9.2f}|'.format('\033[1;44mKENT AZUL BOX\033[m',kentazulbox, kentazulbox, kentazulboxs, vend9, tot9))
print('{:^55}|{:^9}|         |{:^7}|{:^10}|{:^10}|{:^9.2f}|'.format('\033[7;41mCARLTON\033[m',carlton, carlton, carltons, vend10, tot10))
print('{:^55}|{:^9}|         |{:^7}|{:^10}|{:^10}|{:^9.2f}|'.format('\033[44mROTHMANS AZUL\033[m',rothazul, rothazul, rothazuls, vend11, tot11))
print('{:^55}|{:^9}|         |{:^7}|{:^10}|{:^10}|{:^9.2f}|'.format('\033[41mROTHMANS VERMELHO\033[m',rothverm, rothverm, rothverms, vend12, tot12))
print('{:^55}|{:^9}|         |{:^7}|{:^10}|{:^10}|{:^9.2f}|'.format('\033[47;30mROTHMANS PRATA\033[m',rothprata, rothprata, rothpratas, vend13, tot13))
print('{:^55}|{:^9}|         |{:^7}|{:^10}|{:^10}|{:^9.2f}|'.format('\033[44mLUCKY STRIKE AZUL\033[m',lustazul, lustazul, lustazuls, vend14, tot14))
print('{:^55}|{:^9}|         |{:^7}|{:^10}|{:^10}|{:^9.2f}|'.format('\033[7mLUCKY STRIKE \033[m\033[30;44mDOUBLE\033[m\033[42;30mCLICK\033[m',lustdb, lustdb, lustdbs, vend15, tot15))
print('{:^55}|{:^9}|         |{:^7}|{:^10}|{:^10}|{:^9.2f}|'.format('\033[7mRITZ\033[m',ritz, ritz, ritzs, vend16, tot16))
print('{:^55}|{:^9}|         |{:^7}|{:^10}|{:^10}|{:^9.2f}|'.format('\033[7mPLAZA CURTO\033[m',plazac, plazac, plazacs, vend17, tot17))
print('{:^55}|{:^9}|         |{:^7}|{:^10}|{:^10}|{:^9.2f}|'.format('\033[7mPLAZA LONGO\033[m',plazal, plazal, plazals, vend18, tot18))
print('{:^55}|{:^9}|         |{:^7}|{:^10}|{:^10}|{:^9.2f}|'.format('\033[43;30mLUXOR\033[m',luxor, luxor, luxors, vend19, tot19))
print('{:^55}|{:^9}|         |{:^7}|{:^10}|{:^10}|{:^9.2f}|'.format('\033[44mCHESTERFIELD AZUL\033[m',chestazul, chestazul, chestazuls, vend20, tot20))
print('{:^55}|{:^9}|         |{:^7}|{:^10}|{:^10}|{:^9.2f}|'.format('\033[41mCHESTERFIELD VERMELHO\033[m',chestverm, chestverm, chestverms,vend21, tot21))
print('{:^55}|{:^9}|         |{:^7}|{:^10}|{:^10}|{:^9.2f}|'.format('\033[1;41mMALBORO BOX VERMELHO\033[m',malbbverm, malbbverm, malbbverms, vend22,tot22))
print('{:^55}|{:^9}|         |{:^7}|{:^10}|{:^10}|{:^9.2f}|'.format('\033[1;30;43mMALBORO BOX GOLD\033[m',malbbg, malbbg, malbbgs, vend23, tot23))
print()
print('TOTAL GERAL: R$ {:.2f}\033[m'.format(totg))
print()
