# ##### Use list() as stack #######
# s = []
# s.append('https://www.cnn.com/')
# s.append('https://www.cnn.com/world')
# s.append('https://www.cnn.com/india')
# s.append('https://www.cnn.com/china')

# print(s)
# print(s[-1])
# print(s.pop())
# print(s.pop())
# print(s.pop())



# from collections import deque
# stack = deque()
# print(dir(stack)) #dir() return all attributes of this object
# stack.append('https://www.cnn.com/')
# stack.append('https://www.cnn.com/world')
# stack.append('https://www.cnn.com/india')
# stack.append('https://www.cnn.com/china')

# print(stack[-1])
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())

from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()

    def push(self,val):
        self.container.append(val)
        return
    
    def pop(self):
        self.container.pop()
        return
    
    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

sk = Stack()
sk.push(123)
sk.push(456)
sk.push(789)
sk.pop()
print(sk.peek())
