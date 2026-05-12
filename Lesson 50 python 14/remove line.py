f1 = open('Codingal.txt', 'r')

f2 = open('CodingalU.txt', 'w')

for line in f1.readlines():

    if not (line.startswith('Coding')):

        print(line)

        f2.write(line)
f2.close()
f1.close()