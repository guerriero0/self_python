'''

x = input('Enter a file name: ')
fx = open(x)
diz = dict()
for row in fx:
    if row.startswith("From"):
        row = row.rstrip()
        row = row.split()
        for word in row:
            if word in ("Mon","Tue","Wed","Thu","Fri","Sat","Sun"):
                if word not in diz:
                    diz[word] = 1
                else:
                    diz[word] += 1
print(diz)

'''

diz = {}
x = input('Enter a file name: ')
fx = open(x)
for line in fx:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    else:
        if words[2] not in diz:
            diz[words[2]] = 1
        else:
            diz[words[2]] += 1

print(diz)

'''
dictionary_days = dict()                       # Initializes the dictionary
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    else:
        if words[2] not in dictionary_days:
            dictionary_days[words[2]] = 1       # First entry
        else:
            dictionary_days[words[2]] += 1      # Additional counts

print(dictionary_days)
'''









