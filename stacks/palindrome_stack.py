#Check palindrome using stack

user_input = input("Type a string: ")
def checkpalindrome(input):
    stack = []
    palindrome = False

    if len(input) <= 1:
        palindrome = True
    for char in input:
        stack.append(char)
    for char in input:
        if char == stack[-1]:
            stack.pop()
            palindrome = True
        else:
            palindrome = False
            break
    
    if palindrome == True:
        print("Palindrome")
    else:
        print("Not Palindrome")

checkpalindrome(user_input)