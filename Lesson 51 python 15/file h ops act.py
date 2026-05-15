print('\n')
nf1 = open('N_F1.txt', 'x')
nf1.close()

import os
print('Checking if m_f exists or not...')

if os.path.exists('m_f.txt'):
    os.remove('m_f.txt')
else:
    print('File does not exist')

m_f = open('m_f.txt', 'w')
m_f.write('Hi i am cat and i am 3')
m_f.close()

os.remove('Codingal.txt')

os.rmdir('nf')

print('\n')
print('\n')
print('\n')

with open('Codingal.txt', 'w') as file:
    file.write('Hi i am cat and i am 3')
file.close()

with open('Codingal.txt', 'r') as file:
    data = file.readlines()
    print('words in this file r...')
    for line in data:
        word = line.split()
        print (word)
    file.close()

print('\n')
print('\n')
print('\n')

with open('Codingal.txt') as fp:
    d1 = fp.read()

with open('CodingalU.txt') as fp:
    d2 = fp.read()

d1 += '\n'
d1 += d2

print('Merging files...')
with open('Mfile.txt', 'w') as fp:
    fp.write(d1)

file.close

print('\n')
print('\n')
print('\n')

of = open('UpdatedFile.txt', 'w')

isf = open('repeated file.txt', 'r')
    
lssf = set()
print('Eliminatings duplicates..')

for line in isf:
    if line not in lssf:
        of.write(line)
        lssf.add(line)

isf.close()
of.close()
    