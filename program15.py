import re

input1 = input('Enter a file: ')
fh = open(input1)

l = list()

for line in fh:
    y = re.findall('[0-9]+',line)
    l = l + y

sum = 0
for i in l:
    sum = sum + int(i)
print('Sum:', sum)
