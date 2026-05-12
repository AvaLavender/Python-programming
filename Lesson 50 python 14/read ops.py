file = open('cats.txt', 'r')
print(file.read())
file.close()

file = open('cats.txt', 'r')
print('\n Read in parts \n')
print(file.read(8))
file.close

file = open('cats.txt', 'a')
file.write('Hi i am a cat and i am 3')
file.close