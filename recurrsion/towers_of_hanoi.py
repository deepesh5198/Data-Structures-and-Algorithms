#Towers of hanoi
"""Algorithm:
step1. move (n-1) rings From Source rod to Auxiliary rod
step2. move nth ring from Source rod to Destination rod
step3. move the (n-1) rings from Auxiliary rod to Destination rod
"""

def towersOfHanoi(n, s, a , d):
    if n == 1:
        print("disk{0}:{1}-->{2}".format(n,s,d))
        return
    else:
        towersOfHanoi(n-1, s, d, a)
        print("disk{0}:{1}-->{2}".format(n,s,d))
        towersOfHanoi(n-1, a, s, d)
        # count+=1

towersOfHanoi(4, "A", "B", "C")