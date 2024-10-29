import json
# Imprimir o e-mail do usuário com id 2
with open('teste1.json') as arquivo_json:
    data = json.load(arquivo_json)
    print(data['user'][1]['email'])
# imprimir a city do usuário com id 1
with open('teste1.json') as arquivo_json:
    data = json.load(arquivo_json)
    print(data['user'][0]['address']['city'])
# Imprimir o total do pedido do usuário com id 2
with open('teste1.json') as arquivo_json:
    data = json.load(arquivo_json)
    print(data['user'][1]['orders'][0]['total'])