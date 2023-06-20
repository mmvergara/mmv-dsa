def reverse_string(strr:str):
    print(strr)
    if strr == "":
        return ""
    return reverse_string(strr[1:]) + strr[0]


print(reverse_string("Hello"))