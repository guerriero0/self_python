def minimo(valori):
    smallest = None
    for valore in valori:
        if smallest is None or smallest > valore:
            smallest = valore
    return smallest

def massimo(valori):
    largest = None
    for valore in valori:
        if largest is None or largest < valore:
            largest = valore
    return largest


lista = []
try:
    while True:
        x = input('Enter a number: ')
        if x == 'done': break
        x = float(x)
        lista.append(x)
    print(minimo(lista), massimo(lista))
except:
    print('Error, please enter a number!')







