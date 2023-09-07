class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        rulekeys = {
            "type":0,
            "color":1,
            "name":2
        }
        ans = 0
        for item in items:
            if item[rulekeys[ruleKey]] == ruleValue:
                ans+=1
        return ans
