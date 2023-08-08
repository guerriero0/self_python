try:
    x = input('Enter the file name: ')
    if x == 'na na boo boo':
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
    nada, xd = x.split('/Users/gianluca/Downloads/')
    fx = open(x)
    conta = 0
    for line in fx:
        if line.startswith('Subject:'):
            conta = conta + 1
    print(f'There were {conta} subject lines in %s' % (xd))
except:
    if not x == 'na na boo boo':
        print('File cannot be opened!')







