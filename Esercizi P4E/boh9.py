diz = {}
x = open('/Users/gianluca/Desktop/Python/words.txt')
j = 0
for row in x:
    for parola in row.rstrip().split():
        j = j + 1
        diz[parola] = j
print(diz)

# Contare i caratteri di una stringa o gli elementi di una lista
## metodo senza get
frase = 'quadrato'
d = dict()
for i in frase:
    if i not in d:
        d[i] = 1
    else:
        d[i] = d[i] + 1
print(d)

## metodo con get
frase = 'quadrato'
d = dict()
for i in frase:
    d[i] = d.get(i,0) + 1
print(d)

counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    if counts[key] > 10 :
        print(key, counts[key])

'''

x = input('Enter a file: ')
fx = open(x)
d = dict()
for row in fx:
    words = row.rstrip().split(",")
    for i in words:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
print(d)
'''

import string
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)




