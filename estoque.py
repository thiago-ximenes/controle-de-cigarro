import json

def getEstoque() :
    with open('estoque.json','r') as file:
            data = json.load(file)
    return data

def printEstoque(data) :
    print('| NOME DO PRODUTO |'.ljust(25)  + '| QUANTIDADE |'.center(20) +'| PREÇO R$ |'.rjust(20) + '\n')
    for i in data :
        print(i.ljust(25) +  str(data[i]['qtd']).center(20) +  str(data[i]['preco']).rjust(15))

def updateEstoque(data):
    lista = getEstoque()
    
    with open('bk_' + 'estoque.json', 'w') as file:
        json.dump(lista,file)
    
    with open('estoque.json', 'w') as file:
        json.dump(data,file)


