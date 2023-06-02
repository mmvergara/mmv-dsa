def sum_of_all_natural_numbers(num):
    if num == 0:
        return 0
    print(num)
    return sum_of_all_natural_numbers(num-1) + num
    
print(sum_of_all_natural_numbers(10))