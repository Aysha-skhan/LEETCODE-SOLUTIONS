from collections import Counter
def findAnagrams(s: str, p: str):
    indexes=[]
    upto=len(p)
    d = {}
    for m in range(len(p)):
        if p[m] not in d:
            d[p[m]] = 1
        else:
            d[p[m]] += 1
    p_count=d
    # print(p_count)
    new=[]
    for k in range(len(s)-(upto-1)):
        check=s[k:k+upto]
        new.append(check)
    for y in range(len(new)):
        if Counter(new[y])==p_count:
            indexes.append(y)
    return indexes

print(findAnagrams("cbaebabacd","abc"))


# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         indexes = []
#         upto = len(p)
#         d = {}
#         for m in range(len(p)):
#             if p[m] not in d:
#                 d[p[m]] = 1
#             else:
#                 d[p[m]] += 1
#         # print(d)
#         for k in range(len(s) - (upto - 1)):
#             check = list(s[k:k + upto])
#             count_letters = 0
#             for u in range(len(check)):
#                 if check[u] in d:
#                     if check.count(check[u]) == d[check[u]]:
#                         count_letters += 1
#                 else:
#                     break
#             if count_letters == upto:
#                 indexes.append(k)
#         return indexes


