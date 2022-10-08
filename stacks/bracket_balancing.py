#stck problem
#bracket balancing: Check if the open bracket is closed

# user_input = input("Type a bracket sequence.")
# from inspect import stck, stck


user_input = "() (()[()])"
print(user_input)
def check_the_input(input):
    stck = []
    for symbol in input:
        if symbol in """"[({'""":
            stck.append(symbol)
        else:
            if symbol in """"]})'""":
                stck.pop()

            else:
                continue

    if len(stck) == 0:
        print("Input is good")

    else:
        print("You forgot to close the {0}".format(stck[-1]))
    print(stck)
check_the_input(user_input)


 




















user_input = input("Enter your string: ")
def check_input(input):
    stack = []
    for char in input:
        if char in """({["'""":
            stack.append(char)
        elif char in """)}]"'""":
            stack.pop()

        else:
            continue

    if len(stack) == 0:
        print("input is good")

    else:
        print("You forgot to close the {}".format(stack[-1]))

check_input(user_input)