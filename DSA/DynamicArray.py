

# Checking how memory allocating in python list.
""" import sys

L = []

for i in range(100):
    print(i," current size ",sys.getsizeof(L))
    L.append(i)
    print(L) """


# watching vedio length 02.00min

import ctypes


# Creating my own list and estrabishing here all the methods that is available in python list.
class MyList:

    def __init__(self):
        self.size = 1
        self.n = 0

        self.A = self.__make_array(self.size)

    # for length
    def __len__(self):
        return self.n

    # for append
    def append(self, item):
        if self.n == self.size:
            # resize
            self.__resize(self.size*2)

        # append
        self.A[self.n] = item
        self.n = self.n + 1

    def __resize(self, new_capacity):
        # create a new array with new capacity
        B = self.__make_array(new_capacity)
        self.size = new_capacity
        # copy the content of A to B
        for i in range(self.n):
            B[i] = self.A[i]
        # reassign A
        self.A = B

    # For Print

    def __str__(self):
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','
        return '[' + result[:-1] + ']'

    #  For Indexing
    def __getitem__(self, index):
        if 0 <= index < self.n:
            return self.A[index]
        else:
            return 'IndexError - Index out of range'

    # For Pop
    def pop(self):
        if self.n == 0:
            return 'Empty List'

        print(self.A[self.n-1])
        self.n = self.n-1

    # For Clear
    def clear(self):
        self.n = 0
        self.size = 1

    # For Find
    def find(self, item):
        for i in range(self.n):
            if self.A[i] == item:
                return i

        return 'ValueError - not in list'

    # For Insert
    def insert(self, pos, item):
        # if size of is less than it increase
        if self.n == self.size:
            self.__resize(self.size*2)

        for i in range(self.n, pos, -1):
            self.A[i] = self.A[i-1]
        self.A[pos] = item
        self.n = self.n + 1

    # For delete
    def __delitem__(self, pos):
        if 0 <= pos < self.n:
            for i in range(pos, self.n-1):
                self.A[i] = self.A[i+1]
            self.n = self.n - 1

    # For remove
    def remove(self, item):
        pos = self.find(item)

        if type(pos) == int:
            self.__delitem__(pos)
        else:
            return pos

    def __make_array(self, capacity):
        return (capacity*ctypes.py_object)()


List = MyList()
List.append("Jahid")
List.append(201041)
List.append(True)
List.append("Hasan")
# print(len(List))

# print(List)
# print(type(List[3]))
# print(List.pop())
# List.clear()

# print(List.find("Hasan"))

# List.insert(2,"Ma Kon Hoo")

# del List[1]

List.remove("Jahid")


print(List)

# Watching vedio length 02.50min
