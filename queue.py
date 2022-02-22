# # from tkinter import W


# wmt_stock_price_queue = []
# wmt_stock_price_queue.insert(0,131.10)
# wmt_stock_price_queue.insert(0,131.20)
# wmt_stock_price_queue.insert(0,131.30)

# # print(wmt_stock_price_queue)
# print(wmt_stock_price_queue.pop())
# print(wmt_stock_price_queue.pop())
# print(wmt_stock_price_queue.pop())
# print(wmt_stock_price_queue.pop())

###### import module ######
# from collections import deque
# q = deque()
# q.appendleft(5) # add x to the left side of the deque...cf. q.append(): add x to the right side of the deque
# q.appendleft(8)
# q.appendleft(28)
# q.appendleft(17)
# print(q.pop())
# print(q.pop())
# print(q.pop())
# print(q.pop())
# print(q.pop())


from collections import deque
class Queue:
    def __init__(self):
        self.buffer = deque()
        return

    def enqueue(self,val):
        self.buffer.appendleft(val)
        return
    
    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

pq = Queue()
pq.enqueue({'company':'Wall Mart','timestep':'15 apr, 11.02 AM','price': 132})
pq.enqueue({'company':'Wall Mart','timestep':'15 apr, 11.03 AM','price': 135})
pq.enqueue({'company':'Wall Mart','timestep':'15 apr, 11.04 AM','price': 133})

print(pq.dequeue())
print(pq.dequeue())
# print(pq.dequeue())

print(pq.is_empty())
print(pq.size())