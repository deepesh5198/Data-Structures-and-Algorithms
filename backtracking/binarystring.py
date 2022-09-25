# generate all binary strings with n bits assume A = [0,.., n-1] is an array of size n

def bitsrtrings(n):
    if n == 0:
        return []
    elif n == 1:
        return ['0','1']
    else:
        b = []
       
        for i in bitsrtrings(n-1):
            for j in bitsrtrings(1):
                 b.append(i+j)
        return b
        
        # return [digit + bitstring for digit in bitsrtrings(1) for bitstring in bitsrtrings(n-1)]
print(bitsrtrings(3))