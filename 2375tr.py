def smallestNumber(self, pattern: str) -> str:
        ans = []
        stack = []
        for i in range(len(pattern)+1): 
            stack.append(str(i+1))
            print("Append")
            print(stack)
            if i == len(pattern) or pattern[i] == 'I': 
                while stack: 
                    ans.append(stack.pop())
                    print("ans")
                    print(ans)
        return ''.join(ans) 



#smallestNumber("","IIIDIDDD")
smallestNumber("","IIIDIDDD")
    



         



