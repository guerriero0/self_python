try:
    x = '/Users/gianluca/Desktop/Python/mbox-short.txt'
    fx = open(x)
except FileNotFoundError:
    print('File cannot be opened.')

import re
for line in fx:
    line = line.rstrip()
    if re.search('^From:.+za|^From:.+edu', line):
        print(line)



for line in fx:
    line = line.rstrip()
    x = re.findall('\S+@\S+', line)
    if len(x) > 0:
        print(x)

for line in fx:
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
    if len(x) > 0:
        print(x)

for line in fx:
    line = line.rstrip()
    if re.search('^X\S*: [0-9.]+', line):
        print(line)

for line in fx:
    line = line.rstrip()
    x = re.findall('^X\S*: ([0-9.]+)', line)
    if len(x) > 0:
        print(x)

x = '/Users/gianluca/Desktop/Python/mbox-short.txt'
fx = open(x)
for line in fx:
    line = line.rstrip()
    x = re.findall('^From .* ([0-9][0-9]):', line)
    if len(x) > 0: print(x)

# grep '^From:' mbox-short.txt # terminal macos

# help()

print(dir(re))
help(re.search)