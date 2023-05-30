def dec_to_binary(num:int,result:str)->str:
    if num == 0:
        return result
    result = str(num % 2 ) + result
    return dec_to_binary(int(num / 2), result)




def dec_to_binary_nr(num:int,result:str)->str:
    result = ""
    while(num != 0):
      if(num % 2 == 0):
          result = "0" + result
      else:
          result = "1" + result
      num = int(num/2)
    return result
        
print(dec_to_binary_nr(233,""))
