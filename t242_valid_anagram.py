s = 'anagram'
t = 'nagaram'
dic_s = {}
for i,v in enumerate(s):
    if v in dic_s:
        dic_s[v] += 1
    else:
        dic_s[v] = 1
print(dic_s)

dic_t = {}
for i,v in enumerate(t):
    if v in dic_t:
        dic_t[v] += 1
    else:
        dic_t[v] = 1

print(dic_t)
print(dic_s == dic_t)