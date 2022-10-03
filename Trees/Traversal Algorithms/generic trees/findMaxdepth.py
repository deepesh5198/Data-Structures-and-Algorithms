# to find the max depth of the N-ary tree
#given a parent array for eg. [-1,0,1,6,6,0,0,2,7]
#the root node's parent is always -1
#the elements of parent array are Parents
#index corresponding to parent element of the array is the child of that parent
#for example:   0-> -1, 1-> 0, 2->1, 3->6, 4->6, 5->0, 6->0, 7->2, 8->7
#      -1       
#      [0]
# [1]  [5]    [6]
# [2]       [3] [4]  
# [7]
# [8]                   

def findMaxdepth(P):
    maxdepth = -1
    currentdepth = -1
    for i in range(len(P)):
        currentdepth = 0
        j = i
        while P[j] != -1:
            currentdepth +=1
            j = P[j]

        if currentdepth > maxdepth:
            maxdepth = currentdepth
    return maxdepth

P = [-1,0,1,6,6,0,0,2,7]

print("max depth: ", findMaxdepth(P))