class Solution:
    def fairCandySwap(self, alice, bob):
        sumA = sum(alice)
        sumB = sum(bob)       
        diff = (sumB - sumA) // 2
        sett = set(bob)
        
        for a in alice:
            if a + diff in sett:
                return [a, a + diff]
