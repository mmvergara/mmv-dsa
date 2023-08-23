
class Solution:
    def fizzBuzz(self, num: int) -> List[str]:
        res = [0] * num
        

        for i in range(num):
            n = i+1
            if n % 3 == 0 and n % 5 == 0:
                res[i] = "FizzBuzz"
                continue

            if n % 3 == 0:
                res[i] = "Fizz"
                continue

            if n % 5 == 0:
                res[i] = "Buzz"
                continue

            res[i] = str(n)

        return res

