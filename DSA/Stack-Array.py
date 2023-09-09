# 0123456789

class Stack:
    
    def __init__(self,size):
        self.size = size
        self.stack = [None] * self.size
        self.top = -1

    def push(self,value):
        if self.top == self.size - 1:
            return "Overflow"
        else:
            self.top += 1
            self.stack[self.top] = value
    def pop(self):
        if self.top == -1:
            return "Empty"
        else:
            data = self.stack[self.top]
            self.top -=1
            return data
    def traverse(self):

        for i in range(self.top + 1):
            print(self.stack[i],end=' ')

s = Stack(3)
s.push(7)
s.push(6)
s.push(76)

print(s.stack)

print(s.pop())
print(s.pop())
print(s.traverse())


# Watching vedio length 06.20min