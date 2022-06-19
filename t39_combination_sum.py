# def function(candidates,target):
#     lst = []
#     def dfs(target,combine,idx):
#         if idx == len(candidates):
#             return
#         if target == 0:
#             return lst.append(candidates[idx])

#         dfs(target,combine,idx+1)
#         if target - candidates[idx] >= 0:
#             dfs(target-candidates[idx],combine.append(candidates[idx]),idx)

#     return dfs(target,list(),0)
            


# candidates = [2,3,6,7]
# target = 7
# combine = []
# idx = 0
# print(function(candidates,target))

'''
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        def dfs(candidates, target, result, depth, start, size):
            # base case
            if target == 0:
                # result.append(candidate)
                # print('added')
                return 

            if target < min(candidates):
                result = []
                return
            
            for index in range(start, size):
                if candidates[index] <= target:
                    candidate = candidates[index]
                    target = target - candidates[index]
                    # if target < min(candidates):
                    #     result = []
                    #     return
                    result.append(candidates[index])
                    print('added')
                    dfs(candidates, target, result, depth + 1, index, size)

                
            results.extend([result])
            return results
            
        results = []
        result = []
        start = 0
        size = len(candidates)
        return dfs(candidates, target, result, 0, start, size)
'''
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        def dfs(candidates, target, results, result, start, size, depth):
            # base case
            if target == 0:
                results.append(result)
                return 

            if target < 0:
                return
            
            for index in range(start, size):  
                # 写在内部与写在外部的区别？
                # target -= candidates[index]
                # result += [candidates[index]]
                # dfs(candidates, target, results, result, index, size, depth + 1)

                dfs(candidates, target - candidates[index], results, result + [candidates[index]], index, size, depth + 1)

            
            # return results
            
        results = []
        result = []
        start = 0
        size = len(candidates)
        depth = 0
        if size == 0:
            return []
        dfs(candidates, target, results, result, start, size, depth)
        return results

'''
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(candidates, begin, size, path, res, target):
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return

            for index in range(begin, size):
                dfs(candidates, index, size, path + [candidates[index]], res, target - candidates[index])

        size = len(candidates)
        if size == 0:
            return []
        path = []
        res = []
        dfs(candidates, 0, size, path, res, target)
        return res
'''


if __name__ == '__main__':
    candidates = [2,3,6,7]
    target = 7
    sol = Solution()
    print(sol.combinationSum(candidates, target))
