nome = input('Nome Completo: ')

def gerar_nome_completo(nome):
    print(f'Bem vindo(a) {nome}')

gerar_nome_completo(nome)



valor = int(input('Valor do produto: '))
numero = int(input('Quantidade: '))


def calcular_valores(produto, quantidade=1):
    print(f'{produto*quantidade}')

    
    
calcular_valores(valor,numero)


