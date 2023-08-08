def massimo(valori):
    largest = None
    for valore in valori:
        if largest is None or largest < valore:
            largest = valore
    return largest


def minimo(valori):
    smallest = None
    for valore in valori:
        if smallest is None or smallest > valore:
            smallest = valore
    return smallest

def info_estr():
    lista = []
    while True:
        try:
            x = input('Enter a number: ')
            lista.append(float(x))
        except:
            if x == 'done':
                break
    return print(massimo(lista), minimo(lista),sep=", ")

info_estr()





