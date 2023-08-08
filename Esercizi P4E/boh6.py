frase = 'ladro'


index = 4
while index >= 0:
    print(frase[index])
    index = index - 1

for char in frase:
    print(char)

print(frase[0:6])
print(frase[:6])
print(frase[0:])
print(frase[6:6])

n_frase = frase[:4] + 'i'
print(n_frase)

def conta_lettere(frase,lettera):
    try:
        conta = 0
        for char in str(frase):
            if char == str(lettera):
                conta = conta + 1
        print(conta)
    except:
        print('I accept only strings')

conta_lettere('mocc a sort','o')

conta_lettere([5,6,7],7)

print('o' in frase)

frase1 = 'Testa'

print(frase1 > frase)
print(dir(frase))

print(help(str.capitalize))
print(help(str.format))


print(frase.upper())
print(frase.capitalize())
print(frase.lower().startswith('l'))

prova = '     Non è vero     '

print(prova.strip())
frase2 = 'tavola'
print(frase2.count('a'))

data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
21
sppos = data.find(' ',atpos)
print(sppos)
31
host = data[atpos+1:sppos]
print(host)

print('I have %d brothers, Im %g times angry and I feel like an %s.' % (3,1.5,'idiot'))

frase = '1  +  1'
print(frase.split(" "))

data = open('/Users/gianluca/Downloads/mbox.txt')
print(data)

data_short = open('/Users/gianluca/Downloads/mbox-short.txt')
print(data_short)

conta = 0
for line in data_short:
    conta = conta + 1
print('Total lines:', conta)

conta = 0
for line in data:
    conta = conta + 1
print('Total lines:', conta)

data = open('/Users/gianluca/Downloads/mbox.txt')
inp = data.read()
print(len(inp))
print(inp[:100])

data_short = open('/Users/gianluca/Downloads/mbox-short.txt')
for line in data_short:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

data_short = open('/Users/gianluca/Downloads/mbox-short.txt')
for line in data_short:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)

data_short = open('/Users/gianluca/Downloads/mbox-short.txt')
for line in data_short:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1:
        continue
    print(line)


name = input('Enter a file name:')
try:
    fhand = open(name)
except:
    print('File cannot be opened:', name)
    exit()
conta = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('Subject:'):
        conta = conta + 1
print('Totale:', conta)



