file_read = open('cats.txt', 'r')
print('File in read mode')
print(file_read.read())
file_read.close()

file_write = open('cats.txt', 'w')
file_write.write('\n File in write mode...')
file_write.write('Hi i am cat and i am 1')
file_write.close()

file_append = open('cats.txt', 'a')
file_append.write('\n File in append mode...')
file_append.write('Hi i am cat and i am 1')
file_append.close()

