class Node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
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
    
    def insert_at_end(self,data):
        if self.head is None:
            node = Node(data,None)
            self.head = node
            # self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next: #iterate until point to the end: None
            itr = itr.next
        
        node = Node(data,None)
        itr.next = node

        return

    def insert_values(self,data_list):
        self.head = None # datalist insert to the end, point to the end
        for data in data_list:
            self.insert_at_end(data)
        return

    def get_length(self):
        count = 0
        itr = self.head
        while itr: #interate until it is None
            itr = itr.next
            count += 1
        return count

    def remove_at(self,index):
        if index<0 or index >= self.get_length():
            raise Exception('Invalid Index!!!')
        
        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break # remember to break to loop! OR just return
            itr = itr.next
            count += 1
        
        return
            
    def insert_at(self, index,data):
        if index<0 or index >= self.get_length():
            raise Exception('Invalid Index!!!')   

        if index == 0:
            self.head = Node(data, self.head)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                itr.next = Node(data,itr.next)
                # break
                return
            count += 1
            itr = itr.next
        
        # return
            

        


        


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(89)
    ll.insert_at_end(17)
    ll.insert_at_end(190)
    ll.insert_at_end(67)
    ll.insert_at_end(12)
    
    # ll.insert_values(['mango','apple','banana'])
    ll.ll_print()
    ll.remove_at(0)
    ll.ll_print()
    ll.insert_at(2,666)
    ll.insert_at(2,8888)
    ll.ll_print()
    print('length of the linkedlist:' , ll.get_length())