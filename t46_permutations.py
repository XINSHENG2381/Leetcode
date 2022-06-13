class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []

        # base case
        if len(nums) == 1:
            # return [nums.copy()]
            return [nums[:]]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            # n = nums.pop(-1)
            perms = self.permute(nums) 

            for perm in perms:
                perm.append(n)
                # perm.insert(0,n)

            result.extend(perms)
            nums.append(n)
            # nums.insert(0,n)

        return result

if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,3]
    print(sol.permute(nums))
        
