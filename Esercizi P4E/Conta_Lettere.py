import string
import re

try:
    x = input('Enter a file name: ')
    fx = open(x)
except FileNotFoundError:
    print('File cannot be opened')
    exit()


def clean(text):
    pattern = r"\b(?=[MDCLXVIΙ])M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})([IΙ]X|[IΙ]V|V?[IΙ]{0,3})\b\.?"
    return re.sub(pattern, '&', text)
def clean1(text):
    pattern1 = r"è"
    return re.sub(pattern1,'&', text)


diz = dict()
for line in fx:
    line = clean(line)
    line = clean1(line)
    line = line.rstrip().translate(line.maketrans("", "", string.punctuation))
    line = line.translate(line.maketrans("", "", string.digits))
    line = line.translate(line.maketrans("", "", string.whitespace)).lower()
    words = line.split(" ")
    for word in words:
        if word != "":
            for letter in word:
                if letter not in diz:
                    diz[letter] = 1
                else:
                    diz[letter] += 1

lista_lettere = list()
lista_lettere_percentuale = list()
for key, val in diz.items():
    lista_lettere.append((val, key))
    lista_lettere.sort(reverse=True)

for val, key in lista_lettere:
    percentuale = round(val/sum(diz.values())*100, 4)
    lista_lettere_percentuale.append((percentuale, key))
    lista_lettere_percentuale.sort(reverse=True)

for val, key in lista_lettere_percentuale:
    print(val, key)
