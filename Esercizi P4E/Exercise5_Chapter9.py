diz = dict()
try:
    fx = open(input('Enter a file name: '))
except FileNotFoundError:
    print('File cannot be opened', fx)
    exit()
for line in fx:
    line = line.rstrip()
    words = line.split()
    if len(words) < 2 or words[0] != "From":
        continue
    else:
        atpos = words[1].find("@")
        dominio = words[1][atpos+1:]
        if dominio not in diz:
            diz[dominio] = 1
        else:
            diz[dominio] += 1
print(diz)





