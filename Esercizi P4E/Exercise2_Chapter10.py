try:
    x = input('Enter a file name: ')
    fx = open(x)
except FileNotFoundError:
    print('File cannot be opened')
    exit()

diz = dict()
for line in fx:
    words = line.strip().split(" ")
    if words[0] != 'From':
        continue
    else:
        hour, minutes, seconds = words[6].split(":")
        if hour not in diz:
            diz[hour] = 1
        else:
            diz[hour] += 1

lista = list()
for key, val in diz.items():
    lista.append((key, val))
    lista.sort()
print(lista)

diz_percentuali = dict()
somma = 0
for key, val in lista:
    somma = somma + val
for key,val in lista:
    percentuale = val/somma
    print('La percentuale è per il mese', key, ':', round(percentuale,2))
    if key not in diz_percentuali:
        diz_percentuali[key] = round(percentuale,2)
    else:
        continue

lista_percentuali = []
for mese,perc in diz_percentuali.items():
    lista_percentuali.append((perc,mese))
    lista_percentuali.sort()

print(max(lista_percentuali))