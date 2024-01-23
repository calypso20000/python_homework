#Given a list of numbers, write a function to find the sum of all numbers in the list that can be divided by 7.

class SumOfAllNumbers:

    def __init__(self, numbers=[]):
        self.numbers=numbers

    def summ(self):
            renum=0
            for num in self.numbers:
                 if num%7==0:
                      renum+=num
            return renum
            
s=SumOfAllNumbers()
s.numbers=[1,7,21,28,53]
print(s.summ())
        