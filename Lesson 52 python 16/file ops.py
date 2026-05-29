file_read = open('dog.txt', 'r')
print('File in read mode- ')
print(file_read.read())
file_read.close()

file_write = open('dog.txt' , 'w')
file_write.write('\n File in write mode...')
file_write.write('This is in write mode')
file_write.close()

file_append = open('dog.txt' , 'a')
file_append.write('\n File in append mode...')
file_append.write('File is in append mode')
file_append.close()