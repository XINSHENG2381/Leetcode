# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         def cover_string(sub_s, t):
#             for letter in t:
#                 if sub_s.find(letter) == -1:
#                     return False
            
#             return True
        

#         if len(s) < len(t):
#             return ""
        
#         start = 0
#         end = 1
#         min_length = float('inf')
#         sub_s = ""
#         result = sub_s

#         while end <= len(s):
#             sub_s = s[start:end+1]
#             # print(sub_s)
#             if cover_string(sub_s, t):
#                 if min_length > len(sub_s):
#                     min_length = len(sub_s)
#                     result = sub_s
#                 start += 1

#             else:
#                 end += 1
        
#         return result



# if __name__ == "__main__":
#     sol = Solution()
#     s = "ADOBECODEBANC"
#     t = "ABC"
#     # s = 'aa'
#     # t = 'aa'
#     print(sol.minWindow(s,t))



class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def mapping(string):
            string_map = dict()
            for letter in string:
                if letter in string_map:
                    string_map[letter] += 1
                else:
                    string_map[letter] = 1 
            return string_map

        def cover_string(sub_s_map, t_map):
            if len(sub_s) < len(t):
                return False
            for k,v in t_map.items():
                if not k in sub_s_map.keys():
                    return False
                elif v > sub_s_map[k]:
                    return False   
            return True

        if len(s) < len(t):
            return ""
        
        start = 0
        end = 0
        min_length = 100001
        left, right = start, end

        while end <= len(s):
            sub_s = s[start:end]
            sub_s_map = mapping(sub_s)
            t_map = mapping(t)
            if cover_string(sub_s_map, t_map):
                if min_length > len(sub_s):
                    min_length = len(sub_s)
                    left, right = start, end
                start += 1
            else:
                end += 1
        return s[left:right]