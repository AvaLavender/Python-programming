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
    