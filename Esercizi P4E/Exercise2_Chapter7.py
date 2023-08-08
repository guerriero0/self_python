x = input('Enter a file name: ')
fx = open(x)
conta = 0
lista = []
for line in fx:
    if line.startswith('X-DSPAM-Confidence:'):
        conta = conta + 1
        nada, valore = line.strip().split('X-DSPAM-Confidence:')
        valore = float(valore)
        repr(line)
        lista.append(valore)
print(f'La somma dei valori è: {sum(lista):.2f}')
print(f'Totale linee è: {conta:.2f}')
average = sum(lista)/conta
print(f'La media è: {average:.2f}')










