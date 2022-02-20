####### Treating l1 & l2 as lists ############

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
len1 = len(l1)
len2 = len(l2)
# print(len1,len2)
num1 = 0
for i in range(len1):
    num1 = num1 + 10**(i)*l1[i]

# print(num1)
num2 = 0
for i in range(len2):
    num2 = num2 + 10**(i)*l2[i]

Added = num1 + num2
# print(Added)
str_added = str(Added)
# print(str_added)
lenAdded = len(str_added)
# print(lenAdded)
lst = []
temp = Added
i = lenAdded
while i > 0:
    t = temp//(10**(i-1))
    lst.append(t)
    temp = temp - t * (10**(i-1))
    i = i - 1

# print(lst)
re_lst = []
# print(len(lst))
for i in range(len(lst)-1,-1,-1):
    re_lst.append(lst[i])

print(re_lst)


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

######### Submitted on Leetcode ##########
'''
class Solution:


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:        
        l1_list = []
        while True:
            l1_list.append(l1.val)
            l1 = l1.next
            if l1 == None:
                break
        # print(l1_list)
        
        l2_list = []
        while True:
            l2_list.append(l2.val)
            l2 = l2.next
            if l2 == None:
                break

        len1 = len(l1_list)
        len2 = len(l2_list)
        num1 = 0
        for i in range(len1):
            num1 = num1 + 10**(i)*l1_list[i]

        # print(num1)
        num2 = 0
        for i in range(len2):
            num2 = num2 + 10**(i)*l2_list[i]

        Added = num1 + num2
        # print(Added)
        str_added = str(Added)
        # print(str_added)
        lenAdded = len(str_added)
        # print(lenAdded)
        lst = []
        temp = Added
        i = lenAdded
        while i > 0:
            t = temp//(10**(i-1))
            lst.append(t)
            temp = temp - t * (10**(i-1))
            i = i - 1

        # print(lst)
        re_lst = []
        # print(len(lst))
        for i in range(len(lst)-1,-1,-1):
            re_lst.append(lst[i])
        
        res_nodes = cur = ListNode()
        # y = enumerate(re_lst)
        # print(list(y))
        
        ######### return ListNode() ###########
        for idx, value in enumerate(re_lst):
            cur.val = value #supply the parameter first
            if idx < len(re_lst)-1:
                nextNode = ListNode()
                cur.next = nextNode
                cur = cur.next
                # cur = nextNode #此处不能替换为 cur = ListNode() 因ListNode是创造一个新的node而cur = nextNode是指向与cur.next相同的node
        ######### return ListNode() #############  
            
        
        return res_nodes
        
'''
        



        

