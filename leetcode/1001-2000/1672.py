
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0

        for acc in accounts:
            totalMoney = 0 
            for m in acc:
                totalMoney+=m
            richest = max(richest,totalMoney)

        return richest


        
