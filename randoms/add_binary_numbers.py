def add_binary(bin1,bin2):
    return bin(int(bin1,2) +int(bin2,2))[2:]


print(add_binary("101","110"))
