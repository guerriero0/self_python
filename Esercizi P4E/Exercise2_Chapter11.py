import re

try:
    x = '/Users/gianluca/Desktop/Python/mbox-short.txt'
    fx = open(x)
except FileNotFoundError:
    print('File cannot be opened')

conta = 0
somma = 0
for line in fx:
    line.rstrip()
    x = re.findall(".*New Revision: ([0-9]+)",line)
    if len(x) > 0:
        for numero in x:
            numero = int(numero)
            conta += 1
            somma += numero
media = somma/conta
print(f'{media:.1f}')

