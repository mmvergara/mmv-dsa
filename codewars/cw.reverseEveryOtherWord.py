def reverse_alternate(s:str):
    # if odd reverse the string, else dont
    return " ".join([x if i % 2 == 0 else x[::-1] for i,x in enumerate(s.split())])

print(reverse_alternate("WHAT YOWW "))