# 0123456789


class Node:

    def __init__(self,value):
        self.data = value
        self.next = None


class Queue:

    def __init__(self):
        self.front = None
        self.rear = None
    
    # For Inserting data
    def enqueue(self,value):
        new_node = Node(value)

        if self.rear == None:
            self.front = new_node
            self.rear = self.front
        else:
            self.rear.next = new_node  # type: ignore
            self.rear = new_node

    # For deleting data
    def dequeue(self):
        if self.front == None:
            return "Empty"
        else:
            self.front = self.front.next

    def is_empty(self):
        return self.front == None
    
    def size(self):
        temp = self.front
        counter = 0

        while temp != None:
            counter += 1
            temp = temp.next
        return counter
    
    # For geting front item
    def front_item(self):
        if self.front == None:
            return "Empty"
        else:
            return self.front.data
        
    
    # For geting rear item
    def rear_item(self):
        if self.front == None:
            return "Empty"
        else:
            return self.rear.data
        
    
    # For traversing data
    def traverse(self):
        temp = self.front

        while temp != None:
            print(temp.data,end=' ')
            temp = temp.next

q = Queue()


q.enqueue(7)
q.enqueue(8)
q.enqueue(9)
q.enqueue(78)
q.dequeue()
print(q.size())
print(q.front_item())
print(q.rear_item())

q.traverse()





# Watching vedio length 07.33min