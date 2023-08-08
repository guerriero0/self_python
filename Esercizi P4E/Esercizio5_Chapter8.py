x = input('Enter a file name: ')
fx = open(x)
print(fx)
for row in fx:
    if row.startswith('From '):
        y = row.rstrip().split(' ')
        print(y[1])




