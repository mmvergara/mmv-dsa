
# uses recursive to count bits
# Take a num and then recursively divide it by 0 and taking the remainder to count
# more info on freecodecamp Recursion in programming video 29:00

def countBits(self, n: int) -> list[int]:
    def dec_to_binary_count_1(num:int,count=0)->str:
      if num == 0:
          return count
      if num % 2 == 1:
          count+=1
      return dec_to_binary_count_1(num // 2, count)
    out_arr = []
    for i in range(n+1):
        out_arr.append(dec_to_binary_count_1(i))
    return out_arr
    


print(countBits("",2))