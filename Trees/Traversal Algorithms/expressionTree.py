from turtle import left, right


op_precedence = {"(":0,")":0,"+":1,"-":1,"*":2,"/":2}

def postfix_convert(infix):
    stack = []
    postfix = []

    for char in infix:
        if char not in op_precedence:
            postfix.append(char)
        else:
            if len(stack) == 0:
                stack.append(char)

            else:
                if char == "(":
                    stack.append(char)

                elif char == ")":
                    while stack[len(stack)-1] != "(":
                        postfix.append(stack.pop()) 

                    stack.pop()

                elif op_precedence[char] > op_precedence[stack[len(stack)-1]]:
                    stack.append(char)

                else:
                    while len(stack) != 0:
                        if stack[len(stack)-1] == "(":
                            break
                        postfix.append(stack.pop())
                    stack.append(char)

    while len(stack)!=0:
        postfix.append(stack.pop())

    return postfix



class Node:
    def __init__(self, data):
        self.data = data
        self.left = left
        self.right = right

class ExpressionTree:
    def __init__(self, root = None):
        self.__root = root

    def inorder(self):
        self.__inorderRec(self.__root)

    def __inorderRec(self, node):
        if node:
            self.__inorderRec(node.left)
            print(node.data)
            self.__inorderRec(node.right)

    def preorder(self):
        self.__preorderRec(self.__root)

    def __preorderRec(self, node):
        if node:
            print(node.data)
            self.__preorderRec(node.left)
            self.__preorderRec(node.right)
            

    def postorder(self):
        self.__postorderRec(self.__root)

    def __postorderRec(self, node):
        if node:
            self.__postorderRec(node.left)
            self.__postorderRec(node.right)
            print(node.data)



def buildExpTree(infix):
    postfix = postfix_convert(infix)
    stack = []
    for char in postfix:
        if char not in op_precedence:
            node = Node(char)
            stack.append(node)

        else:
            node = Node(char)
            node.right = stack.pop()
            node.left = stack.pop()
            stack.append(node)

    return ExpressionTree(stack.pop())


print("In Order")
buildExpTree("(5+3)*2").inorder()