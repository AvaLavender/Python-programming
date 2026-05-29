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
