#climbing using dp
class Solution:
    def __init__(self):
        self.dp=None
    def climbStairs(self, n: int) -> int:
        if self.dp is None:
            self.dp = [-1] * (n + 1)
            self.dp[0] = 1
            self.dp[1] = 1

        if self.dp[n]!=-1:
            return self.dp[n]
        else:
            self.dp[n]=self.climbStairs(n-1)+self.climbStairs(n-2)
            return self.dp[n]
