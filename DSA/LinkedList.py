

class Node:

    def __init__(self,value):
        self.data = value
        self.next = None

# a = Node(5)
# b = Node(10)
# c = Node(15)

# print(a.data)
# print(a.next)
# print(id(a))
# print(a) 

class LinkedList:

    def __init__(self):
        
        # Empty Linked List
        self.head = None
        # number of nodes in the LL
        self.n = 0

    def __len__(self):
        return self.n
    
    # FOr Insert data
    def insert_head(self,value):

        # new node
        new_node = Node(value)

        # create connection
        new_node.next = self.head
        # reassign head
        self.head = new_node
        # increment n
        self.n = self.n +1
    
    # For Traversing all data
    def __str__(self):
        curr = self.head

        result = " "

        while curr != None:
            result = result + str(curr.data) + " -> "
            curr = curr.next
        return result[:-3]
    
    # For insert new data in tail or last memory locations
    def append(self,value):
        new_node = Node(value)

        if self.head == None:
            # list is empty
            self.head = new_node
            self.n = self.n + 1
            return

        curr = self.head

        while curr.next != None:
            curr = curr.next

        # at the last node
        curr.next = new_node
        self.n = self.n + 1

    # Inserting data in the point where we want
    def insert_after(self,after,value):
        new_node = Node(value)

        curr = self.head

        while curr != None:
            if curr.data == after:
                break
            curr = curr.next
        # Now there has been tow cases.They are:
        # case 1: get the item and break.
        if curr != None:
            new_node.next = curr.next
            curr.next = new_node
            self.n = self.n + 1
        # case 2: loop ended but item doesn't get.
        else:
            return "Item doesn't Found!!!"
    # Clear the LinkList
    def clear(self):
        self.head = None
        self.n = 0
    # Delete data from the head
    def delete_head(self):
        if self.head != None:
            self.head = self.head.next
            self.n = self.n - 1
        else:
            return "Empty List"
    # Data delete in the last
    def pop(self):
        curr = self.head
        if self.head == None:
            return "Empty LinkedList"

        while curr.next.next != None:
            curr = curr.next

        if curr.next != None:
            curr.next = None
            self.n = self.n - 1
        else:
            self.delete_head()
    # Deleted input data from any random places
    def remove(self,value):
        if self.head == None:
            return "Empty LinkedList"
        
        if self.head.data == value:
            # You want to delete the head node
            self.n = self.n - 1
            return self.delete_head()

        curr = self.head

        while curr.next != None:
            if curr.next.data == value:
                break
            curr = curr.next
        
        # now there is two cases
        # One: item found
        # Two: Item not found
        if curr.next == None:
            return 'Not Found'
        else:
            curr.next = curr.next.next
            self.n = self.n - 1
    # Searching an item from LinkedList
    def search(self,item):
        curr = self.head
        pos = 0

        while curr != None:
            if curr.data == item:
                return pos
            curr = curr.next
            pos = pos + 1
        return "Not Found"
    #  Giving the index number and get the item
    def __getitem__(self,index):
        curr = self.head
        pos = 0

        while curr != None:
            if pos == index:
                return curr.data
            curr = curr.next
            pos = pos + 1
        return 'IndexError'

L = LinkedList()

L.insert_head(5)
L.insert_head(10)
L.insert_head(15)
L.insert_head(20)

# print(len(L))
# L.traverse()
# L.append(55)
# L.insert_after(20,66)
# L.clear()
# L.delete_head()
# L.pop()
# L.remove(10)
# searchitem = L.search(55)
indexitem = L[2]
print(L.n)

print(indexitem)


# Watching vedio length 05.06min



