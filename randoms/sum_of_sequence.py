def sequence_sum(begin_number, end_number, step):
    cur_num = begin_number
    out = []
    while(end_number >= cur_num):
      if cur_num > end_number :
         continue
      print(cur_num)
      out.append(cur_num)
      cur_num += step
    return sum(out)

res = sequence_sum(2,6,2)
# print(res) 

print(list(range(1,16,2)))
# 12