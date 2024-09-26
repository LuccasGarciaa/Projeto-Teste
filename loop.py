# LOOP FOR
for numero in range(18, 111):
    print(f'Estamos em {numero}')

for passo in range(1, 11):
  print(f'Realizando passo {passo}')


celulares = ['Asus', 'Samsung', 'Sony', 'IPhone']
versoes = ['Plus', 'Premium Plus', 'Premium Deluxe', 'Plus Premium Ultra']

for celular in celulares:
    for versao in versoes:
        print(f'Celular {celular} Modelo {versao}')

#LOOP WHILE
#Contagem crescente
contagem = 0
while contagem <= 120:
    print(contagem)
    contagem += 1

#Senha
senha = ''
while senha != 'secreto':
    senha = input('Digite sua senha: ')
print('Desbloqueado')

#Contagem Descrescente
contagem = 100
while contagem >= 0:
    print(contagem)
    contagem -= 1