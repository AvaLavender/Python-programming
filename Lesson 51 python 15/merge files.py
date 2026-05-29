with open('Codingal.txt') as fp:
    d1 = fp.read()

with open('CodingalU.txt') as fp:
    d2 = fp.read()

d1 += '\n'
d1 += d2

print('Merging files...')
with open('Mfile.txt', 'w') as fp:
    fp.write(d1)