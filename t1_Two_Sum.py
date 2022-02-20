# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

####### Memory Limit Exceed #########
# nums = [2,7,11,15]
# target = 9
# n = len(nums)
# table = [[0 for k in range(n)] for k in range(n)]
# # print(table)
# output = []

# for i in range(n):
#     for j in range(n):
       
#         if i == j:
#             continue
#         table[i][j] = nums[i] + nums[j]
#         if target == table[i][j]:
#             output.append(i)
#             output.append(j)
#             break

# # output = list(set(output))



# print(output[:2])


# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

nums = [2,7,11,15]
target = 9
dic = {}
lst = []
for idx, value in enumerate(nums):
    if value in dic:
        lst.append(dic[value])
        lst.append(idx)
        # print(dic[value],idx)
    else:
        dic[target-value] = idx

print(lst)
