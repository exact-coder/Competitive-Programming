# 0123456789
class Node:
    
    def __init__(self,value):
        self.data = value
        self.next = None

class Stack:

    def __init__(self) -> None:
        self.top = None
    
    def isempty(self):
        return self.top == None
    
    
    def push(self,value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
    
    def traverse(self):
        temp = self.top

        while temp != None:
            print(temp.data)
            temp = temp.next
    def peek(self):
        if(self.isempty()):
            return "Stack Empty"
        else:
            return self.top.data
        
    def pop(self):
        if(self.isempty()):
            return "Stack Empty"
        else:
            data = self.top.data
            self.top = self.top.next
            return data

S = Stack()

# S.push(5)
# S.push(10)
# S.push(20)
# S.push(30)
# S.push(40)

# print(S.isempty())
# print(S.peek())
# print(S.pop())
# print(S.peek())

# Text editor problem solving by stack
def text_editor(text,pattern):
    u = Stack()
    r = Stack()

    for i in text:
        u.push(i)
    for  i in pattern:
        if i == 'u':
            data = u.pop()
            r.push(data)
        else:
            data = r.pop()
            u.push(data)
    res = ""
    while(not u.isempty()):
        res = u.pop() + res
    print(res)

# result = text_editor("Dhaka","uuurruu")

# Celebrity problem solving using Stack
L = [
    [0,0,1,1],
    [0,0,0,1],
    [0,0,0,0],
    [0,1,0,1]
]
def find_the_celeb(L):
    s = Stack()
    sum = 0
    for i in range(len(L)):
        s.push(i)
        sum += 1
    
    while sum >= 2:

        i = s.pop()
        j = s.pop()
        
        if L[i][j] == 0:
            # j is not a celebrity
            s.push(i)
        else:
            # i is not a celebrity
            s.push(j)
    celeb = s.pop()

    for i in range(len(L)):
        if i != celeb:
            if L[i][celeb] == 0 or L[celeb][i] == 1:
                print("No one is a Celebrity")
                return
    print("The Celebrity is", celeb)

find_the_celeb(L)
# Watching vedio length 06.07min