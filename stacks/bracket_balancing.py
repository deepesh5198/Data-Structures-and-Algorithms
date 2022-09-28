#stack problem
#bracket balancing: Check if the open bracket is closed

# user_input = input("Type a bracket sequence.")
user_input = "() (()[()])"
print(user_input)
def check_the_input(input):
    stack = []
    for symbol in input:
        if symbol in """"[({'""":
            stack.append(symbol)
        else:
            if symbol in """"]})'""":
                stack.pop()

            else:
                continue

    if len(stack) == 0:
        print("Input is good")

    else:
        print("You forgot to close the {0}".format(stack[-1]))

check_the_input(user_input)

 
