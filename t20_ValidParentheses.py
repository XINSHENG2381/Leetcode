# class Solution:
# def isValid(self, s: str) -> bool:
def isValid(s):
    while '{}' in s or '()' in s or '[]' in s:
        s = s.replace('{}', '')
        s = s.replace('[]', '')
        s = s.replace('()', '')
    return s == ''


    # lst = []
    # for ss in s:
    #     if ss == '(':
    #         lst.append('(')
    #         continue
    #     if ss == '[':
    #         lst.append('[')
    #         continue
    #     if ss == '{':
    #         lst.append('{')
    #         continue

    #     if ss == ')' and '(' in lst:
    #         lst.remove('(')
    #         if lst == []:
    #             return True
    #         continue

    #     if ss == ']' and '[' in lst:
    #         lst.remove('[')
    #         if lst == []:
    #             return True
    #         continue

    #     if ss == '}' and '{' in lst:
    #         lst.remove('{')
    #         if lst == []:
    #             return True
    #         continue
        
    #     return False    
        


if __name__ == '__main__':


    s = '{(})'
    print('\n\n\n')
    print(isValid(s))
    print('\n\n\n')