#problem4. Generate all the strings of length n drawn from 0 to k-1

def range_to_list(k):
    result = []
    for i in range(k):
        result.append(str(i))

    return result

def baseKstrings(n,k):
    if n==0:
        return []
    
    elif n == 1:
        return range_to_list(k)

    else:
        return [i+j for i in baseKstrings(1,k) for j in baseKstrings(n-1,k)]


print(baseKstrings(3,2))