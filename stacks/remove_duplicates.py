#Problem: Remove all adjacent duplicates from string
#for eg. MISSISSIPPI

input = "MISSISSIPPI"

def rmv_duplicates(input):
    stack = []
    for char in input:
        if len(stack) == 0:
            stack.append(char)     #push 1st char from str to stack
                                   #top = M

        elif char == stack[-1]:    #is TOP = current char    
            stack.pop()             #remove TOP from stack
        else:
            stack.append(char)      #else append char to stack
    print("".join(stack))

rmv_duplicates(input)