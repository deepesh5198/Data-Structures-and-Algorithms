#implementing postfix evaluation  using stack

# user_input = "() (()[()])"
user_input = input("Write the problem here: ")
print(user_input)
def evaluate_postfix(input):
    if len(input) <= 1:
        print(input)
    stack = []
    for char in input:
        if char in """0123456789""":
            stack.append(char)
        else:
            if char in """+-*/""":
                b = stack[-1]
                stack.pop()
                a = stack[-1]
                stack.pop()
                
                stack.append(solveit(a,b,char))
                print(stack)

            else:
                continue

def solveit(op1,op2,op):
    if op == "+":
        return int(op1)+int(op2)
    elif op == "-":
        return int(op1)-int(op2)
    elif op == "*":
        return int(op1)*int(op2)
    elif op == "/":
        return int(op1)/int(op2)
    else:
        print("Invalid Operation!")

evaluate_postfix(user_input)