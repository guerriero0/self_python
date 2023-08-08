x = input('Enter a file name: ')
xhand = open(x)
for line in xhand:
    print(line.rstrip().upper())
    