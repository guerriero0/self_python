diz = dict()
try:
    fx = open(input('Enter a file name: '))
except FileNotFoundError:
    print('File cannot be opened', fx)
    exit()

for line in fx:
    line = line.rstrip()
    words = line.split(" ")
    if words[0] != "From:":
        continue
    else:
        words.sort()
        if words[1] not in diz:
            diz[words[1]] = 1
        else:
            diz[words[1]] += 1

print(diz)

def massimo(valori):
    largest = None
    for valore in valori:
        if largest is None or largest < valore:
            largest = valore
    return largest

print(massimo(diz),massimo(diz.values()))
print(max(diz), max(diz.values()))

# /Users/gianluca/Desktop/Python/mbox-short.txt
# /Users/gianluca/Desktop/Python/mbox.txt