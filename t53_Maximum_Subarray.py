class Solution:
    def maxSubArray(self, nums):
    # ###### 贪心算法 ######
    # ###每一步采取当前的最优解：若当前所指元素之前的和小于0，则丢弃当前元素之前的序列 ###
    #     cur_sum, max_sum = nums[0], nums[0]
    #     for i in range(1,len(nums)):           
    #         # cur_sum += nums[i] if nums[i]>0 else 0
    #         cur_sum = max(nums[i], cur_sum + nums[i])
    #         max_sum = max(max_sum, cur_sum)
    #     return max_sum

    ###### 动态规划 ######
        for i in range(1,len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
    
        return max(nums)


if __name__ == '__main__':
    sol = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print('-'*10)
    print(sol.maxSubArray(nums))
    print('-'*10)