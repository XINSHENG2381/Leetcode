# class linkednode:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#         # self.index = []

#     def add_node(self,data):
#         cur = self
#         while cur.next:
#             cur = self.next
#         cur.data = data
    
#     def linkednode_length(self):
#         count = 0
#         cur = self
#         while cur.next:
#             count += 1
#             cur = cur.next
#         return count

#     def insert_node(self,node,index):
#         cur = self
#         i = 0
#         while cur.next:
#             if i == index:
#                 cur.next = node
#             i += 1
       
from lib2to3.pytree import Node


if __name__ == '__main__':
    # lst = []
    # cur = linkedListNode
    # while cur.next != None:
    #     lst.append(cur.data)
    #     cur = cur.next
    # p1 = Node
    # p2 = Node.next
    # temp = p1
    # p1 = p2
    # p2 = temp

    # p2 = p1.next
    # temp = p1
    # p1 = p2
    # p2 = temp    

    p1 = Node
    p2 = Node.next

    while p2.next != None:
        temp = p1
        p1 = p2
        p2 = temp
        p2.next = p1            
        p1 = Node
    







