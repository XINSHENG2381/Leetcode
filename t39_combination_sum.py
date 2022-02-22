def function(candidates,target):
    lst = []
    def dfs(target,combine,idx):
        if idx == len(candidates):
            return
        if target == 0:
            return lst.append(candidates[idx])

        dfs(target,combine,idx+1)
        if target - candidates[idx] >= 0:
            dfs(target-candidates[idx],combine.append(candidates[idx]),idx)

    return dfs(target,list(),0)
            


candidates = [2,3,6,7]
target = 7
combine = []
idx = 0
print(function(candidates,target))
