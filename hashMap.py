# def get_hash(key):
#     h = 0
#     for char in key:
#         h += ord(char)
    
#     return h % 100   # mod 此处取100的余数 

class hashTable:
    def __init__(self):
        self.max = 100
        self.arr = [None for i in range(self.max)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        
        return h % self.max   # mod 此处取100的余数，h为hash table 内部的index

    def __setitem__(self,key,val): # std function in Python
    # def add_hash(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self,key):
    # def get(self,key): #查找key以获得value
        h = self.get_hash(key)
        return self.arr[h]


t =  hashTable()
# print(t.get_hash('march 6'))
# t.add_hash('march 6', 130)
# print(t.arr)
 
# print(t.get('march 6'))
t['march 6'] = 130
t['may 1'] = 20
t['april 5'] = 80
print(t.arr) 


