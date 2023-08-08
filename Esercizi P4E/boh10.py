try:
    a = (5,6,78,0)
    a[0] = 10
    print(a)
except TypeError:
    print('ERROR: TUPLES ARE IMMUTABLE')

try:
    a = (5,6,78,0)
    a = (10,) + a[1:]
    print(a)
except:
    print('ERROR: TUPLES ARE IMMUTABLE')

frase = 'La banca è fallita'
l = tuple(frase.split())
print(l)

txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
for word in words:
    t.append((len(word), word))
t.sort(reverse=True)
print(t)

res = list()
for length, word in t:
    res.append(word)
print(res)

mail = 'gianlucaguerriero98@gmail.com'
name, dominio = mail.split('@')
print(name)
print(dominio)

d = {'a':5,'c':10,'b':7}
t = list(d.items())
t.sort()
print(t)

for key,value in t:
    print(key,value)

e = {'a':20,'c':30,'b':5}
lista =list()
for key,val in e.items():
    lista.append((val,key))
    lista.sort(reverse=True)
    print(lista)

for val,key in lista:
    print(val,key)

e['Gianluca','Guerriero'] = (3892422173,25)
print(e)

list_of_ints_in_strings = ['42', '65', '12']
list_of_ints = [ int(x) for x in list_of_ints_in_strings ]
print(sum(list_of_ints))