
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