####### 链表 #########
class node: # a sublist for linked list 
    def __init__(self,data = None):
        self.data = data
        self.next = None     #The next() function returns the next item from the iterator.

class linkedList:
    def __init__(self):
        self.head = node()

    def append(self,data):
        newNode = node(data)
        cur = self.head # cur --- current node
        while cur.next != None:
            cur = cur.next
        cur.next = newNode
    
    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        elems = []
        curNode = self.head
        while curNode.next != None:
            curNode = curNode.next
            elems.append(curNode.data)
        print(elems)

    def get(self,index):
        if index >= self.length():
            print('Error: get(index) out of range')
            return None
        curIndex = 0
        curNode = self.head
        while True:
            curNode = curNode.next
            if curIndex == index: return curNode
            
            curIndex += 1

    def erase(self,index):
        if index >= self.length():
            print('Error: get(index) out of range')
            return
        curIndex = 0
        curNode = self.head
        while True:
            lastNode = curNode
            curNode = curNode.next
            if curIndex == index:
                lastNode.next = curNode.next
                return
            curIndex += 1





myList = linkedList()

myList.append(0)
myList.append(1)
myList.append(2)
myList.append(3)
myList.append(4)

myList.display()
print(f'Element at 2nd Index: {myList.get(2)}')

myList.erase(1)
print('After erasing Index 1: ', end = '')
myList.display()


