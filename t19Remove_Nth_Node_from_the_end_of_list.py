class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = ListNode(data, self.head)
        self.head = node

    def ll_print(self):
        if self.head is None:
            print('This linkedlist is empty')
            return
        itr = self.head
        llstr = ''
        while itr:
            # print(itr.data)
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

# def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    # dummyhead = ListNode(-1,head)
    # p1,p2 = dummyhead,dummyhead
head = LinkedList()
head.insert_at_beginning(1)
head.insert_at_beginning(2)
head.insert_at_beginning(3)
head.insert_at_beginning(4)
head.insert_at_beginning(5)
head.ll_print()

# p1, p2 = head, head
# for i in range(n):
#     p2 = p2.next

    
    
    
# print(p1)
# print('\n\n')
# print(p2)