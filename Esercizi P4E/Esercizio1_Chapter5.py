def somma(valori):
    sommatoria = 0
    for value in valori:
        sommatoria = sommatoria + value
    return sommatoria

def conteggio(valori):
    conta = 0
    for value in valori:
        conta = conta + 1
    return conta


def media(valori):
    try:
        sommatoria = 0
        for value in valori:
            sommatoria = sommatoria + value
        conta = 0
        for value in valori:
            conta = conta + 1
        x_medio = sommatoria/conta
        return x_medio
    except:
        return print('Fix the error!!')

def info():
    lista = []
    while True:
        try:
            x = input('Enter a number: ')
            lista.append(float(x))
        except:
            if x == 'done':
                break
    return print(somma(lista), conteggio(lista), media(lista),sep=", ")

info()