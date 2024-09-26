#Continue'ignorar, pular' / Break 'parar'

estilos = ['Hip-Hop','Rock','Rap','Pop']

for estilo in estilos:
    if estilo == 'Rap':
        continue
    print(estilo)

for estilo in estilos:
    if estilo == 'Rap':
        break
    print(estilo)