class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first={'q','w','e','r','t','y','u','i','o','p'}
        second={'a','s','d','f','g','h','j','k','l'}
        third={'z','x','c','v','b','m','n'}
        out=[]
        for k in range(len(words)):
            tmp=set(words[k].lower())
            if tmp.issubset(first) or tmp.issubset(second) or tmp.issubset(third):
                out.append(words[k])
        return out
