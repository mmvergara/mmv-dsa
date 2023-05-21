
# num should be lower or equal than num2
def greatest_common_factor(num1,num2):
  if(num1 > num2):
    num1,num2 = num2,num1

  while num1%num2 != 0:
    remainder = num2%num1
    print(remainder)
    old_num1 = num1
    num1 = remainder
    num2 = old_num1
    
  print(num2)
  return num2

  




greatest_common_factor(54,888)