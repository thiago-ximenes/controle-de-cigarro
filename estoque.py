import json
import os


def clear():
    return os.system('cls' if os.name == 'nt' else 'clear')


def getEstoque() :
	with open('estoque.json','r') as file:
			data = json.load(file)
	return data


def printEstoque(data) :
	print('| NOME DO PRODUTO |'.ljust(25)  + '| ESTOQUE |'.center(20) +'| PREÇO R$ |'.rjust(20) + '\n')
	for i in data :
		print(f'{i:<25}{data[i]["qtd"]:^20}{str(moeda(data[i]["preco"])):>20}')

def updateEstoque(data):
	lista = getEstoque()
	
	with open('bk_' + 'estoque.json', 'w') as file:
		json.dump(lista,file)
	
	with open('estoque.json', 'w') as file:
		json.dump(data,file)


def moeda(valor):
	s = f'R$ {valor:.2f}'.replace('.', ',')
	return s
	

def atualizeEstoque(est):
	for k, v in est.items():
		while True:	
			print('=-=-=- ATUALIZANDO ESTOQUE -=-=-=')
			v['qtd'] = str(input(f'{k} ESTOQUE (aperte enter para "0"): ')).strip()
			if v['qtd'].isalpha():
				print(f'\033[31mValor {v["qtd"]} inválido, por favor entre com um valor inteiro válido\033[m')
			elif v['qtd'] == '':
				v['qtd'] = int(0)
				break
			else:
				v['qtd'] = int(v['qtd'])
				break
		clear()
			
		
		
