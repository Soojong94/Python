number = 10
def add(n1,n2) :
    return n1 + n2

def divisor(num, endstr=" ") : 
    for i in range (1,num+1, 1) :
        if num % i == 0 :
            print(i, end=endstr)
            