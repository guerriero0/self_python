fx = open('/Users/gianluca/Desktop/Python/romeo.txt')
lista = []
for row in fx:
    x = row.rstrip().split()
    for i in x:
        if i in lista:
            continue
        else:
            lista.append(i)
lista.sort()
print(lista)






