# class Solution:
#     def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
#         cur_array = nums[:k]
#         max_num = max(cur_array)
#         result = [max_num]
#         for i in range(1, len(nums)-k + 1):
#             cur_array.append(nums[k+i-1])
#             cur_array.pop(0)
#             max_num = max(cur_array)
#             result.append(max_num)
        
#         return result

# if __name__ == '__main__':
#     sol = Solution()
#     nums = [1,3,-1,-3,5,3,6,7]
#     k = 3
#     result = sol.maxSlidingWindow(nums, k)
#     print(result)


# ------------------------ #
# nums = [1,3,-1,-3,5,3,6,7]
# k = 3
# cur_array = nums[:k]
# max_num = max(cur_array)
# result = [max_num]
# for i in range(1, len(nums)-k + 1):
#     cur_array.append(nums[k+i-1])
#     cur_array.pop(0)
#     max_num = max(cur_array)
#     result.append(max_num)

# print(result)

# ------------------------ #
# import heapq
# nums = [1,3,-1,-3,5,3,6,7]
# k = 3
# n = len(nums)
# q = [(-nums[i], i) for i in range(k)]
# heapq.heapify(q)
# print('heapified q = ', q)
# ans = [-q[0][0]]
# print('initial ans = ', ans)
# for i in range(k, n):
#     heapq.heappush(q, (-nums[i], i))
#     while q[0][1] <= i - k:
#         heapq.heappop(q)
#     ans.append(-q[0][0])
#     print('i = ', i, ' |   q = ', q)

# print(ans)




# cur_array = nums[:k]
# max_num = max(cur_array)
# result = [max_num]
# for i in range(1, len(nums)-k + 1):
#     max_num = max(max_num, nums[k+i-1])


#     result.append(max_num)

# print(result)


class MyQueue: #单调队列（从大到小
    def __init__(self):
        self.queue = [] #使用list来实现单调队列
    
    #每次弹出的时候，比较当前要弹出的数值是否等于队列出口元素的数值，如果相等则弹出。
    #同时pop之前判断队列当前是否为空。
    def pop(self, value):
        if self.queue and value == self.queue[0]:
            self.queue.pop(0)#list.pop()时间复杂度为O(n),这里可以使用collections.deque()
            
    #如果push的数值大于入口元素的数值，那么就将队列后端的数值弹出，直到push的数值小于等于队列入口元素的数值为止。
    #这样就保持了队列里的数值是单调从大到小的了。
    def push(self, value):
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)
        
    #查询当前队列里的最大值 直接返回队列前端也就是front就可以了。
    def front(self):
        return self.queue[0]
    
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        que = MyQueue()
        result = []
        for i in range(k): #先将前k的元素放进队列
            que.push(nums[i])
        result.append(que.front()) #result 记录前k的元素的最大值
        for i in range(k, len(nums)):
            que.pop(nums[i - k]) #滑动窗口移除最前面元素
            que.push(nums[i]) #滑动窗口前加入最后面的元素
            result.append(que.front()) #记录对应的最大值
        return result

if __name__ == '__main__':
    sol = Solution()
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(sol.maxSlidingWindow(nums,k))

