class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        def check(comb,left,right):
            if left==n and right==n:
                result.append(comb)
                return
            if left < n:
                check(comb+'(',left+1,right)
            if right < left:
                check(comb+')',left,right+1)
        check('',0,0)
        return result