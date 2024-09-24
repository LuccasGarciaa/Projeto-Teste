from datetime import datetime

data_aniversario = datetime.strptime(input('Seu Aniversario?'), '%d/%m/%Y')

data_atual = datetime.now()

prazo = data_aniversario - data_atual

print(prazo.days)