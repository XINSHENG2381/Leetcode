'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
'''

'''
class Solution:
    def reverse(self, x: int) -> int:
'''

a = 105
b = 10
c = a%b
print(c)
d = int((a-c)/10%b)
# print(int((a-c)/10%b))
print(d)
e = int((a-c-10*d)/100%b)
print(e)

print(100*c + 10*d + e)