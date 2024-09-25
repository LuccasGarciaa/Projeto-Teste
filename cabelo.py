cabelo = 35

if cabelo <= 20:
    print('Valor R$ 50,00')
elif cabelo >= 21 and cabelo <= 30:
    print('Valor R$ 70,00')
elif cabelo >= 31 and cabelo <= 50:
    print('Valor R$ 100,00')
else:
    print('Favor consultar a recepção')

#Inteiro
Velocidade = int(input('Sua Velocidade? '))
print('Você foi multado') if Velocidade > 100 else  print('Seguir em Frente')


#Booleano
Velocidade_carro = False
print('seguir em frente') if Velocidade_carro else print('Foi Multado')