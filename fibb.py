file = open(input(),"r")

def getnum(x):  
    ''' get file name from user '''
    num = x.read()
    x.close()
    return int(num)

def fibonacci(n):               
    ''' find the fibonacci by recursion '''
    if n == 1 :
        return 1
    elif n == 0:
        return 0
    else :
        return fibonacci(n-1) + fibonacci(n-2)

def show(n,fn):                                  # output the sollution
    print("Fibonacci(%s) = "%(n)+str(fn))

file2 = open("result.txt","w")

def saveFile(y):               #  write output to the another file
    y.write(str(fn))
    y.close()
    

n = getnum(file)
if n >= 0 and n <= 20:
    fn = fibonacci(n)
    show(n,fn)
    saveFile(file2)

else:                                       # for unnecessary inputs     
    print("Invalid input.")
    
    

file = open(input(),"r")

def getnum(x):  
    ''' get file name from user '''
    num = x.read()
    x.close()
    return int(num)

def fibonacci(n):               
    ''' find the fibonacci by recursion '''
    if n == 1 :
        return 1
    elif n == 0:
        return 0
    else :
        return fibonacci(n-1) + fibonacci(n-2)

def show(n,fn):                                  # output the sollution
    print("Fibonacci(%s) = "%(n)+str(fn))

file2 = open("result.txt","w")

def saveFile(y):               #  write output to the another file
    y.write(str(fn))
    y.close()
    

n = getnum(file)
if n >= 0 and n <= 20:
    fn = fibonacci(n)
    show(n,fn)
    saveFile(file2)

else:                                       # for unnecessary inputs     
    print("Invalid input.")
    
    

