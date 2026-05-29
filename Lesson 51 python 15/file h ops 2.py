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

  