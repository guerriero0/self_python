import re

try:
    x = '/Users/gianluca/Desktop/Python/mbox.txt'
    fx = open(x)
except FileNotFoundError:
    print('File cannot be opened')

conta = 0
for line in fx:
    line = line.rstrip()
    if re.search("^Received:.*",line):
        conta = conta + 1
print(f"mbox.txt had {conta} lines that matched ^Received:.*")

