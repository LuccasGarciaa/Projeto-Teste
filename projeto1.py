from datetime import datetime
import random

print('----------- Bem-Vindo a nossa empresa -----------')
#Obter nome de usuário
nome = input('Qual seu nome? ')
#Obter a idade do usuário
idade = int(input('Qual sua idade? '))
#Registre de forma automatica a data do cadastro do usuário, usando a data do registro como data de registro
data_registro = datetime.now()

#cada funcionario novo registrado, recebe um cartao sorteado 
'''Cartoes = ['R$50,00' 'R$250,00' 'R$120,00']'''
cartoes = ['R$50,00', 'R$250,00', 'R$120,00']
cartao = random.choice(cartoes)

#Guarde as informações sobre a data de aniversario do funcionario(dd/mm/aaaa)
aniversario = datetime.strptime(
    input('Digite sua data de aniverário no formato dd/mm/aaaa: '), '%d/%m/%Y')


print(f'Olá {nome}, seu registro foi concluído com sucesso no dia {data_registro.day}/{data_registro.month}/{data_registro.year}.\n Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de {cartao}')