#checks if given array is sorted
def isArraySorted(array):
    #base case if array is of len 1 it is sorted
    if len(array) == 1:                         #if array converges till last element
        return True
    
    else:
        return array[0]<=array[1] and isArraySorted(array[1:])          #check a[0]<=a[1]   and send a[1:] to func()
                                                                    #eg: [12,13,15,17]    and   send [13,15,17] to func()
                                                                    #       True          and   recurrsion     

array = [12,13,15,17,176,245]
print(isArraySorted(array))
#len = 6 False
#12<=13 True and func([13:245])
#len = 5 False
#13<=15 True and func([15:245])
#len = 4 False
#15<=17 True and func([17:245])
#len = 3 False
#17<=176 True and func([176:245])
#len = 2 False
#176<=245 True and func([245]) True as len = 1
#Return True