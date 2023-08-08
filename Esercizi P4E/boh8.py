lista = ['boh','a','c','d','e','f']

print('c' in lista)

def chop(x):
    del x[0]
    del x[-1]
    return None


def middle(x):
    x = x[1:-1]
    return print(x)

middle(lista)

print(lista.sort())
print(lista)

x = input('Enter: ')
print(x.isnumeric())
