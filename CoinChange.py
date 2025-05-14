class Solution:
    # dp used if cant come up with amount return -1
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coins_needed=[amount+1]*(amount+1)
        min_coins_needed[0]=0
        # CURRENT
        for curr_amount in range(1,amount+1):
            for curr_coin in coins:
                if curr_amount - curr_coin >=0:
                    min_coins_needed[curr_amount]=min(min_coins_needed[curr_amount],1+(min_coins_needed[curr_amount-curr_coin]))
        if  min_coins_needed[-1]==(amount+1):
            return -1
        else:
             return min_coins_needed[-1]
        
