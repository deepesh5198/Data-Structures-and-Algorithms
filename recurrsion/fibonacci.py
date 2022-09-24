def Fibo(n):
    if n == 0:              #first base case
        return 0

    elif n == 1:            #second base case
        return 1

    else:
        return Fibo(n-2) + Fibo(n-1)        #recursion step using the two base cases

for i in range(1, 14): 
    print(Fibo(i))          #print 1st 13 fibonacci numbers
