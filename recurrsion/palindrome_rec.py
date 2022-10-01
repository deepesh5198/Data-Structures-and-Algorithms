#Misc. Palindrome with recurrsion

def rec_palindrome(text,s,e):
    if (e-s == 1) or (s==e):
        return True

    elif text[s] == text[e]:
        return rec_palindrome(text, s+1, e - 1)
    else:
        return False

text = input("Enter the word: ")
l = len(text)
if rec_palindrome(text.lower(), s=0, e= l-1):
    print("Yes")

else:
    print("No")    