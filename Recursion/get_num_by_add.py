def get_num_by_add(start_num,end_num):
    if end_num == start_num:
        return
    print(start_num)
    return get_num_by_add(start_num + 1,end_num)


print(get_num_by_add(1,5))