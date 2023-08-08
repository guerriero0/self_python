new_data = open('boh.txt', 'w')
print(new_data)
line1 = 'Vaffanculo coglione'
print(new_data.write(line1))
line2 = 'Ok coglione'
print(new_data.write(line2))

new_data.close()

lista = [2,6,7]
print(sum(lista))
print(lista[1])
lista[1] = 10
print(lista)

print(lista[-1])
print(7 in lista)

for i in range(len(lista)):
    lista[i] = lista[i] * 2
print(lista)

lista1 = [5,8,12]
print(lista + lista1)
print(lista * 4)

lista[0:1] = [100,200]
print(lista)
lista.append(130)
lista.extend(lista1)
print(lista)

lista.sort()
print(lista)

print(lista.pop(4))
print(lista)
del lista[3]

lista.remove(12)
print(lista)

del lista[0:2]
print(lista)



