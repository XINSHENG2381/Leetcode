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


######## l1 & l2 are listnodes ########
### To calculate the length of listnodes:
# def len_link(list):
#     temp=list.head
#     count=0
#     while(temp):
#         count+=1
#         temp=temp.next
#     return count


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def len_link(self, list):
#         temp=list.head
#         count=0
#         while(temp):
#             count+=1
#             temp=temp.next
#         return count



#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         # len1 = len(l1)
#         # len2 = len(l2)
#         len1 = self.len_link(l1)
#         len2 = self.len_link(l2)
#         # print(len1,len2)
#         num1 = 0
#         for i in range(len1):
#             num1 = num1 + 10**(i)*l1[i]

#         # print(num1)
#         num2 = 0
#         for i in range(len2):
#             num2 = num2 + 10**(i)*l2[i]

#         Added = num1 + num2
#         # print(Added)
#         str_added = str(Added)
#         # print(str_added)
#         lenAdded = len(str_added)
#         # print(lenAdded)
#         lst = []
#         temp = Added
#         i = lenAdded
#         while i > 0:
#             t = temp//(10**(i-1))
#             lst.append(t)
#             temp = temp - t * (10**(i-1))
#             i = i - 1

#         # print(lst)
#         re_lst = []
#         # print(len(lst))
#         for i in range(len(lst)-1,-1,-1):
#             re_lst.append(lst[i])

#         return re_lst

        

