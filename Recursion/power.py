def power(num:int,expo:int):
    if expo == 1:
        return num
    
    return num * power(num,expo-1)

print(power(2,4))