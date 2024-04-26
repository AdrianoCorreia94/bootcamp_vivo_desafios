# praticando conceitos basicos de datas

from datetime import date, datetime, timedelta


def menu():
    print("escolha uma opcao \
          1 - fazer nova reserva\
          2 - ver agenda\
          3 - sair")


def minha_funcao(carro, porte):
    global ultimo_horario_livre
    chegada = ultimo_horario_livre
    if porte.lower() == 'm':
        tempo = 45

    elif porte.lower() == 'p':
        tempo = 30

    elif porte.lower() == 'g':
        tempo = 60

    else:
        print('Porte invalido')

    # armazenar entrada para proxima reserva
    ultimo_horario_livre += timedelta(minutes=tempo)
    reservando = {'porte': porte,
                  'chegada': f'{chegada}',
                  'saída': f'{ultimo_horario_livre}'}

    reservas[carro] = reservando


ultimo_horario_livre = datetime.now()
reservas = {}

while True:
    menu()
    op = str(input('> '))
    if op == '1':
        minha_funcao(input('carro: '), input('porte'))
    elif op == '2':
        for x, y in reservas.items():
            print(x, y)
    elif op == '3':
        break
    else:
        print('digite uma opcao valida')