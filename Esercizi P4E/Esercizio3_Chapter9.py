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


