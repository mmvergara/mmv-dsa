

def productExceptSelf(self, nums: list[int]) -> list[int]:
    prefix = []
    postfix = [0 for i in range(len(nums))] 

    # populate postifx
    prod = 1
    for n in nums:
        prod*=n
        prefix.append(prod)

    # populate prefix
    prod = 1
    for i in range(len(nums)-1,-1,-1):
        prod*=nums[i]
        postfix[i] = prod
    prod = 0
    
    out = []
    # calculate product
    print(prefix)
    for i in range(len(nums)):
        prefixProd = 1
        postfixProd = 1

        # if there is a prefix
        if (i-1) >= 0:
            prefixProd = prefix[i-1]

        # if there is a postfix
        if (i+1) <= len(nums)-1:
            postfixProd = postfix[i+1]

        out.append(postfixProd*prefixProd)

    return out
    






productExceptSelf("",[1,2,3,4])
