class Solution:
    def binarySearch(self,nums,target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right - left)//2 + left
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
            
        return -1

if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,3,4,5]
    target = 3
    print(sol.binarySearch(nums,target))
     



# d = dict()
# for idx, value in enumerate(nums):
#     d[idx] = value

# # print(d)
# left = d[0]
# right = d[len(nums)-1]
# print(left)
# print(right)
# l_idx = 0
# left = nums[l_idx]
# r_idx = len(nums)-1
# right = nums[r_idx]
 
# while (l_idx + 1) < r_idx:
#     if target < left or target > right:
#         # return -1
#         print(-1)
#         break
#     # mid = nums[int(len(nums)/2)]
#     m_idx = int((l_idx + r_idx)/2)
#     mid = nums[m_idx]
#     if target == mid:
#         # return int(len(nums)/2)
#         print(m_idx)
#         break
#     elif target < mid:
#         right = mid
#         r_idx = m_idx
#     else:
#         left = mid
#         l_idx = m_idx

# print(-1)