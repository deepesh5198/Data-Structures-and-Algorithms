#Towers of hanoi
"""Algorithm:
step1. move (n-1) rings From Source rod to Auxiliary rod
step2. move nth ring from Source rod to Destination rod
step3. move the (n-1) rings from Auxiliary rod to Destination rod
"""

def towersOfHanoi(n, source, destination, auxiliary):
    if n == 1:
        print("move disk {0} from source {1} to destination {2} rod".format(n,source,destination))
        return
    else:
        towersOfHanoi(n-1, source, auxiliary, destination)
        print("move disk {0} from source {1} to destination {2} rod".format(n,source,destination))
        towersOfHanoi(n-1, auxiliary, destination, source)
        # count+=1

towersOfHanoi(4, "A", "B", "C")