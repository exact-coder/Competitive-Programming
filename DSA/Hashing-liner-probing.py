# 0123456789

class Dictionary:

    def __init__(self,size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size


    def put(self,key,value):
        hash_value = self.hash_function(key)

        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = value
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = value
            else:
                new_hash_value = self.rehash(hash_value)

                while self.slots[new_hash_value] != None and self.slots[new_hash_value] != key:
                    new_hash_value = self.rehash(new_hash_value)
                if self.slots[new_hash_value] == None:
                    self.slots[new_hash_value] = key
                    self.data[new_hash_value] = value
                else:
                    self.data[new_hash_value] = value
    
    def rehash(self,old_hash):
        return (old_hash + 1) % self.size
    
    def __str__(self):
        for i in range(len(self.slots)):
            if self.slots[i] != None:
                print(self.slots[i], ":", self.data[i],end=' ')
        return ""
    
    def __setitem__(self,key,value):
        self.put(key,value)

    def __getitem__(self,key):
        return self.get(key)

    def get(self,key):
        start_position = self.hash_function(key)
        current_position = start_position

        while self.slots[current_position] != None:
            if self.slots[current_position] == key:
                return self.data[current_position]
            
            current_position = self.rehash(current_position)

            if current_position == start_position:
                return "Not Found"
        return "Not Found"

    def hash_function(self,key):
        return abs(hash(key)) % self.size

D1 = Dictionary(3)

D1.put("Python",3)
D1.put("Python",37)
D1.put("Django",33)
D1.put("NextJS",333)
# D1.put("JS",333)

print(D1.slots)
print(D1.data)
print(D1.get("Django"))
print(D1)



# Watching vedio length 08.12min