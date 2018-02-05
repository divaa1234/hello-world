def applyToEach(L, f):
     for i in range(len(L)):
          L[i] = f(L[i])
     return L    
     
testList = [1, -4, 8, -9]

def fun(a):
     return a*5


def makePositive(a):
     count = 0
     for i in testList:
         if i < 0:
             testList[count] = abs(i)
         count += 1
     return a


