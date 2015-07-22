#Fib sequence and diff ways to get nth fib, with fib(0) = 1

def fibRecursive(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else: 
        return fibRecursive(n-1) + fibRecursive(n-2)
        
def fibIter(n):
    prevFibSum = 0
    fibSum = 1
    for currNum in xrange(n):
        fibSum, prevFibSum = fibSum + prevFibSum, fibSum
    return fibSum

fibDict = {0: 1, 1: 1}
def fibDynamic(n):
    global fibDict
    if n in fibDict:
        return fibDict[n]
    else:
        fibDict[n] = fibDynamic(n - 1) + fibDynamic(n - 2)
        return fibDict[n]
        
def checkAllEqual(*args):
    if len(args) <= 1:
        return
    for ii in xrange(len(args) - 1):
        assert args[ii] == args[ii + 1]

for n in xrange(10):
    checkAllEqual(fibRecursive(n), fibIter(n), fibDynamic(n))