#problem: replace element with nearest greater element on the right
# [1,2,3,4,5] -> [1,2,3,5] -> [1,2,5] -> [1,5] -> [5]

def replace_element(stack):
    if len(stack) == 0:
        return stack

    elif len(stack) == 1:
        return stack

    else:
        top = stack[-1]               #hold the value of last element in TOP
        stack.pop()                   #pop last element
        if stack[-1] < top:           #compare TOP element with "now-top" element
            stack[-1] = top           #if its small replace it with TOP

            replace_element(stack)    #call the function again with changed stack

        else:                         #when "now-top" value greater than the TOP value
            return stack              #return the stack

    return stack

result = replace_element([1,2,3,4,5,10])
print(result)