try:
    x = input('Enter a file name: ')
    fx = open(x)
except FileNotFoundError:
    print('File cannot be opened!')
    exit()

diz = dict()
for line in fx:
    line.rstrip()
    words = line.split()
    if (len(words) < 3) or words[0] != 'From':
        continue
    else:
        if words[1] not in diz:
            diz[words[1]] = 1
        else:
            diz[words[1]] += 1

lista = list()
for key,val in diz.items():
    lista.append((val,key))
    lista.sort(reverse=True)

for val,key in lista[:1]:
    print(key,val)

print(max(lista))