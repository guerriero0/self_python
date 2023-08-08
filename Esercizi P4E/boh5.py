x = 100
while x > 10:
    print('OK')
    x = x - 20
print('Vabbe')

while True:
    frase = input('Scrivi. ')
    if frase.startswith('e') or frase.startswith('E'):
        break
    print(frase)
print('Fatto!')

while True:
    frase = input('Scrivi. ')
    if frase[0] == 'e' or 'E':
        break
    print(frase)
print('Fatto!')

while True:
    frase = input('Scrivi. ')
    if frase[0] == 'a':
        continue
    if frase[0] == 'e' or 'E':
        break
    print(frase)
print('Fatto!')



