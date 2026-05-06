class Expression:

   def __init__(self, ques ,ans):
        self.ques = ques
        self.ans = ans

a = Expression ('2x + 2 = 6. Find x', 2 )

print('Your question is: {}'.format( a.ques ))
print('Answer is {}' .format( a.ans ))