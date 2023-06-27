def countVowelStrings(self, n: int) -> int:
    vowels = ['a','e','i','o','u']


    def count(m,last=""):
        if m == 0:
            return 1
        else:
            mb = 0
            for vowel in vowels:
                if last <= vowel:
                    mb += count(m-1,vowel)
            return mb
        
    
    pass





res = countVowelStrings("",2)
print(res)