# def dec_to_binary(num:int,result="")->str:
#     if num == 0:
#         return result
#     result = str(num % 2 ) + result
#     return dec_to_binary(num // 2, result)

def dec_to_binary_count_1(num:int,count=0)->str:
    if num == 0:
        return count
    if num % 2 == 1:
        count+=1
    return dec_to_binary_count_1(num // 2, count)

# def dec_to_binary_nr(num:int,result="")->str:
#     result = ""
#     while(num != 0):
#       if(num % 2 == 0):
#           result = "0" + result
#       else:
#           result = "1" + result
#       num = int(num/2)
#     return result
        
print(dec_to_binary_count_1(15))

# 15 -4
# 5 - 2