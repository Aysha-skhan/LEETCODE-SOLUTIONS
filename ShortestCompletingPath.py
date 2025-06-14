class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        d = {}
        result = []
        for y in range(len(licensePlate)):
            if ord(licensePlate[y]) >= 65:
                c = licensePlate[y].lower()
                if c in d:
                    d[c] += 1
                else:
                    d[c] = 1
        # print(d)
        for m in range(len(words)):
            if len(words[m]) >= len(d):
                # print('check-->',words[m])
                chk = 0
                for key, value in d.items():
                    if words[m].count(key) < value:
                        # print(words[m],key)
                        chk = -1
                        break
                if chk ==0 :
                    # print('yes')
                    result.append(words[m])
        minn = len(result[0])
        ans = result[0]
        for n in range(1, len(result)):
            if len(result[n]) < minn:
                minn = len(result[n])
                ans = result[n]
        return ans
